# 컴포넌트별 CSS 예제

## 완전한 오버라이드 CSS 예제

아래는 `cwnu-admin-override.css`의 전체 예제입니다.

```css
@charset "utf-8";

/* ========================================
   CSS Custom Properties (Design Tokens)
   ======================================== */
:root {
    /* Colors */
    --cwnu-primary-01: #003179;
    --cwnu-primary-02: #0046AC;
    --cwnu-primary-03: #005ADF;
    --cwnu-black: #000000;
    --cwnu-white: #FFFFFF;
    --cwnu-gray-100: #f9f9f9;
    --cwnu-gray-200: #e0e0e0;
    --cwnu-primary-bg: #f1f3f7;
    
    /* Typography */
    --cwnu-font-heading: 'Paperlogy', sans-serif;
    --cwnu-font-body: 'Pretendard', sans-serif;
    
    /* Spacing */
    --cwnu-spacing-xs: 4px;
    --cwnu-spacing-sm: 8px;
    --cwnu-spacing-md: 12px;
    --cwnu-spacing-lg: 16px;
    --cwnu-spacing-xl: 20px;
    --cwnu-spacing-2xl: 24px;
    --cwnu-spacing-3xl: 32px;
    
    /* Border Radius */
    --cwnu-radius-sm: 4px;
    --cwnu-radius-md: 8px;
    --cwnu-radius-lg: 12px;
    --cwnu-radius-xl: 20px;
    --cwnu-radius-full: 1000px;
    
    /* Shadows */
    --cwnu-shadow-card: 0 4px 10px rgba(0, 0, 0, 0.1);
    --cwnu-shadow-sm: 0 4px 4px rgba(0, 0, 0, 0.05);
}

/* ========================================
   기본 타이포그래피
   ======================================== */
body {
    font-family: var(--cwnu-font-body);
}

/* ========================================
   통계 영역 (.local_ov)
   ======================================== */
.local_ov01,
.local_ov {
    display: flex;
    align-items: center;
    gap: var(--cwnu-spacing-md);
    margin-bottom: var(--cwnu-spacing-xl);
}

.ov_listall {
    background: var(--cwnu-primary-01);
    color: var(--cwnu-white);
    padding: var(--cwnu-spacing-sm) var(--cwnu-spacing-lg);
    border-radius: var(--cwnu-radius-full);
    font-weight: 800;
    font-size: 14px;
    text-decoration: none;
}

.btn_ov01 {
    background: var(--cwnu-white);
    border: 1px solid var(--cwnu-gray-200);
    padding: var(--cwnu-spacing-sm) var(--cwnu-spacing-lg);
    border-radius: var(--cwnu-radius-full);
    font-size: 14px;
    text-decoration: none;
    color: var(--cwnu-black);
}

.btn_ov01:hover {
    border-color: var(--cwnu-primary-01);
}

.ov_num {
    color: var(--cwnu-primary-01);
    font-weight: 800;
}

/* ========================================
   검색 폼 (.local_sch)
   ======================================== */
.local_sch01,
.local_sch {
    background: var(--cwnu-primary-bg);
    padding: var(--cwnu-spacing-2xl);
    border-radius: var(--cwnu-radius-lg);
    margin-bottom: var(--cwnu-spacing-xl);
    display: flex;
    align-items: center;
    gap: var(--cwnu-spacing-md);
    flex-wrap: wrap;
}

.local_sch select {
    border: 1px solid var(--cwnu-gray-200);
    border-radius: var(--cwnu-radius-md);
    padding: 10px var(--cwnu-spacing-lg);
    font-size: 14px;
    font-family: var(--cwnu-font-body);
    min-width: 120px;
    background: var(--cwnu-white);
}

.local_sch select:focus {
    outline: none;
    border-color: var(--cwnu-primary-01);
}

.local_sch input[type="text"],
.frm_input {
    border: 1px solid var(--cwnu-gray-200);
    border-radius: var(--cwnu-radius-md);
    padding: 10px var(--cwnu-spacing-lg);
    font-size: 14px;
    font-family: var(--cwnu-font-body);
    min-width: 200px;
}

.local_sch input[type="text"]:focus,
.frm_input:focus {
    outline: none;
    border-color: var(--cwnu-primary-01);
}

.btn_submit {
    background: var(--cwnu-primary-01);
    color: var(--cwnu-white);
    border: 1px solid var(--cwnu-primary-01);
    border-radius: var(--cwnu-radius-full);
    padding: var(--cwnu-spacing-sm) var(--cwnu-spacing-lg);
    font-family: var(--cwnu-font-body);
    font-weight: 800;
    font-size: 14px;
    cursor: pointer;
    transition: background 0.2s;
}

.btn_submit:hover {
    background: var(--cwnu-primary-02);
}

/* ========================================
   설명 영역 (.local_desc)
   ======================================== */
.local_desc01,
.local_desc {
    background: var(--cwnu-gray-100);
    padding: var(--cwnu-spacing-lg);
    border-radius: var(--cwnu-radius-md);
    margin-bottom: var(--cwnu-spacing-xl);
    border-left: 4px solid var(--cwnu-primary-01);
}

.local_desc p {
    font-size: 14px;
    line-height: 1.5;
    color: #666;
}

/* ========================================
   테이블 (.tbl_head01)
   ======================================== */
.tbl_head01,
.tbl_wrap {
    background: var(--cwnu-white);
    border-radius: var(--cwnu-radius-lg);
    box-shadow: var(--cwnu-shadow-card);
    overflow: hidden;
    margin-bottom: var(--cwnu-spacing-xl);
}

.tbl_head01 table {
    width: 100%;
    border-collapse: collapse;
}

.tbl_head01 caption {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
}

.tbl_head01 thead th {
    background: var(--cwnu-primary-bg);
    color: var(--cwnu-primary-01);
    font-weight: 800;
    font-size: 14px;
    padding: var(--cwnu-spacing-lg) var(--cwnu-spacing-md);
    text-align: center;
    border-bottom: 2px solid var(--cwnu-gray-200);
}

.tbl_head01 tbody tr {
    transition: background 0.2s;
}

.tbl_head01 tbody tr:hover {
    background: var(--cwnu-gray-100);
}

.tbl_head01 tbody td {
    padding: 14px var(--cwnu-spacing-md);
    text-align: center;
    border-bottom: 1px solid var(--cwnu-gray-100);
    font-size: 14px;
    line-height: 1.5;
}

/* 특정 셀 스타일 */
.tbl_head01 .td_chk {
    width: 40px;
}

.tbl_head01 .td_num {
    width: 60px;
    color: #666;
}

.tbl_head01 .td_mng {
    width: 80px;
}

.tbl_head01 .td_left {
    text-align: left;
}

.tbl_head01 .empty_table {
    padding: 40px;
    text-align: center;
    color: #999;
}

/* ========================================
   폼 테이블 (.tbl_frm01)
   ======================================== */
.tbl_frm01 {
    background: var(--cwnu-white);
    border-radius: var(--cwnu-radius-lg);
    box-shadow: var(--cwnu-shadow-card);
    overflow: hidden;
    margin-bottom: var(--cwnu-spacing-xl);
}

.tbl_frm01 table {
    width: 100%;
    border-collapse: collapse;
}

.tbl_frm01 th {
    background: var(--cwnu-primary-bg);
    color: var(--cwnu-primary-01);
    font-weight: 800;
    font-size: 14px;
    padding: 14px var(--cwnu-spacing-lg);
    text-align: left;
    width: 150px;
    border-bottom: 1px solid var(--cwnu-gray-200);
    vertical-align: middle;
}

.tbl_frm01 td {
    padding: 14px var(--cwnu-spacing-lg);
    border-bottom: 1px solid var(--cwnu-gray-100);
}

.tbl_frm01 input[type="text"],
.tbl_frm01 select {
    border: 1px solid var(--cwnu-gray-200);
    border-radius: var(--cwnu-radius-md);
    padding: 10px var(--cwnu-spacing-md);
    font-size: 14px;
    font-family: var(--cwnu-font-body);
}

.tbl_frm01 input[type="radio"],
.tbl_frm01 input[type="checkbox"] {
    margin-right: 6px;
    accent-color: var(--cwnu-primary-01);
}

/* ========================================
   버튼 (.btn)
   ======================================== */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-family: var(--cwnu-font-body);
    font-weight: 800;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.2s;
}

/* Primary Button */
.btn.btn_01 {
    background: var(--cwnu-primary-01);
    color: var(--cwnu-white);
    border: 1px solid var(--cwnu-primary-01);
    border-radius: var(--cwnu-radius-full);
    padding: var(--cwnu-spacing-sm) var(--cwnu-spacing-lg);
    font-size: 16px;
    line-height: 1.5;
}

.btn.btn_01:hover {
    background: var(--cwnu-primary-02);
    border-color: var(--cwnu-primary-02);
}

/* Secondary Button */
.btn.btn_02 {
    background: var(--cwnu-white);
    color: var(--cwnu-primary-01);
    border: 1px solid var(--cwnu-primary-01);
    border-radius: var(--cwnu-radius-full);
    padding: var(--cwnu-spacing-sm) var(--cwnu-spacing-lg);
    font-size: 16px;
    line-height: 1.5;
}

.btn.btn_02:hover {
    background: var(--cwnu-primary-bg);
}

/* Small Button */
.btn.btn_03 {
    background: var(--cwnu-white);
    color: var(--cwnu-primary-01);
    border: 1px solid var(--cwnu-primary-01);
    border-radius: var(--cwnu-radius-full);
    padding: 6px var(--cwnu-spacing-md);
    font-size: 14px;
    line-height: 1.5;
}

.btn.btn_03:hover {
    background: var(--cwnu-primary-01);
    color: var(--cwnu-white);
}

/* ========================================
   페이지네이션 (.pg_wrap)
   ======================================== */
.pg_wrap {
    padding: var(--cwnu-spacing-xl) 0;
}

.pg {
    display: inline-flex;
    align-items: center;
    gap: var(--cwnu-spacing-sm);
}

.pg_page {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 32px;
    height: 32px;
    padding: 0 var(--cwnu-spacing-md);
    font-weight: 800;
    font-size: 16px;
    color: var(--cwnu-black);
    text-decoration: none;
    border-radius: var(--cwnu-radius-sm);
    transition: all 0.2s;
}

.pg_page:hover {
    background: var(--cwnu-gray-100);
}

.pg_current {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 32px;
    height: 32px;
    padding: 0 var(--cwnu-spacing-md);
    background: var(--cwnu-primary-01);
    color: var(--cwnu-white);
    font-weight: 800;
    font-size: 16px;
    border-radius: var(--cwnu-radius-sm);
}

.pg_start,
.pg_prev,
.pg_next,
.pg_end {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: var(--cwnu-radius-sm);
    transition: background 0.2s;
}

.pg_start:hover,
.pg_prev:hover,
.pg_next:hover,
.pg_end:hover {
    background: var(--cwnu-gray-100);
}

/* ========================================
   섹션 제목
   ======================================== */
#container_wr h2 {
    font-family: var(--cwnu-font-heading);
    font-weight: 800;
    font-size: 24px;
    line-height: 1.5;
    color: var(--cwnu-primary-01);
    margin: 0 0 var(--cwnu-spacing-lg) 0;
    padding-bottom: var(--cwnu-spacing-md);
    border-bottom: 2px solid var(--cwnu-primary-01);
}

/* ========================================
   필터 영역 (라디오/체크박스 그룹)
   ======================================== */
.local_sch strong {
    font-weight: 800;
    color: var(--cwnu-primary-01);
    margin-right: var(--cwnu-spacing-sm);
}

.local_sch input[type="radio"],
.local_sch input[type="checkbox"] {
    margin-right: var(--cwnu-spacing-xs);
    accent-color: var(--cwnu-primary-01);
}

/* ========================================
   날짜 선택 버튼
   ======================================== */
.local_sch button {
    background: var(--cwnu-white);
    border: 1px solid var(--cwnu-gray-200);
    border-radius: var(--cwnu-radius-md);
    padding: var(--cwnu-spacing-sm) var(--cwnu-spacing-md);
    font-size: 14px;
    cursor: pointer;
    transition: all 0.2s;
}

.local_sch button:hover {
    border-color: var(--cwnu-primary-01);
    color: var(--cwnu-primary-01);
}

/* ========================================
   고정 버튼 영역
   ======================================== */
.btn_fixed_top {
    display: flex;
    gap: var(--cwnu-spacing-sm);
}

/* ========================================
   체크박스 스타일
   ======================================== */
input[type="checkbox"] {
    width: 18px;
    height: 18px;
    accent-color: var(--cwnu-primary-01);
}

/* ========================================
   링크 스타일
   ======================================== */
.tbl_head01 a {
    color: var(--cwnu-primary-01);
    text-decoration: none;
}

.tbl_head01 a:hover {
    text-decoration: underline;
}
```

## 폰트 로드

`admin.head.php`에 폰트를 추가합니다:

```html
<!-- Google Fonts - Pretendard -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">

<!-- Paperlogy (로컬 또는 CDN) -->
<style>
@font-face {
    font-family: 'Paperlogy';
    src: url('/fonts/Paperlogy-8ExtraBold.woff2') format('woff2');
    font-weight: 800;
    font-style: normal;
}
@font-face {
    font-family: 'Paperlogy';
    src: url('/fonts/Paperlogy-7Bold.woff2') format('woff2');
    font-weight: 700;
    font-style: normal;
}
@font-face {
    font-family: 'Paperlogy';
    src: url('/fonts/Paperlogy-3Light.woff2') format('woff2');
    font-weight: 300;
    font-style: normal;
}
</style>
```

## CSS 파일 로드 순서

`admin.head.php`에서:

```php
<!-- 기존 레이아웃 CSS -->
<link rel="stylesheet" href="<?php echo G5_ADMIN_URL ?>/css/admin.css">

<!-- 디자인 시스템 오버라이드 CSS (admin.css 뒤에 로드) -->
<link rel="stylesheet" href="<?php echo G5_ADMIN_URL ?>/css/cwnu-admin-override.css">
```
