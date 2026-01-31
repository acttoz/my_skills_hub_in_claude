# Gnuboard5 Playwright Auth 문제 해결 가이드

## 일반적인 문제와 해결책

### 1. 환경 변수 오류

#### 증상
```
Error: .env 파일에 BASE_URL이 설정되어 있지 않습니다.
```

#### 해결책
1. 프로젝트 루트에 `.env` 파일이 있는지 확인
2. `.env.example`을 복사하여 `.env` 생성:
   ```bash
   cp .env.example .env
   ```
3. `.env` 파일에 실제 값 입력
4. `playwright.config.ts` 상단에 `import 'dotenv/config';` 추가 확인

---

### 2. 로그인 폼 셀렉터 오류

#### 증상
```
Error: locator.fill: Error: Element not found
```
또는 로그인이 수행되지 않음

#### 원인
커스텀 테마에서 로그인 폼의 `input` 필드명이 다를 수 있음

#### 해결책

1. 브라우저 개발자 도구에서 실제 필드명 확인:
   ```javascript
   // 콘솔에서 실행
   document.querySelector('input[name="mb_id"]')
   document.querySelector('input[name="mb_password"]')
   ```

2. 필드명이 다른 경우 `GnuboardAuth` 클래스 확장:
   ```typescript
   import { GnuboardAuth } from './gnuboard-auth';
   import { Page } from '@playwright/test';

   export class CustomAuth extends GnuboardAuth {
     protected async performLogin(userId: string, userPw: string) {
       const loginUrl = `${this.baseUrl}/bbs/login.php`;
       await this.page.goto(loginUrl);
       
       // 커스텀 셀렉터 사용
       await this.page.fill('#your_id_field', userId);
       await this.page.fill('#your_pw_field', userPw);
       await this.page.click('.your_submit_button');
       
       await this.page.waitForLoadState('networkidle');
     }
   }
   ```

---

### 3. 타임아웃 오류

#### 증상
```
Error: Timeout 10000ms exceeded while waiting for locator('a[href*="logout.php"]')
```

#### 원인
- 서버 응답이 느림
- 로그인 실패 (잘못된 계정 정보)
- 로그아웃 링크 셀렉터가 테마에 맞지 않음

#### 해결책

1. **서버 응답 느림**: 타임아웃 값 증가
   ```typescript
   // playwright.config.ts
   export default defineConfig({
     timeout: 60000, // 전체 테스트 타임아웃
     expect: {
       timeout: 15000, // expect 타임아웃
     },
   });
   ```

2. **계정 정보 확인**: 브라우저에서 수동으로 로그인 테스트

3. **로그아웃 링크 셀렉터 확인**: 커스텀 테마의 로그아웃 링크 확인
   ```typescript
   // isLoggedIn 메서드 오버라이드
   protected async isLoggedIn(): Promise<boolean> {
     const logoutLink = this.page.locator('.your-logout-class, #logout-link');
     try {
       await logoutLink.waitFor({ state: 'visible', timeout: 3000 });
       return true;
     } catch {
       return false;
     }
   }
   ```

---

### 4. CAPTCHA 문제

#### 증상
로그인 페이지에 CAPTCHA가 표시되어 자동 로그인 불가

#### 해결책

**옵션 1: 테스트 환경에서 CAPTCHA 비활성화**
그누보드 관리자 → 기본환경설정 → 로그인 CAPTCHA 해제

**옵션 2: 테스트용 IP 화이트리스트**
서버 설정에서 테스트 서버 IP에 대해 CAPTCHA 면제

**옵션 3: 수동 개입 (권장하지 않음)**
```typescript
// 디버그 모드로 실행하여 수동으로 CAPTCHA 입력
// playwright.config.ts
export default defineConfig({
  use: {
    headless: false, // 브라우저 표시
  },
});
```

---

### 5. 세션/쿠키 문제

#### 증상
- 로그인 후에도 인증되지 않은 상태
- 페이지 이동 시 로그인 상태 유실

#### 해결책

1. **쿠키 도메인 확인**: BASE_URL과 실제 사이트 도메인 일치 확인

2. **storageState 사용** (세션 재사용):
   ```typescript
   // global-setup.ts
   import { chromium } from '@playwright/test';
   import { GnuboardAuth } from './gnuboard-auth';

   async function globalSetup() {
     const browser = await chromium.launch();
     const page = await browser.newPage();
     
     const auth = new GnuboardAuth(page);
     await auth.ensureLoggedIn();
     
     // 인증 상태 저장
     await page.context().storageState({ path: './auth.json' });
     await browser.close();
   }

   export default globalSetup;
   ```

   ```typescript
   // playwright.config.ts
   export default defineConfig({
     globalSetup: require.resolve('./global-setup.ts'),
     use: {
       storageState: './auth.json',
     },
   });
   ```

---

### 6. HTTPS/SSL 인증서 오류

#### 증상
```
Error: net::ERR_CERT_AUTHORITY_INVALID
```

#### 해결책
```typescript
// playwright.config.ts
export default defineConfig({
  use: {
    ignoreHTTPSErrors: true,
  },
});
```

---

### 7. 네트워크 오류

#### 증상
```
Error: net::ERR_CONNECTION_REFUSED
```

#### 해결책
1. BASE_URL이 올바른지 확인
2. 서버가 실행 중인지 확인
3. 방화벽/보안 그룹 설정 확인
4. VPN 연결 필요 여부 확인

---

## 디버깅 팁

### 1. 스크린샷 캡처
```typescript
test('debug test', async ({ page }) => {
  const auth = new GnuboardAuth(page);
  
  try {
    await auth.ensureLoggedIn();
  } catch (e) {
    await page.screenshot({ path: 'debug-screenshot.png', fullPage: true });
    throw e;
  }
});
```

### 2. 브라우저 표시 모드
```bash
npx playwright test --headed
```

### 3. 디버그 모드
```bash
npx playwright test --debug
```

### 4. 특정 테스트만 실행
```bash
npx playwright test tests/example.spec.ts
```

### 5. 콘솔 로그 확인
```typescript
page.on('console', msg => console.log('PAGE LOG:', msg.text()));
```

---

## 자주 묻는 질문

### Q: 여러 계정으로 테스트하려면?

A: `.env`에 추가 계정 설정 후 테스트에서 지정:
```typescript
await auth.ensureLoggedIn(process.env.USER2_ID, process.env.USER2_PW);
```

### Q: 로그인 상태를 테스트 간에 유지하려면?

A: `storageState`를 사용하여 세션 저장/복원 (위 "세션/쿠키 문제" 참조)

### Q: CI/CD 환경에서 테스트하려면?

A: GitHub Actions 예시:
```yaml
- name: Run Playwright tests
  env:
    BASE_URL: ${{ secrets.TEST_BASE_URL }}
    USER_ID: ${{ secrets.TEST_USER_ID }}
    USER_PW: ${{ secrets.TEST_USER_PW }}
  run: npx playwright test
```
