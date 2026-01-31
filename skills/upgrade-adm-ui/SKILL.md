---
name: upgrade-adm-ui
description: PHP 관리자 페이지 UI 스타일 업그레이드 에이전트. Figma 디자인 토큰 기반으로 adm_cw 관리자 페이지 스타일을 현대화합니다. admin.css 레이아웃 선택자는 유지하면서 CSS 오버라이드 파일로 스타일만 변경. 스타일 리팩토링, 디자인 시스템 적용, CSS 현대화 작업 시 사용.
---

# 관리자 UI 스타일 업그레이드

## 목적

`adm_cw/css/admin.css`의 **레이아웃 선택자를 유지**하면서 Figma 디자인 시스템 기반으로 스타일을 현대화합니다.

## 핵심 원칙

1. **admin.css 레이아웃 선택자 변경 금지**
2. **CSS 오버라이드 파일로만 스타일 적용**
3. **Figma 디자인 토큰 정확히 사용**

## 작업 워크플로우

```
Task Progress:
- [ ] Step 1: 대상 PHP 파일 확인
- [ ] Step 2: 기존 CSS 클래스 매핑
- [ ] Step 3: 오버라이드 CSS 생성/수정
- [ ] Step 4: PHP 파일에 CSS 링크 추가
- [ ] Step 5: 결과 검증
```

### Step 1: 대상 PHP 파일 확인

대상 파일을 읽고 사용 중인 CSS 클래스를 파악합니다.

### Step 2: 기존 CSS 클래스 매핑

`admin.css`에 정의된 레이아웃 선택자와 대상 파일의 클래스를 매핑합니다.

**유지해야 할 레이아웃 선택자** (참조: [css-selectors.md](css-selectors.md)):
- `#hd_top`, `#gnb`, `#container`, `#container_wr`, `#ft`
- `.pg_wrap`, `.pg`, `.pg_page`, `.pg_current`

### Step 3: 오버라이드 CSS 생성/수정

별도 CSS 파일에 스타일 오버라이드를 작성합니다.
디자인 토큰은 [design-tokens.md](design-tokens.md) 참조.

**파일 위치**: `adm_cw/css/` 디렉토리 내

### Step 4: PHP 파일에 CSS 링크 추가

`admin.head.php`에 오버라이드 CSS를 추가하거나, 개별 PHP 파일에 직접 추가합니다.

```php
<link rel="stylesheet" href="<?php echo G5_ADMIN_URL ?>/css/cwnu-admin-override.css">
```

### Step 5: 결과 검증

Playwright MCP로 페이지를 열어 스타일 적용을 확인합니다.

## 스타일 적용 규칙

### 버튼

```css
/* Primary 버튼 */
.btn.btn_01, .btn_submit {
    background: #003179;
    color: white;
    border: 1px solid #003179;
    border-radius: 1000px;
    padding: 8px 16px;
    font-family: 'Pretendard', sans-serif;
    font-weight: 800;
    font-size: 16px;
    line-height: 1.5;
}

/* Secondary 버튼 */
.btn.btn_02 {
    background: white;
    color: #003179;
    border: 1px solid #003179;
    border-radius: 1000px;
    padding: 8px 16px;
}

/* 작은 버튼 */
.btn.btn_03 {
    padding: 6px 12px;
    font-size: 14px;
}
```

### 테이블

```css
/* 테이블 컨테이너 */
.tbl_head01, .tbl_wrap {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* 테이블 헤더 */
.tbl_head01 thead th {
    background: #f1f3f7;
    color: #003179;
    font-weight: 800;
    padding: 16px 12px;
    border-bottom: 1px solid #e0e0e0;
}

/* 테이블 셀 */
.tbl_head01 tbody td {
    padding: 14px 12px;
    border-bottom: 1px solid #f9f9f9;
    font-size: 14px;
    line-height: 1.5;
}
```

### 검색 폼

```css
/* 검색 폼 컨테이너 */
.local_sch01, .local_sch {
    background: #f1f3f7;
    padding: 24px;
    border-radius: 12px;
    margin-bottom: 20px;
}

/* Select */
.local_sch select {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 14px;
    min-width: 120px;
}

/* Text Input */
.local_sch input[type="text"],
.frm_input {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 14px;
}
```

### 페이지네이션

```css
.pg_wrap {
    text-align: center;
    padding: 20px 0;
}

.pg_page {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 32px;
    height: 32px;
    padding: 0 12px;
    font-weight: 800;
    font-size: 16px;
    color: black;
}

.pg_current {
    background: #003179;
    color: white;
    border-radius: 4px;
    min-width: 32px;
    height: 32px;
}
```

### 섹션 타이틀

```css
/* 섹션 제목 (h2) */
#container_wr h2 {
    font-family: 'Paperlogy', sans-serif;
    font-weight: 800;
    font-size: 24px;
    line-height: 1.5;
    color: #003179;
    margin-bottom: 16px;
}
```

### 폼 테이블

```css
/* 폼 테이블 헤더 */
.tbl_frm01 th {
    background: #f1f3f7;
    color: #003179;
    font-weight: 800;
    padding: 14px 16px;
    text-align: left;
    border-bottom: 1px solid #e0e0e0;
}

/* 폼 테이블 셀 */
.tbl_frm01 td {
    padding: 14px 16px;
    border-bottom: 1px solid #f9f9f9;
}

/* Radio/Checkbox 그룹 */
.tbl_frm01 input[type="radio"],
.tbl_frm01 input[type="checkbox"] {
    margin-right: 6px;
    accent-color: #003179;
}
```

## 추가 리소스

- [design-tokens.md](design-tokens.md) - 디자인 토큰 상세
- [css-selectors.md](css-selectors.md) - admin.css 선택자 참조
- [component-examples.md](component-examples.md) - 컴포넌트별 CSS 예제

## 주의사항

1. `admin.css`의 레이아웃 속성(`position`, `width`, `height`, `padding`, `margin` 등)은 오버라이드하지 않음
2. 색상, 폰트, border-radius, box-shadow 등 **시각적 스타일만** 오버라이드
3. 기존 클래스 구조를 활용하여 선택자 작성
4. `!important` 사용 최소화 (필요시에만)
