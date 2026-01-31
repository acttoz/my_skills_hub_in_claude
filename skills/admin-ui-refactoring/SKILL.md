---
name: admin-ui-refactoring
description: 관리자 페이지 UI 디자인 리팩토링 전문 에이전트. Figma 디자인 시스템을 기반으로 adm_cw 관리자 페이지의 스타일을 현대화합니다. CSS 충돌 방지와 기존 HTML 구조 유지에 중점. 스타일 리팩토링, CSS 오버라이드, 디자인 시스템 적용 작업 시 사용하세요.
---

# Admin UI Refactoring Agent

관리자 페이지(adm_cw) UI를 Figma 디자인 시스템에 맞춰 리팩토링하는 전문 에이전트입니다.

## Quick Start

1. 기존 CSS 구조 분석 → `adm_cw/css/admin.css` 읽기
2. Figma 디자인 컨텍스트 가져오기
3. CSS 오버라이드 파일 생성/수정
4. 기존 HTML 구조 유지하며 클래스 추가

## Design System

### Color Palette

```css
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
  
  /* Gradients */
  --cwnu-gradient-blue-black: linear-gradient(180deg, #0046ac 0%, #000000 100%);
}
```

### Typography

```css
/* Heading - Paperlogy */
--cwnu-font-heading: 'Paperlogy', sans-serif;

/* Body - Pretendard */
--cwnu-font-body: 'Pretendard', sans-serif;

/* Sizes */
--cwnu-text-h1: 64px;    /* line-height: 1.3 */
--cwnu-text-h2: 48px;    /* line-height: 1.3 */
--cwnu-text-h3: 32px;    /* line-height: 1.5 */
--cwnu-text-h4: 28px;    /* line-height: 1.5 */
--cwnu-text-h5: 24px;    /* line-height: 1.5 */
--cwnu-text-xl: 28px;    /* line-height: 1.5 */
--cwnu-text-lg: 20px;    /* line-height: 1.8 */
--cwnu-text-md: 16px;    /* line-height: 1.8 */
--cwnu-text-sm: 14px;    /* line-height: 1.5 */
```

## CSS Collision Prevention Strategy

### 1. Namespace Prefix

모든 새로운 클래스는 `cwnu-` 접두사를 사용합니다:

```css
/* Good */
.cwnu-btn-primary { ... }
.cwnu-table { ... }

/* Bad - 기존 클래스와 충돌 가능 */
.btn-primary { ... }
.table { ... }
```

### 2. Scoped Overrides

기존 selector를 오버라이드할 때는 더 높은 specificity를 사용합니다:

```css
/* 기존 admin.css의 스타일 오버라이드 */
body.cwnu-admin-theme .tbl_head01 thead th {
  background: var(--cwnu-primary-1);
  color: var(--cwnu-white);
}

/* 특정 페이지만 오버라이드 */
.cwnu-page-member .tbl_frm01 th {
  background: var(--cwnu-gray-100);
}
```

### 3. CSS Layer 활용 (선택적)

```css
@layer base, admin-override, cwnu-design;

@layer cwnu-design {
  .cwnu-btn { ... }
}
```

### 4. 기존 Element Selector 재사용

admin.css의 기존 selector를 분석하여 동일한 구조로 오버라이드합니다:

```css
/* admin.css 기존 구조 유지 */
#container { ... }
#container_wr { ... }
.tbl_head01 { ... }
.tbl_frm01 { ... }
.btn_submit { ... }
.frm_input { ... }
```

## Override Rules for Existing Elements

### Tables

```css
/* 기존 .tbl_head01 오버라이드 */
body.cwnu-admin-theme .tbl_head01 thead th {
  background: var(--cwnu-primary-1);
  color: var(--cwnu-white);
  border: 1px solid var(--cwnu-primary-2);
  font-family: var(--cwnu-font-body);
  font-weight: 800;
  font-size: 14px;
  padding: 12px 10px;
}

body.cwnu-admin-theme .tbl_head01 tbody td {
  border: 1px solid var(--cwnu-gray-200);
  padding: 10px;
  font-family: var(--cwnu-font-body);
  font-size: 14px;
}

body.cwnu-admin-theme .tbl_head01 tbody tr:hover {
  background: var(--cwnu-primary-bg);
}
```

### Buttons

```css
/* 기존 버튼 오버라이드 */
body.cwnu-admin-theme .btn_submit,
body.cwnu-admin-theme .btn_01 {
  background: var(--cwnu-primary-1);
  color: var(--cwnu-white);
  font-family: var(--cwnu-font-body);
  font-weight: 800;
  border: none;
  border-radius: 4px;
  transition: background 0.3s ease;
}

body.cwnu-admin-theme .btn_submit:hover,
body.cwnu-admin-theme .btn_01:hover {
  background: var(--cwnu-primary-2);
}

body.cwnu-admin-theme .btn_02 {
  background: var(--cwnu-white);
  color: var(--cwnu-primary-1);
  border: 2px solid var(--cwnu-primary-1);
}
```

### Forms

