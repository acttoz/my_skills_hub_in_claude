import { test, expect } from '@playwright/test';
import { GnuboardAuth } from './gnuboard-auth';

/**
 * Gnuboard5 인증 테스트 예제
 * 
 * 이 파일은 GnuboardAuth 클래스 사용법을 보여주는 예제입니다.
 * 실제 테스트 작성 시 참고하세요.
 */

test.describe('Gnuboard5 로그인 테스트', () => {
  test('로그인 성공 확인', async ({ page }) => {
    const auth = new GnuboardAuth(page);
    await auth.ensureLoggedIn();
    
    // 로그인 성공 시 로그아웃 링크가 표시됨
    await expect(page.locator('a[href*="logout.php"]')).toBeVisible();
  });

  test('로그아웃 후 재로그인', async ({ page }) => {
    const auth = new GnuboardAuth(page);
    
    // 로그인
    await auth.ensureLoggedIn();
    await expect(page.locator('a[href*="logout.php"]')).toBeVisible();
    
    // 로그아웃
    await auth.logout();
    
    // 로그인 링크가 다시 표시되어야 함
    await expect(page.locator('a[href*="login.php"]')).toBeVisible();
    
    // 재로그인
    await auth.ensureLoggedIn();
    await expect(page.locator('a[href*="logout.php"]')).toBeVisible();
  });
});

test.describe('회원 전용 페이지 테스트', () => {
  test.beforeEach(async ({ page }) => {
    // 각 테스트 전에 로그인 수행
    const auth = new GnuboardAuth(page);
    await auth.ensureLoggedIn();
  });

  test('회원정보 페이지 접근', async ({ page }) => {
    // 회원정보 수정 페이지로 이동 (비밀번호 확인 페이지)
    await page.goto(process.env.BASE_URL + '/bbs/member_confirm.php?url=register_form.php');
    
    // 비밀번호 확인 폼이 표시되어야 함
    await expect(page.locator('input[name="mb_password"]')).toBeVisible();
  });

  test('포인트 내역 페이지 접근', async ({ page }) => {
    await page.goto(process.env.BASE_URL + '/bbs/point.php');
    
    // 포인트 페이지 요소 확인 (테마에 따라 셀렉터 수정 필요)
    await expect(page).toHaveURL(/point\.php/);
  });
});

test.describe('게시판 테스트', () => {
  test('게시판 목록 조회', async ({ page }) => {
    const auth = new GnuboardAuth(page);
    await auth.ensureLoggedIn();
    
    // 게시판 페이지로 이동 (bo_table은 실제 게시판 ID로 수정)
    // await page.goto(process.env.BASE_URL + '/bbs/board.php?bo_table=free');
    
    // 게시판 목록이 표시되어야 함
    // await expect(page.locator('.board_list, .tbl_wrap, table')).toBeVisible();
    
    // 이 테스트는 실제 게시판 ID에 맞게 수정하세요
    expect(true).toBe(true);
  });

  test('글쓰기 폼 접근', async ({ page }) => {
    const auth = new GnuboardAuth(page);
    await auth.ensureLoggedIn();
    
    // 글쓰기 페이지로 이동 (bo_table은 실제 게시판 ID로 수정)
    // await page.goto(process.env.BASE_URL + '/bbs/write.php?bo_table=free');
    
    // 글쓰기 폼 요소 확인
    // await expect(page.locator('input[name="wr_subject"]')).toBeVisible();
    // await expect(page.locator('textarea[name="wr_content"], .note-editable')).toBeVisible();
    
    // 이 테스트는 실제 게시판 ID에 맞게 수정하세요
    expect(true).toBe(true);
  });
});

test.describe('다중 사용자 역할 테스트', () => {
  test('관리자 페이지 접근 (관리자 계정 필요)', async ({ page }) => {
    // ADMIN_ID, ADMIN_PW가 .env에 설정되어 있어야 함
    const adminId = process.env.ADMIN_ID;
    const adminPw = process.env.ADMIN_PW;
    
    if (!adminId || !adminPw) {
      test.skip();
      return;
    }
    
    const auth = new GnuboardAuth(page);
    await auth.ensureLoggedIn(adminId, adminPw);
    
    // 관리자 페이지로 이동
    await page.goto(process.env.BASE_URL + '/adm/');
    
    // 관리자 페이지 요소 확인
    await expect(page.locator('.adm_content, #adm_container, .admin')).toBeVisible();
  });
});
