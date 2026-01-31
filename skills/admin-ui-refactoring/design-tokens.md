# CWNU Design Tokens Reference

Figma 디자인 시스템에서 추출한 디자인 토큰 상세 레퍼런스입니다.

## Color Tokens

### Primary Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `--cwnu-primary-1` | `#003179` | 주요 브랜드 컬러, 버튼 배경, 테이블 헤더 |
| `--cwnu-primary-2` | `#0046ac` | 보조 브랜드 컬러, hover 상태, 그라디언트 |
| `--cwnu-primary-bg` | `#f1f3f7` | 배경색, hover 배경 |

### Grayscale

| Token | Hex | Usage |
|-------|-----|-------|
| `--cwnu-gray-100` | `#f9f9f9` | 밝은 회색 배경, 폼 테이블 헤더 |
| `--cwnu-gray-200` | `#dddddd` | 중간 회색, 보더, 구분선 |
| `--cwnu-gray-400` | `#f2f2f2` | 비활성 배경 |
| `--cwnu-black` | `#000000` | 검정 텍스트 |
| `--cwnu-white` | `#ffffff` | 흰색 배경, 텍스트 |

### Semantic Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `--cwnu-warning` | `#ff0004` | 경고, 오류, 삭제 버튼 |
| `--cwnu-success` | `#28a745` | 성공 상태 (선택적) |
| `--cwnu-info` | `#17a2b8` | 정보 상태 (선택적) |

### Gradients

```css
--cwnu-gradient-blue-black: linear-gradient(180deg, #0046ac 0%, #000000 100%);
--cwnu-gradient-primary: linear-gradient(125.37deg, #0046ac 0%, #0046ac 26.92%, #000000 100%);
```

## Typography Tokens

### Font Families

```css
--cwnu-font-heading: 'Paperlogy', sans-serif;
--cwnu-font-body: 'Pretendard', sans-serif;
```

### Font Weights

| Token | Value | Usage |
|-------|-------|-------|
| `--cwnu-font-light` | `300` | Light heading |
| `--cwnu-font-regular` | `400` | Body text |
| `--cwnu-font-bold` | `700` | Bold heading |
| `--cwnu-font-extrabold` | `800` | Extra bold |

### Font Sizes

| Token | Size | Line Height | Usage |
|-------|------|-------------|-------|
| `--cwnu-text-h1` | `64px` | `1.3` | 페이지 제목 |
| `--cwnu-text-h2` | `48px` | `1.3` | 섹션 제목 |
| `--cwnu-text-h3` | `32px` | `1.5` | 서브섹션 제목 |
| `--cwnu-text-h4` | `28px` | `1.5` | 카드 제목 |
| `--cwnu-text-h5` | `24px` | `1.5` | 작은 제목 |
| `--cwnu-text-xl` | `28px` | `1.5` | 큰 본문 |
| `--cwnu-text-lg` | `20px` | `1.8` | 강조 텍스트 |
| `--cwnu-text-md` | `16px` | `1.8` | 기본 텍스트 |
| `--cwnu-text-sm` | `14px` | `1.5` | 작은 텍스트, 라벨 |

## Spacing Tokens

```css
--cwnu-spacing-xs: 4px;
--cwnu-spacing-sm: 8px;
--cwnu-spacing-md: 12px;
--cwnu-spacing-lg: 16px;
--cwnu-spacing-xl: 20px;
--cwnu-spacing-2xl: 24px;
--cwnu-spacing-3xl: 32px;
--cwnu-spacing-4xl: 40px;
```

## Border Radius

```css
--cwnu-radius-sm: 4px;
--cwnu-radius-md: 8px;
--cwnu-radius-lg: 12px;
--cwnu-radius-xl: 20px;
--cwnu-radius-full: 1000px;  /* pill shape */
```

## Shadows

```css
--cwnu-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--cwnu-shadow-md: 0 2px 8px rgba(0, 0, 0, 0.1);
--cwnu-shadow-lg: 0 4px 16px rgba(0, 0, 0, 0.15);
```

## Transitions

```css
--cwnu-transition-fast: 0.15s ease;
--cwnu-transition-normal: 0.3s ease;
--cwnu-transition-slow: 0.5s ease;
```

