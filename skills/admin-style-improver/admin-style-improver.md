# Admin Style Improver

국립창원대 발전기금 관리자 페이지의 UI/UX를 Figma 디자인 시스템에 맞춰 개선합니다.

## When to Use

이 스킬은 다음과 같은 경우에 사용합니다:
- 관리자 페이지 CSS 스타일 개선
- 디자인 시스템 적용
- 테이블, 버튼, 폼 등 UI 컴포넌트 현대화
- 회원관리, 기부/후원 관리 페이지 리팩토링

## Design System Specifications

### Color Palette

```css
/* Primary Colors */
--color-primary-1: #003179;      /* 주요 브랜드 컬러 (네이비) */
--color-primary-2: #0046ac;      /* 보조 브랜드 컬러 (블루) */
--color-primary-bg: #f1f3f7;     /* 배경색 */

/* Grayscale */
--color-gray-100: #f9f9f9;
--color-gray-200: #dddddd;
--color-gray-400: #f2f2f2;
--color-black: #000000;
--color-white: #ffffff;

/* Semantic */
--color-warning: #ff0004;

/* Gradient */
--gradient-blue-black: linear-gradient(180deg, #0046ac 0%, #000000 100%);
```

### Typography

**Headings**: Paperlogy (300/700/800)
- H1: 64px, H2: 48px, H3: 32px, H4: 28px, H5: 24px

**Body**: Pretendard (400/800)
- XL: 28px, Extra: 24px, Large: 20px, Medium: 16px, Small: 14px

### Component Classes

**Buttons**
```css
.btn-primary    /* 네이비 배경, 흰색 텍스트 */
.btn-secondary  /* 흰색 배경, 네이비 테두리 */
.btn-warning    /* 빨간색 배경, 삭제/경고용 */
```

**Tables**
```css
.admin-table        /* 기본 테이블 */
.admin-table thead  /* 네이비 배경 헤더 */
.admin-table tbody tr:hover  /* 호버 효과 */
```

**Forms**
```css
.form-group         /* 폼 그룹 컨테이너 */
.form-label         /* 라벨 */
.form-control       /* 입력 필드 */
.form-control.error /* 에러 상태 */
.form-error-message /* 에러 메시지 */
```

**Cards**
```css
.admin-card         /* 카드 컨테이너 */
.admin-card-header  /* 카드 헤더 */
.admin-card-body    /* 카드 본문 */
```

**Badges**
```css
.badge-primary      /* 네이비 배지 */
.badge-secondary    /* 연한 배지 */
.badge-warning      /* 빨간 배지 */
```

## Target Files

### Core Files
- `adm_cw/css/design-system.css` - 디자인 시스템 CSS
- `adm_cw/css/admin.css` - 관리자 메인 CSS
- `adm_cw/admin.head.php` - 헤더 템플릿

### Member Management
- `adm_cw/member_list_bri.php` - 회원 목록
- `adm_cw/member_form_bri.php` - 회원 등록/수정

### Shop Admin
- `adm_cw/shop_admin/itemlist_bri.php` - 캠페인 목록
- `adm_cw/shop_admin/itemform_bri.php` - 캠페인 등록/수정
- `adm_cw/shop_admin/orderlist_bri.php` - 기부 목록
- `adm_cw/shop_admin/inorderlist_bri.php` - 정기기부 목록

## Instructions

이 스킬이 호출되면:

1. **분석**: 대상 파일의 현재 스타일 분석
2. **CSS 변수 사용**: 하드코딩된 색상을 CSS 변수로 교체
3. **클래스 적용**: 인라인 스타일을 디자인 시스템 클래스로 교체
4. **일관성**: 모든 컴포넌트에 동일한 스타일 패턴 적용
5. **접근성**: WCAG 2.1 AA 준수 (색상 대비 4.5:1 이상)

### Task Examples

- "member_list_bri.php 스타일 개선해줘"
- "기부 관리 페이지 테이블 현대화해줘"
- "design-system.css에 새 컴포넌트 추가해줘"
- "폼 입력 필드 스타일 통일해줘"

## Constraints

- 기존 기능 유지 (backward compatibility)
- !important 최소화
- 인라인 스타일 금지 (동적 값 제외)
- 모바일 반응형 고려
- 크로스 브라우저 호환성 (Chrome, Firefox, Edge, Safari)

## Reference

- Figma Design: https://www.figma.com/design/JLcydBrlnKBsH3Z8SE96oM/
- 기존 에이전트 문서: `.claude/agents/admin-style-improver.md`
