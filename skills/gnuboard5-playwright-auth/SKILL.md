---
name: gnuboard5-playwright-auth
description: Sets up Playwright authentication for Gnuboard5 projects. This skill should be used when initializing Playwright tests for Gnuboard5, when user mentions "Gnuboard login test", "Gnuboard Playwright setup", "그누보드 로그인 테스트", or needs to test authenticated pages on Gnuboard5 sites. Handles the complex login flow so users can focus on writing unit tests.
---

# Gnuboard5 Playwright Auth

## Overview

This skill automates Playwright authentication setup for Gnuboard5 projects. After using this skill, the login authentication layer is fully configured, allowing users to immediately write unit tests without dealing with session management or login form handling.

## Quick Start Workflow

### Step 1: Configure Environment Variables

Create a `.env` file in the project root (where `package.json` is located):

```bash
cp .env.example .env
```

Edit `.env` with actual credentials:

```bash
# Gnuboard5 Playwright Test Configuration
BASE_URL=https://your-gnuboard-site.com
USER_ID=your_test_account_id
USER_PW=your_test_account_password
```

**Security Warning**: Never commit `.env` files containing real credentials to version control. Add `.env` to `.gitignore`.

### Step 2: Install Dependencies

```bash
npm install dotenv --save-dev
```

### Step 3: Copy Authentication Files

Copy the following files from this skill's `assets/` directory to the project:

| Source | Destination |
|--------|-------------|
| `assets/playwright.config.ts` | `playwright.config.ts` |
| `assets/gnuboard-auth.ts` | `tests/gnuboard-auth.ts` |
| `assets/.env.example` | `.env.example` |
| `assets/example.spec.ts` | `tests/example.spec.ts` (optional reference) |

### Step 4: Write Tests

Use the `GnuboardAuth` class in test files:

```typescript
import { test, expect } from '@playwright/test';
import { GnuboardAuth } from './gnuboard-auth';

test('can access member-only page', async ({ page }) => {
  const auth = new GnuboardAuth(page);
  await auth.ensureLoggedIn();
  
  // Now write your test logic - user is authenticated
  await page.goto('/bbs/board.php?bo_table=member_board');
  await expect(page.locator('.board_list')).toBeVisible();
});
```

## Usage Examples

### Basic Login Test

```typescript
import { test, expect } from '@playwright/test';
import { GnuboardAuth } from './gnuboard-auth';

test('login succeeds with valid credentials', async ({ page }) => {
  const auth = new GnuboardAuth(page);
  await auth.ensureLoggedIn();
  
  // Verify login by checking for logout link
  await expect(page.locator('a[href*="logout.php"]')).toBeVisible();
});
```

### Testing Member-Only Pages

```typescript
test.describe('Member Board Tests', () => {
  test('can view member board list', async ({ page }) => {
    const auth = new GnuboardAuth(page);
    await auth.ensureLoggedIn();
    
    await page.goto(process.env.BASE_URL + '/bbs/board.php?bo_table=member');
    await expect(page.locator('.board_list')).toBeVisible();
  });

  test('can write new post', async ({ page }) => {
    const auth = new GnuboardAuth(page);
    await auth.ensureLoggedIn();
    
    await page.goto(process.env.BASE_URL + '/bbs/write.php?bo_table=member');
    await page.fill('input[name="wr_subject"]', 'Test Post Title');
    await page.fill('textarea[name="wr_content"]', 'Test post content');
    await page.click('button[type="submit"]');
    
    await expect(page).toHaveURL(/board\.php/);
  });
});
```

### Multiple User Roles

```typescript
test.describe('Admin Tests', () => {
  test('admin can access admin page', async ({ page }) => {
    const auth = new GnuboardAuth(page);
    // Override default credentials for admin user
    await auth.ensureLoggedIn(
      process.env.ADMIN_ID || 'admin',
      process.env.ADMIN_PW || 'adminpassword'
    );
    
    await page.goto(process.env.BASE_URL + '/adm/');
    await expect(page.locator('.adm_content')).toBeVisible();
  });
});
```

### Using beforeEach for Multiple Tests

```typescript
test.describe('Authenticated User Tests', () => {
  test.beforeEach(async ({ page }) => {
    const auth = new GnuboardAuth(page);
    await auth.ensureLoggedIn();
  });

  test('can view profile', async ({ page }) => {
    await page.goto(process.env.BASE_URL + '/bbs/member_confirm.php?url=register_form.php');
    await expect(page.locator('form[name="fregisterform"]')).toBeVisible();
  });

  test('can view point history', async ({ page }) => {
    await page.goto(process.env.BASE_URL + '/bbs/point.php');
    await expect(page.locator('.point_list')).toBeVisible();
  });
});
```

## Customization

### Custom Login Form Selectors

If the Gnuboard5 site uses a custom theme with different login form selectors, extend the `GnuboardAuth` class:

```typescript
import { GnuboardAuth } from './gnuboard-auth';
import { Page } from '@playwright/test';

export class CustomThemeAuth extends GnuboardAuth {
  constructor(page: Page, baseUrl?: string) {
    super(page, baseUrl);
  }

  protected async performLogin(userId: string, userPw: string) {
    const loginUrl = this.baseUrl.endsWith('/') 
      ? `${this.baseUrl}bbs/login.php` 
      : `${this.baseUrl}/bbs/login.php`;

    await this.page.goto(loginUrl);

    // Custom selectors for your theme
    await this.page.fill('#custom_id_field', userId);
    await this.page.fill('#custom_pw_field', userPw);
    await this.page.click('#custom_login_button');

    await this.page.waitForLoadState('networkidle');
  }
}
```

### Handling Custom Login URL

```typescript
const auth = new GnuboardAuth(page, 'https://custom-domain.com');
await auth.ensureLoggedIn();
```

## GnuboardAuth API Reference

### Constructor

```typescript
constructor(page: Page, baseUrl?: string)
```

- `page`: Playwright Page instance
- `baseUrl`: Optional. Overrides `process.env.BASE_URL`

### Methods

#### ensureLoggedIn

```typescript
async ensureLoggedIn(userId?: string, userPw?: string): Promise<void>
```

Checks login status and performs login if needed.

- `userId`: Optional. Defaults to `process.env.USER_ID`
- `userPw`: Optional. Defaults to `process.env.USER_PW`
- Throws error if required environment variables are missing

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `BASE_URL` | Yes | Gnuboard5 site base URL (e.g., `https://example.com`) |
| `USER_ID` | Yes | Test account username |
| `USER_PW` | Yes | Test account password |
| `ADMIN_ID` | No | Admin account username (for admin tests) |
| `ADMIN_PW` | No | Admin account password (for admin tests) |

## Troubleshooting

See `references/troubleshooting.md` for common issues and solutions including:

- Login form selector issues with custom themes
- Session/cookie handling problems
- CAPTCHA handling strategies
- Timeout issues on slow servers