## Component Specific Tokens

### Buttons

```css
/* Primary Button */
--cwnu-btn-primary-bg: var(--cwnu-primary-1);
--cwnu-btn-primary-bg-hover: var(--cwnu-primary-2);
--cwnu-btn-primary-text: var(--cwnu-white);
--cwnu-btn-padding: 12px 24px;
--cwnu-btn-radius: var(--cwnu-radius-sm);

/* Secondary Button */
--cwnu-btn-secondary-bg: var(--cwnu-white);
--cwnu-btn-secondary-border: 2px solid var(--cwnu-primary-1);
--cwnu-btn-secondary-text: var(--cwnu-primary-1);

/* Warning Button */
--cwnu-btn-warning-bg: var(--cwnu-warning);
--cwnu-btn-warning-text: var(--cwnu-white);
```

### Tables

```css
/* Table Header */
--cwnu-table-header-bg: var(--cwnu-primary-1);
--cwnu-table-header-text: var(--cwnu-white);
--cwnu-table-header-border: var(--cwnu-primary-2);
--cwnu-table-header-padding: 12px 10px;

/* Table Body */
--cwnu-table-body-border: var(--cwnu-gray-200);
--cwnu-table-body-padding: 10px;
--cwnu-table-row-hover: var(--cwnu-primary-bg);
--cwnu-table-row-even: #eff3f9;
```

### Forms

```css
/* Input */
--cwnu-input-border: var(--cwnu-gray-200);
--cwnu-input-border-focus: var(--cwnu-primary-1);
--cwnu-input-radius: var(--cwnu-radius-sm);
--cwnu-input-padding: 10px 12px;
--cwnu-input-shadow-focus: 0 0 0 3px rgba(0, 49, 121, 0.1);

/* Form Label */
--cwnu-label-color: var(--cwnu-black);
--cwnu-label-font-weight: 600;
--cwnu-label-margin: 8px;
```

### Cards

```css
--cwnu-card-bg: var(--cwnu-white);
--cwnu-card-radius: var(--cwnu-radius-md);
--cwnu-card-shadow: var(--cwnu-shadow-md);
--cwnu-card-padding: 24px;
--cwnu-card-header-border: 2px solid var(--cwnu-primary-bg);
```

## Mapping to Existing admin.css Selectors

### Header/Navigation

| admin.css Selector | Override Target | Design Token |
|-------------------|-----------------|--------------|
| `#hd_top` | background | `--cwnu-primary-1` |
| `#logo` | background | `--cwnu-primary-2` |
| `#gnb .gnb_oparea li a:hover` | color | `--cwnu-primary-1` |

### Tables

| admin.css Selector | Override Target | Design Token |
|-------------------|-----------------|--------------|
| `.tbl_head01 thead th` | background | `--cwnu-primary-1` |
| `.tbl_head01 thead th` | border-color | `--cwnu-primary-2` |
| `.tbl_head01 tbody tr:nth-child(even)` | background | `--cwnu-table-row-even` |
| `.tbl_head01 tbody tr:hover` | background | `--cwnu-table-row-hover` |

### Buttons

| admin.css Selector | Override Target | Design Token |
|-------------------|-----------------|--------------|
| `.btn_submit` | background | `--cwnu-btn-primary-bg` |
| `.btn_01` | background | `--cwnu-btn-primary-bg` |
| `.btn_02` | background, border | `--cwnu-btn-secondary-*` |
| `.btn_03` | background | `--cwnu-primary-2` |

### Forms

| admin.css Selector | Override Target | Design Token |
|-------------------|-----------------|--------------|
| `.frm_input` | border | `--cwnu-input-border` |
| `.frm_input:focus` | border, shadow | `--cwnu-input-border-focus`, `--cwnu-input-shadow-focus` |
| `.tbl_frm01 th` | background | `--cwnu-gray-100` |

### Pagination

| admin.css Selector | Override Target | Design Token |
|-------------------|-----------------|--------------|
| `.pg_current` | background | `--cwnu-primary-1` |
| `.pg_page:hover` | background | `--cwnu-primary-bg` |
