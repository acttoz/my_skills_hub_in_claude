# CSS Override Examples

기존 admin.css 스타일을 오버라이드하는 실제 코드 예시입니다.

## Complete Override CSS Template

```css
@charset "UTF-8";
/**
 * CWNU Admin Override Styles
 * 
 * 이 파일은 기존 admin.css 스타일을 Figma 디자인 시스템에 맞게 오버라이드합니다.
 * body에 .cwnu-admin-theme 클래스가 있어야 적용됩니다.
 * 
 * 규칙:
 * 1. 기존 HTML 구조 변경 없음
 * 2. 새 클래스는 cwnu- 접두사 사용
 * 3. specificity는 body.cwnu-admin-theme로 확보
 */

/* ============================================
   1. CSS Variables (Design Tokens)
   ============================================ */
:root {
  /* Primary Colors */
  --cwnu-primary-1: #003179;
  --cwnu-primary-2: #0046ac;
  --cwnu-primary-bg: #f1f3f7;
  
  /* Grayscale */
  --cwnu-gray-100: #f9f9f9;
  --cwnu-gray-200: #dddddd;
  --cwnu-gray-400: #f2f2f2;
  --cwnu-black: #000000;
  --cwnu-white: #ffffff;
  
  /* Semantic */
  --cwnu-warning: #ff0004;
  
  /* Typography */
  --cwnu-font-heading: 'Paperlogy', sans-serif;
  --cwnu-font-body: 'Pretendard', sans-serif;
  
  /* Spacing */
  --cwnu-spacing-sm: 8px;
  --cwnu-spacing-md: 12px;
  --cwnu-spacing-lg: 16px;
  
  /* Border Radius */
  --cwnu-radius-sm: 4px;
  --cwnu-radius-md: 8px;
  
  /* Transitions */
  --cwnu-transition: 0.3s ease;
}

/* ============================================
   2. Base Typography Override
   ============================================ */
body.cwnu-admin-theme {
  font-family: var(--cwnu-font-body);
  color: var(--cwnu-black);
}

body.cwnu-admin-theme h1,
body.cwnu-admin-theme h2,
body.cwnu-admin-theme h3,
body.cwnu-admin-theme h4,
body.cwnu-admin-theme h5,
body.cwnu-admin-theme h6 {
  font-family: var(--cwnu-font-heading);
}

/* ============================================
   3. Header Override
   ============================================ */
body.cwnu-admin-theme #hd_top {
  background: var(--cwnu-primary-1);
}

body.cwnu-admin-theme #logo {
  background: var(--cwnu-primary-2);
}

body.cwnu-admin-theme #btn_gnb {
  background-color: var(--cwnu-primary-2);
}

body.cwnu-admin-theme #btn_gnb.btn_gnb_open {
  background-color: var(--cwnu-primary-2);
}

/* ============================================
   4. Table Overrides
   ============================================ */

/* 기본 테이블 헤더 */
body.cwnu-admin-theme .tbl_head01 thead th {
  background: var(--cwnu-primary-1);
  color: var(--cwnu-white);
  border: 1px solid var(--cwnu-primary-2);
  font-family: var(--cwnu-font-body);
  font-weight: 800;
  font-size: 14px;
  padding: 12px 10px;
}

body.cwnu-admin-theme .tbl_head01 thead th a {
  color: var(--cwnu-white);
}

/* 테이블 바디 */
body.cwnu-admin-theme .tbl_head01 tbody td {
  border: 1px solid var(--cwnu-gray-200);
  padding: 10px;
  font-family: var(--cwnu-font-body);
  font-size: 14px;
}

body.cwnu-admin-theme .tbl_head01 tbody tr:nth-child(even) {
  background: #eff3f9;
}

body.cwnu-admin-theme .tbl_head01 tbody tr:hover {
  background: var(--cwnu-primary-bg);
}

/* 폼 테이블 */
body.cwnu-admin-theme .tbl_frm01 th {
  background: var(--cwnu-gray-100);
  font-family: var(--cwnu-font-body);
  font-weight: 600;
  color: var(--cwnu-black);
  border-color: var(--cwnu-gray-200);
}

body.cwnu-admin-theme .tbl_frm01 td {
  border-color: var(--cwnu-gray-200);
  font-family: var(--cwnu-font-body);
}

/* ============================================
   5. Button Overrides
   ============================================ */

/* Primary 버튼 */
body.cwnu-admin-theme .btn_submit,
body.cwnu-admin-theme a.btn_submit,
body.cwnu-admin-theme .btn_01,
body.cwnu-admin-theme a.btn_01 {
  background: var(--cwnu-primary-1);
  color: var(--cwnu-white);
  font-family: var(--cwnu-font-body);
  font-weight: 800;
  border: none;
  border-radius: var(--cwnu-radius-sm);
  transition: background var(--cwnu-transition);
}

body.cwnu-admin-theme .btn_submit:hover,
body.cwnu-admin-theme a.btn_submit:hover,
body.cwnu-admin-theme .btn_01:hover,
body.cwnu-admin-theme a.btn_01:hover {
  background: var(--cwnu-primary-2);
}

/* Secondary 버튼 */
body.cwnu-admin-theme .btn_02,
body.cwnu-admin-theme a.btn_02 {
  background: var(--cwnu-white);
  color: var(--cwnu-primary-1);
  border: 2px solid var(--cwnu-primary-1);
  font-family: var(--cwnu-font-body);
  font-weight: 800;
  border-radius: var(--cwnu-radius-sm);
  transition: all var(--cwnu-transition);
}

body.cwnu-admin-theme .btn_02:hover,
body.cwnu-admin-theme a.btn_02:hover {
  background: var(--cwnu-primary-bg);
}

/* Tertiary 버튼 */
body.cwnu-admin-theme .btn_03,
body.cwnu-admin-theme a.btn_03 {
  background: var(--cwnu-primary-2);
  color: var(--cwnu-white);
  font-family: var(--cwnu-font-body);
  font-weight: 800;
  border-radius: var(--cwnu-radius-sm);
}

/* Warning 버튼 */
body.cwnu-admin-theme .btn-del,
body.cwnu-admin-theme button.btn-del {
  background: var(--cwnu-warning);
  color: var(--cwnu-white);
  font-family: var(--cwnu-font-body);
  font-weight: 800;
  border: none;
  border-radius: var(--cwnu-radius-sm);
  transition: background var(--cwnu-transition);
}

body.cwnu-admin-theme .btn-del:hover,
body.cwnu-admin-theme button.btn-del:hover {
  background: #cc0003;
}

/* 폼라인 버튼 */
body.cwnu-admin-theme .btn_frmline,
body.cwnu-admin-theme a.btn_frmline {
  background: var(--cwnu-primary-1);
  color: var(--cwnu-white);
  border: none;
  border-radius: var(--cwnu-radius-sm);
  font-family: var(--cwnu-font-body);
  font-weight: 600;
}

/* ============================================
   6. Form Overrides
   ============================================ */

/* Input */
body.cwnu-admin-theme .frm_input,
body.cwnu-admin-theme input[type="text"],
body.cwnu-admin-theme input[type="password"],
body.cwnu-admin-theme input[type="email"],
body.cwnu-admin-theme input[type="number"],
body.cwnu-admin-theme input[type="date"] {
  border: 1px solid var(--cwnu-gray-200);
  border-radius: var(--cwnu-radius-sm);
  font-family: var(--cwnu-font-body);
  font-size: 14px;
  transition: border-color var(--cwnu-transition), box-shadow var(--cwnu-transition);
}

body.cwnu-admin-theme .frm_input:focus,
body.cwnu-admin-theme input[type="text"]:focus,
body.cwnu-admin-theme input[type="password"]:focus,
body.cwnu-admin-theme input[type="email"]:focus,
body.cwnu-admin-theme input[type="number"]:focus,
body.cwnu-admin-theme input[type="date"]:focus {
  border-color: var(--cwnu-primary-1);
  outline: none;
  box-shadow: 0 0 0 3px rgba(0, 49, 121, 0.1);
}

/* Select */
body.cwnu-admin-theme select {
  border: 1px solid var(--cwnu-gray-200);
  border-radius: var(--cwnu-radius-sm);
  font-family: var(--cwnu-font-body);
  font-size: 14px;
  background: var(--cwnu-white);
  transition: border-color var(--cwnu-transition);
}

body.cwnu-admin-theme select:focus {
  border-color: var(--cwnu-primary-1);
  outline: none;
}

/* Textarea */
body.cwnu-admin-theme textarea {
  border: 1px solid var(--cwnu-gray-200);
  border-radius: var(--cwnu-radius-sm);
  font-family: var(--cwnu-font-body);
  font-size: 14px;
  transition: border-color var(--cwnu-transition);
}

body.cwnu-admin-theme textarea:focus {
  border-color: var(--cwnu-primary-1);
  outline: none;
  box-shadow: 0 0 0 3px rgba(0, 49, 121, 0.1);
}

/* ============================================
   7. Navigation Overrides
   ============================================ */

body.cwnu-admin-theme #gnb .gnb_oparea li a:hover,
body.cwnu-admin-theme #gnb .gnb_oparea li .on {
  color: var(--cwnu-primary-1);
}

body.cwnu-admin-theme .anchor .selected {
  background: var(--cwnu-primary-1);
}

/* ============================================
   8. Pagination Overrides
   ============================================ */

body.cwnu-admin-theme .pg_current {
  background: var(--cwnu-primary-1);
  color: var(--cwnu-white);
}

body.cwnu-admin-theme .pg a:focus,
body.cwnu-admin-theme .pg a:hover {
  background-color: var(--cwnu-primary-bg);
}

/* ============================================
   9. Search/Filter Area Overrides
   ============================================ */

body.cwnu-admin-theme .member_list_data {
  background: var(--cwnu-gray-100);
  border: 1px solid var(--cwnu-gray-200);
  border-radius: var(--cwnu-radius-md);
}

body.cwnu-admin-theme .btn_reset {
  background: var(--cwnu-primary-1);
  color: var(--cwnu-white);
  font-family: var(--cwnu-font-body);
  font-weight: 600;
  border-radius: var(--cwnu-radius-md);
  transition: background var(--cwnu-transition);
}

body.cwnu-admin-theme .btn_reset:hover {
  background: var(--cwnu-primary-2);
}

/* ============================================
   10. Popup/Modal Overrides
   ============================================ */

body.cwnu-admin-theme .popup-content {
  border-radius: var(--cwnu-radius-md);
}

body.cwnu-admin-theme .popup-header {
  border-bottom: 1px solid var(--cwnu-gray-200);
}

body.cwnu-admin-theme .popup-title {
  font-family: var(--cwnu-font-heading);
  font-weight: 700;
  color: var(--cwnu-primary-1);
}

body.cwnu-admin-theme .popup-footer button {
  background: var(--cwnu-primary-1);
  border-color: var(--cwnu-primary-1);
  font-family: var(--cwnu-font-body);
  font-weight: 600;
  border-radius: var(--cwnu-radius-sm);
}

body.cwnu-admin-theme .popup-footer button:hover {
  background: var(--cwnu-primary-2);
  border-color: var(--cwnu-primary-2);
}

/* ============================================
   11. Status/Badge Overrides
   ============================================ */

body.cwnu-admin-theme .color_st01 {
  background: var(--cwnu-warning);
}

body.cwnu-admin-theme .color_st02 {
  background: #28a745;
}

body.cwnu-admin-theme .color_st05 {
  background: var(--cwnu-primary-1);
}

/* ============================================
   12. Description/Info Box Overrides
   ============================================ */

body.cwnu-admin-theme .local_desc01 {
  background: var(--cwnu-gray-100);
  border-color: var(--cwnu-gray-200);
  border-radius: var(--cwnu-radius-sm);
}

body.cwnu-admin-theme .local_desc01 strong {
  color: var(--cwnu-warning);
}

/* ============================================
   13. New Utility Classes (cwnu- prefix)
   ============================================ */

/* Colors */
.cwnu-text-primary { color: var(--cwnu-primary-1); }
.cwnu-text-secondary { color: var(--cwnu-primary-2); }
.cwnu-text-warning { color: var(--cwnu-warning); }
.cwnu-text-white { color: var(--cwnu-white); }
.cwnu-text-black { color: var(--cwnu-black); }

.cwnu-bg-primary { background-color: var(--cwnu-primary-1); }
.cwnu-bg-secondary { background-color: var(--cwnu-primary-2); }
.cwnu-bg-light { background-color: var(--cwnu-primary-bg); }
.cwnu-bg-white { background-color: var(--cwnu-white); }

/* Typography */
.cwnu-font-heading { font-family: var(--cwnu-font-heading); }
.cwnu-font-body { font-family: var(--cwnu-font-body); }
.cwnu-font-bold { font-weight: 800; }
.cwnu-font-medium { font-weight: 500; }
.cwnu-font-regular { font-weight: 400; }

/* Borders */
.cwnu-border { border: 1px solid var(--cwnu-gray-200); }
.cwnu-border-primary { border: 1px solid var(--cwnu-primary-1); }
.cwnu-rounded { border-radius: var(--cwnu-radius-sm); }
.cwnu-rounded-md { border-radius: var(--cwnu-radius-md); }

/* Shadows */
.cwnu-shadow { box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }
.cwnu-shadow-lg { box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15); }
```

