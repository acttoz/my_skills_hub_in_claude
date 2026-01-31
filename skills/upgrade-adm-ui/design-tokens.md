# 디자인 토큰 (Figma 기반)

## 색상 (Colors)

### Primary

| 토큰명 | HEX | 용도 |
|--------|-----|------|
| `--color-primary-01` | `#003179` | 메인 브랜드 컬러, Primary 버튼, 강조 텍스트 |
| `--color-primary-02` | `#0046AC` | 그라디언트 중간, 호버 상태 |
| `--color-primary-03` | `#005ADF` | 그라디언트 끝, 라이트 강조 |

### Neutral

| 토큰명 | HEX | 용도 |
|--------|-----|------|
| `--color-black` | `#000000` | 본문 텍스트 |
| `--color-white` | `#FFFFFF` | 배경, 버튼 텍스트 |
| `--color-gray-100` | `#f9f9f9` | 테이블 행 구분선 |
| `--color-gray-200` | `#e0e0e0` | 입력 필드 보더 |

### Backgrounds

| 토큰명 | HEX | 용도 |
|--------|-----|------|
| `--color-primary-bg` | `#f1f3f7` | 검색 폼, 테이블 헤더, 카드 배경 |
| `--color-page-bg` | `#f3f3f3` | 페이지 배경 (기존 유지) |

### 그라디언트

```css
/* CTA 버튼 그라디언트 */
--gradient-primary: linear-gradient(90deg, #003179 0%, #0046AC 50%, #005ADF 100%);

/* 대각선 그라디언트 */
--gradient-diagonal: linear-gradient(125deg, #0046AC 0%, #0046AC 27%, #000000 100%);
```

## 타이포그래피 (Typography)

### 폰트 패밀리

```css
--font-heading: 'Paperlogy', sans-serif;
--font-body: 'Pretendard', sans-serif;
```

### 제목 스타일 (Paperlogy)

| 스타일명 | 크기 | 굵기 | Line Height |
|----------|------|------|-------------|
| H1 | 64px | 700 (Bold) | 1.3 |
| H2 | 48px | 700 (Bold) | 1.3 |
| H3 | 32px | 800 (ExtraBold) | 1.5 |
| H4 | 28px | 800 (ExtraBold) | 1.5 |
| H5 | 24px | 800 (ExtraBold) | 1.5 |
| H1 Light | 64px | 300 (Light) | 1.3 |
| H2 Light | 48px | 300 (Light) | 1.1 |
| H3 Light | 32px | 300 (Light) | 1.5 |
| H4 Light | 28px | 300 (Light) | 1.5 |
| H5 Light | 24px | 300 (Light) | 1.5 |

### 본문 스타일 (Pretendard)

| 스타일명 | 크기 | 굵기 | Line Height |
|----------|------|------|-------------|
| Extra Large Bold | 28px | 800 | 1.5 |
| Extra Bold | 24px | 800 | 1.8 |
| Large Bold | 20px | 800 | 1.8 |
| Medium Bold | 16px | 800 | 1.5 |
| Small Bold | 14px | 800 | 1.5 |
| Extra Large Regular | 24px | 400 | 1.8 |
| Large Regular | 20px | 400 | 1.8 |
| Medium Regular | 16px | 400 | 1.8 |
| Small Regular | 14px | 400 | 1.5 |

## 간격 (Spacing)

| 토큰명 | 값 | 용도 |
|--------|-----|------|
| `--spacing-xs` | 4px | 아이콘-텍스트 간격 |
| `--spacing-sm` | 8px | 요소 내부 간격 |
| `--spacing-md` | 12px | 버튼 그룹 간격 |
| `--spacing-lg` | 16px | 폼 필드 간격 |
| `--spacing-xl` | 20px | 섹션 내부 간격 |
| `--spacing-2xl` | 24px | 검색 폼 패딩 |
| `--spacing-3xl` | 32px | 카드 패딩 |
| `--spacing-4xl` | 40px | 섹션 간격 |

## Border Radius

| 토큰명 | 값 | 용도 |
|--------|-----|------|
| `--radius-sm` | 4px | 페이지네이션 숫자, 작은 요소 |
| `--radius-md` | 8px | 입력 필드, 작은 카드 |
| `--radius-lg` | 12px | 테이블 컨테이너, 버튼(CTA) |
| `--radius-xl` | 20px | 대형 카드 |
| `--radius-full` | 1000px | 필 버튼, 뱃지 |

## Box Shadow

```css
/* 카드/컨테이너 기본 그림자 */
--shadow-card: 0 4px 10px rgba(0, 0, 0, 0.1);

/* 카드/컨테이너 작은 그림자 */
--shadow-sm: 0 4px 4px rgba(0, 0, 0, 0.05);
```

## 컴포넌트별 토큰

### 버튼

```css
/* Primary Button (Pill) */
--btn-primary-bg: var(--color-primary-01);
--btn-primary-text: var(--color-white);
--btn-primary-border: 1px solid var(--color-primary-01);
--btn-primary-radius: var(--radius-full);
--btn-primary-padding: 8px 16px;
--btn-primary-font-size: 16px;
--btn-primary-font-weight: 800;

/* Secondary Button (Pill) */
--btn-secondary-bg: var(--color-white);
--btn-secondary-text: var(--color-primary-01);
--btn-secondary-border: 1px solid var(--color-primary-01);

/* CTA Button */
--btn-cta-bg: var(--gradient-primary);
--btn-cta-text: var(--color-white);
--btn-cta-radius: var(--radius-lg);
--btn-cta-padding: 20px 40px;
--btn-cta-font-size: 32px;
```

### 테이블

```css
/* Table Container */
--table-bg: var(--color-white);
--table-radius: var(--radius-lg);
--table-shadow: var(--shadow-card);

/* Table Header */
--table-header-bg: var(--color-primary-bg);
--table-header-text: var(--color-primary-01);
--table-header-font-weight: 800;
--table-header-padding: 16px 12px;

/* Table Cell */
--table-cell-padding: 14px 12px;
--table-cell-border: 1px solid var(--color-gray-100);
--table-cell-font-size: 14px;
```

### 입력 필드

```css
/* Input */
--input-border: 1px solid var(--color-gray-200);
--input-radius: var(--radius-md);
--input-padding: 10px 16px;
--input-font-size: 14px;

/* Select */
--select-border: var(--input-border);
--select-radius: var(--input-radius);
--select-padding: var(--input-padding);
```

### 페이지네이션

```css
/* Pagination Item */
--pg-item-width: 32px;
--pg-item-height: 32px;
--pg-item-font-size: 16px;
--pg-item-font-weight: 800;
--pg-item-color: var(--color-black);

/* Pagination Current */
--pg-current-bg: var(--color-primary-01);
--pg-current-text: var(--color-white);
--pg-current-radius: var(--radius-sm);
```

## CSS Custom Properties 정의

```css
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
    --cwnu-spacing-4xl: 40px;
    
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
```
