import { Page, expect } from '@playwright/test';

/**
 * Gnuboard5 자동 로그인을 담당하는 클래스입니다.
 * .env 파일의 process.env 값을 직접 참조합니다.
 * 
 * 사용법:
 * ```typescript
 * import { GnuboardAuth } from './gnuboard-auth';
 * 
 * test('my test', async ({ page }) => {
 *   const auth = new GnuboardAuth(page);
 *   await auth.ensureLoggedIn();
 *   // 이제 로그인된 상태에서 테스트 진행
 * });
 * ```
 */
export class GnuboardAuth {
  protected page: Page;
  protected baseUrl: string;

  constructor(page: Page, baseUrl?: string) {
    this.page = page;
    // 인자로 전달된 URL이 없으면 .env의 BASE_URL을 사용합니다.
    this.baseUrl = baseUrl || process.env.BASE_URL || '';
  }

  /**
   * 로그인 상태를 확인하고, 비로그인 시 로그인을 수행합니다.
   * @param userId 로그인 아이디 (기본값: .env의 USER_ID)
   * @param userPw 로그인 비밀번호 (기본값: .env의 USER_PW)
   */
  async ensureLoggedIn(
    userId: string = process.env.USER_ID || '',
    userPw: string = process.env.USER_PW || ''
  ) {
    // 1. 필수 설정값 검증
    if (!this.baseUrl) {
      throw new Error(
        '.env 파일에 BASE_URL이 설정되어 있지 않습니다.\n' +
        '프로젝트 루트에 .env 파일을 생성하고 BASE_URL을 설정하세요.\n' +
        '예: BASE_URL=https://your-gnuboard-site.com'
      );
    }

    // 2. 현재 사이트 접속 및 로그인 여부 확인
    await this.page.goto(this.baseUrl);
    const loggedIn = await this.isLoggedIn();

    if (loggedIn) {
      console.log('이미 로그인되어 있습니다. 테스트를 진행합니다.');
      return;
    }

    // 3. 계정 정보 확인
    if (!userId || !userPw) {
      throw new Error(
        '.env 파일에 USER_ID 또는 USER_PW가 설정되어 있지 않습니다.\n' +
        '프로젝트 루트의 .env 파일에 다음 값을 설정하세요:\n' +
        'USER_ID=your_test_account_id\n' +
        'USER_PW=your_test_account_password'
      );
    }

    // 4. 로그인 수행
    console.log(`비로그인 상태 확인: [${userId}] 계정으로 로그인을 시도합니다.`);
    await this.performLogin(userId, userPw);

    // 5. 로그인 결과 검증 (로그아웃 링크 대기)
    await expect(this.page.locator('a[href*="logout.php"]')).toBeVisible({ timeout: 10000 });
    console.log('로그인 성공. 테스트 환경이 준비되었습니다.');
  }

  /**
   * 화면 내 로그아웃 링크(logout.php) 유무로 로그인 상태를 판별합니다.
   */
  protected async isLoggedIn(): Promise<boolean> {
    const logoutLink = this.page.locator('a[href*="logout.php"]');
    try {
      // 그누보드 응답 시간을 고려하여 최대 3초간 확인
      await logoutLink.waitFor({ state: 'visible', timeout: 3000 });
      return true;
    } catch {
      return false;
    }
  }

  /**
   * 실제 로그인 폼 입력 및 전송 로직
   * 커스텀 테마 사용 시 이 메서드를 오버라이드하세요.
   */
  protected async performLogin(userId: string, userPw: string) {
    const loginUrl = this.baseUrl.endsWith('/') 
      ? `${this.baseUrl}bbs/login.php` 
      : `${this.baseUrl}/bbs/login.php`;

    await this.page.goto(loginUrl);

    // 그누보드 표준 필드: mb_id, mb_password
    await this.page.fill('input[name="mb_id"]', userId);
    await this.page.fill('input[name="mb_password"]', userPw);

    // 로그인 버튼 클릭 (Submit)
    await this.page.click('button[type="submit"], input[type="submit"]');

    // 리다이렉션 완료 후 네트워크 안정화 대기
    await this.page.waitForLoadState('networkidle');
  }

  /**
   * 로그아웃을 수행합니다.
   */
  async logout() {
    const logoutLink = this.page.locator('a[href*="logout.php"]');
    
    if (await logoutLink.isVisible()) {
      await logoutLink.click();
      await this.page.waitForLoadState('networkidle');
      console.log('로그아웃 완료.');
    } else {
      console.log('이미 로그아웃 상태입니다.');
    }
  }

  /**
   * 현재 로그인 상태를 반환합니다.
   */
  async checkLoginStatus(): Promise<boolean> {
    return await this.isLoggedIn();
  }
}