## Minimal Override (Quick Start)

가장 빠르게 적용할 수 있는 최소한의 오버라이드입니다:

```css
/* CWNU Quick Override */
:root {
  --cwnu-primary: #003179;
  --cwnu-primary-light: #0046ac;
  --cwnu-bg: #f1f3f7;
  --cwnu-gray: #dddddd;
}

body.cwnu-admin-theme .tbl_head01 thead th {
  background: var(--cwnu-primary);
  color: #fff;
  border-color: var(--cwnu-primary-light);
}

body.cwnu-admin-theme .btn_submit,
body.cwnu-admin-theme .btn_01 {
  background: var(--cwnu-primary);
  border-radius: 4px;
}

body.cwnu-admin-theme .btn_submit:hover,
body.cwnu-admin-theme .btn_01:hover {
  background: var(--cwnu-primary-light);
}

body.cwnu-admin-theme .frm_input:focus,
body.cwnu-admin-theme select:focus {
  border-color: var(--cwnu-primary);
  box-shadow: 0 0 0 3px rgba(0, 49, 121, 0.1);
}

body.cwnu-admin-theme .pg_current {
  background: var(--cwnu-primary);
}
```

## Page-Specific Override Example

특정 페이지만 다르게 스타일링할 때:

```css
/* 회원 목록 페이지 전용 스타일 */
body.cwnu-admin-theme.cwnu-page-member-list .tbl_head01 {
  /* 특정 스타일 */
}

/* 회원 폼 페이지 전용 스타일 */
body.cwnu-admin-theme.cwnu-page-member-form .tbl_frm01 th {
  width: 180px;
}
```

PHP에서 페이지 클래스 추가:

```php
<?php
$page_class = 'cwnu-page-' . basename($_SERVER['PHP_SELF'], '.php');
?>
<body class="cwnu-admin-theme <?php echo $page_class; ?>">
```