```css
/* 기존 폼 요소 오버라이드 */
body.cwnu-admin-theme .frm_input,
body.cwnu-admin-theme select,
body.cwnu-admin-theme textarea {
  border: 1px solid var(--cwnu-gray-200);
  border-radius: 4px;
  font-family: var(--cwnu-font-body);
  font-size: 14px;
  transition: border-color 0.3s ease;
}

body.cwnu-admin-theme .frm_input:focus,
body.cwnu-admin-theme select:focus,
body.cwnu-admin-theme textarea:focus {
  border-color: var(--cwnu-primary-1);
  outline: none;
  box-shadow: 0 0 0 3px rgba(0, 49, 121, 0.1);
}

body.cwnu-admin-theme .tbl_frm01 th {
  background: var(--cwnu-gray-100);
  font-family: var(--cwnu-font-body);
  font-weight: 600;
  color: var(--cwnu-black);
}
```

## Implementation Workflow

### Step 1: CSS 변수 파일 생성

`adm_cw/css/cwnu-design-system.css` 생성:

```css
@charset "UTF-8";

/* === CWNU Design System Variables === */
:root {
  /* Colors */
  --cwnu-primary-1: #003179;
  --cwnu-primary-2: #0046ac;
  --cwnu-primary-bg: #f1f3f7;
  --cwnu-gray-100: #f9f9f9;
  --cwnu-gray-200: #dddddd;
  --cwnu-gray-400: #f2f2f2;
  --cwnu-black: #000000;
  --cwnu-white: #ffffff;
  --cwnu-warning: #ff0004;
  
  /* Typography */
  --cwnu-font-heading: 'Paperlogy', sans-serif;
  --cwnu-font-body: 'Pretendard', sans-serif;
}

/* 폰트 로드 */
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
@import url('https://cdn.jsdelivr.net/gh/projectnoonnu/2410-1@1.1/Paperlogy.css');
```

### Step 2: 오버라이드 CSS 생성

`adm_cw/css/cwnu-admin-override.css` 생성:

```css
@charset "UTF-8";

/* === CWNU Admin Override Styles === */
/* 기존 admin.css 스타일을 오버라이드 */
/* body에 .cwnu-admin-theme 클래스 필요 */

/* [Override Rules Here] */
```

### Step 3: admin.head.php 수정

```php
<!-- CWNU Design System -->
<link rel="stylesheet" href="<?php echo G5_ADMIN_URL ?>/css/cwnu-design-system.css">
<link rel="stylesheet" href="<?php echo G5_ADMIN_URL ?>/css/cwnu-admin-override.css">
```

### Step 4: body 클래스 추가

```html
<body class="cwnu-admin-theme">
```

## Figma Integration

### Figma MCP 사용법

```javascript
// 1. 디자인 컨텍스트 가져오기
CallMcpTool({
  server: "user-Figma",
  toolName: "get_design_context",
  arguments: {
    fileKey: "JLcydBrlnKBsH3Z8SE96oM",
    nodeId: "773:9448",
    clientLanguages: "html,css,php"
  }
});

// 2. 스크린샷 가져오기
CallMcpTool({
  server: "user-Figma",
  toolName: "get_screenshot",
  arguments: {
    fileKey: "JLcydBrlnKBsH3Z8SE96oM",
    nodeId: "773:9448"
  }
});
```

### Figma URL 파싱

```
URL: https://www.figma.com/design/{fileKey}/{fileName}?node-id={nodeId}

예시:
https://www.figma.com/design/JLcydBrlnKBsH3Z8SE96oM/...?node-id=773-9448

→ fileKey: JLcydBrlnKBsH3Z8SE96oM
→ nodeId: 773:9448 (또는 773-9448)
```

## Checklist

작업 전 확인사항:

- [ ] `adm_cw/css/admin.css` 기존 selector 분석 완료
- [ ] Figma 디자인 컨텍스트 확인
- [ ] CSS 변수 파일 존재 확인
- [ ] body에 `.cwnu-admin-theme` 클래스 확인

작업 후 확인사항:

- [ ] 기존 HTML 구조 유지됨
- [ ] CSS specificity 충돌 없음
- [ ] 새 클래스는 `cwnu-` 접두사 사용
- [ ] 반응형 스타일 유지
- [ ] 브라우저 호환성 확인

## Reference Files

| File | Purpose |
|------|---------|
| `adm_cw/css/admin.css` | 기존 관리자 스타일 (분석용) |
| `adm_cw/css/cwnu-design-system.css` | 디자인 시스템 변수 |
| `adm_cw/css/cwnu-admin-override.css` | 오버라이드 스타일 |
| `adm_cw/admin.head.php` | CSS 로드 위치 |
| `.claude/agents/admin-style-improver.md` | 상세 디자인 사양 |

## Anti-Patterns

### 1. !important 남용 금지

```css
/* Bad */
.btn { background: red !important; }

/* Good - specificity로 해결 */
body.cwnu-admin-theme .btn { background: red; }
```

### 2. 전역 element selector 금지

```css
/* Bad - 모든 table에 영향 */
table { border-collapse: collapse; }

/* Good - scoped */
body.cwnu-admin-theme .tbl_head01 table { ... }
```

### 3. 인라인 스타일 금지

```html
<!-- Bad -->
<div style="background: #003179;">

<!-- Good -->
<div class="cwnu-bg-primary">
```
