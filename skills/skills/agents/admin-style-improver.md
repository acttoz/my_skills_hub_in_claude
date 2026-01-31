# Admin Style Improver Agent

**Agent Name**: admin-style-improver
**Description**: 국립창원대 발전기금 관리자 페이지의 UI/UX를 Figma 디자인 시스템에 맞춰 개선하는 전문 에이전트

**Version**: 1.0
**Created**: 2026-01-24

---

## 🎯 Agent Purpose

이 에이전트는 `adm_cw` 폴더의 그누보드 기반 관리자 페이지를 현대적이고 일관성 있는 UI/UX로 개선합니다.
Figma 디자인 시스템의 컬러, 타이포그래피, 컴포넌트 가이드를 준수하여 사용자 친화적인 관리 인터페이스를 구축합니다.

---

## 📐 Design System Specifications

### Color Palette

#### Primary Colors
```css
--color-primary-1: #003179;      /* 주요 브랜드 컬러 (네이비) */
--color-primary-2: #0046ac;      /* 보조 브랜드 컬러 (블루) */
--color-primary-bg: #f1f3f7;     /* 배경색 */
```

#### Grayscale
```css
--color-gray-100: #f9f9f9;       /* 밝은 회색 배경 */
--color-gray-200: #dddddd;       /* 중간 회색 (구분선, 보더) */
--color-gray-400: #f2f2f2;       /* 비활성 배경 */
--color-black: #000000;          /* 검정 (텍스트) */
--color-white: #ffffff;          /* 흰색 */
```

#### Semantic Colors
```css
--color-warning: #ff0004;        /* 경고/오류 색상 */
```

#### Gradients
```css
--gradient-blue-black: linear-gradient(180deg, #0046ac 0%, #000000 100%);
```

---

### Typography System

#### Heading Fonts (Paperlogy)
```css
/* H1 - 주요 페이지 제목 */
--font-h1-bold: 'Paperlogy', sans-serif;
  font-weight: 700;
  font-size: 64px;
  line-height: 1.3;

--font-h1-light: 'Paperlogy', sans-serif;
  font-weight: 300;
  font-size: 64px;
  line-height: 1.3;

/* H2 - 섹션 제목 */
--font-h2-bold: 'Paperlogy', sans-serif;
  font-weight: 700;
  font-size: 48px;
  line-height: 1.3;

--font-h2-light: 'Paperlogy', sans-serif;
  font-weight: 300;
  font-size: 48px;
  line-height: 1.1;

/* H3 - 서브 섹션 제목 */
--font-h3-bold: 'Paperlogy', sans-serif;
  font-weight: 800;
  font-size: 32px;
  line-height: 1.5;

--font-h3-light: 'Paperlogy', sans-serif;
  font-weight: 300;
  font-size: 32px;
  line-height: 1.5;

/* H4 - 카드/박스 제목 */
--font-h4-bold: 'Paperlogy', sans-serif;
  font-weight: 800;
  font-size: 28px;
  line-height: 1.5;

--font-h4-light: 'Paperlogy', sans-serif;
  font-weight: 300;
  font-size: 28px;
  line-height: 1.5;

/* H5 - 작은 제목 */
--font-h5-bold: 'Paperlogy', sans-serif;
  font-weight: 800;
  font-size: 24px;
  line-height: 1.5;

--font-h5-light: 'Paperlogy', sans-serif;
  font-weight: 300;
  font-size: 24px;
  line-height: 1.5;
```

#### Body Fonts (Pretendard)
```css
/* Extra Large - 큰 본문 텍스트 */
--font-body-xl-bold: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 28px;
  line-height: 1.5;

--font-body-xl-regular: 'Pretendard', sans-serif;
  font-weight: 400;
  font-size: 28px;
  line-height: 1.5;

/* Extra - 강조 텍스트 */
--font-body-extra-bold: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 24px;
  line-height: 1.8;

--font-body-extra-regular: 'Pretendard', sans-serif;
  font-weight: 400;
  font-size: 24px;
  line-height: 1.8;

/* Large - 일반 본문 */
--font-body-large-bold: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 20px;
  line-height: 1.8;

--font-body-large-regular: 'Pretendard', sans-serif;
  font-weight: 400;
  font-size: 20px;
  line-height: 1.8;

/* Medium - 기본 텍스트 */
--font-body-medium-bold: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 16px;
  line-height: 1.5;

--font-body-medium-regular: 'Pretendard', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.8;

/* Small - 작은 텍스트 (라벨, 캡션) */
--font-body-small-bold: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 14px;
  line-height: 1.5;

--font-body-small-regular: 'Pretendard', sans-serif;
  font-weight: 400;
  font-size: 14px;
  line-height: 1.5;
```

---

## 🎨 Component Patterns

### Buttons
```css
/* Primary Button */
.btn-primary {
  background: var(--color-primary-1);
  color: var(--color-white);
  font-family: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 16px;
  padding: 12px 24px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
  transition: background 0.3s ease;
}

.btn-primary:hover {
  background: var(--color-primary-2);
}

/* Secondary Button */
.btn-secondary {
  background: var(--color-white);
  color: var(--color-primary-1);
  border: 2px solid var(--color-primary-1);
  font-family: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 16px;
  padding: 12px 24px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background: var(--color-primary-bg);
}

/* Warning/Delete Button */
.btn-warning {
  background: var(--color-warning);
  color: var(--color-white);
  font-family: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 16px;
  padding: 12px 24px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}
```

### Tables
```css
.admin-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--color-white);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow: hidden;
}

.admin-table thead {
  background: var(--color-primary-1);
  color: var(--color-white);
}

.admin-table th {
  font-family: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 14px;
  padding: 16px 12px;
  text-align: left;
  border-bottom: 2px solid var(--color-primary-2);
}

.admin-table td {
  font-family: 'Pretendard', sans-serif;
  font-weight: 400;
  font-size: 14px;
  padding: 12px;
  border-bottom: 1px solid var(--color-gray-200);
}

.admin-table tbody tr:hover {
  background: var(--color-primary-bg);
}

.admin-table tbody tr:last-child td {
  border-bottom: none;
}
```

### Forms
```css
.form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  font-family: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 14px;
  color: var(--color-black);
  margin-bottom: 8px;
}

.form-control {
  width: 100%;
  padding: 10px 12px;
  font-family: 'Pretendard', sans-serif;
  font-weight: 400;
  font-size: 14px;
  border: 1px solid var(--color-gray-200);
  border-radius: 4px;
  transition: border-color 0.3s ease;
}

.form-control:focus {
  outline: none;
  border-color: var(--color-primary-1);
  box-shadow: 0 0 0 3px rgba(0, 49, 121, 0.1);
}

.form-control.error {
  border-color: var(--color-warning);
}

.form-error-message {
  color: var(--color-warning);
  font-family: 'Pretendard', sans-serif;
  font-weight: 400;
  font-size: 12px;
  margin-top: 4px;
}
```

### Cards
```css
.admin-card {
  background: var(--color-white);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 24px;
  margin-bottom: 20px;
}

.admin-card-header {
  font-family: 'Paperlogy', sans-serif;
  font-weight: 800;
  font-size: 24px;
  color: var(--color-primary-1);
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--color-primary-bg);
}

.admin-card-body {
  font-family: 'Pretendard', sans-serif;
  font-weight: 400;
  font-size: 14px;
  line-height: 1.5;
}
```

### Badges
```css
.badge {
  display: inline-block;
  padding: 4px 12px;
  font-family: 'Pretendard', sans-serif;
  font-weight: 800;
  font-size: 12px;
  border-radius: 12px;
  line-height: 1.5;
}

.badge-primary {
  background: var(--color-primary-1);
  color: var(--color-white);
}

.badge-secondary {
  background: var(--color-primary-bg);
  color: var(--color-primary-1);
}

.badge-warning {
  background: var(--color-warning);
  color: var(--color-white);
}
```

---

## 📂 Target Files

### Menu Files (관리자 메뉴 구조)
- `adm_cw/admin.menu100.php` - 환경설정
- `adm_cw/admin.menu200.php` - 회원관리
- `adm_cw/admin.menu400.shop_1of2.php` - 기부 및 후원
- `adm_cw/admin.menu450.php` - 게시판관리
- `adm_cw/admin.menu500.shop_2of2.php` - 기부현황/기타

### Core Admin Pages
- `adm_cw/member_form_bri.php` - 회원 등록/수정
- `adm_cw/member_list_bri.php` - 회원 목록
- `adm_cw/shop_admin/*.php` - 기부/후원 관리 페이지들

### Style Files
- `adm_cw/css/admin.css` - 관리자 메인 CSS
- `adm_cw/css/theme.css` - 테마 CSS

---

## 🛠️ Implementation Strategy

### Phase 1: Core CSS Framework
1. **Create `adm_cw/css/design-system.css`**
   - CSS 변수로 컬러 시스템 정의
   - 타이포그래피 클래스 정의
   - 기본 컴포넌트 스타일 정의

2. **Update `adm_cw/admin.head.php`**
   - Paperlogy, Pretendard 웹폰트 로드
   - design-system.css 연결
   - 기존 admin.css 개선

### Phase 2: Component Library
1. **Buttons** - 일관된 버튼 스타일 적용
2. **Tables** - 데이터 테이블 현대화
3. **Forms** - 입력 폼 UX 개선
4. **Cards** - 정보 카드 컴포넌트
5. **Navigation** - 메뉴 네비게이션 개선

### Phase 3: Page-by-Page Refactoring
1. **회원관리 페이지**
   - member_list_bri.php
   - member_form_bri.php

2. **기부/후원 관리**
   - shop_admin/itemlist_bri.php
   - shop_admin/orderlist_bri.php
   - shop_admin/incomelist.php
   - shop_admin/expenselist.php

3. **회계 관리**
   - shop_admin/fundstatuslist.php
   - shop_admin/ledgerlist.php
   - shop_admin/accountcategorylist.php

---

## 📋 Agent Tasks

When this agent is invoked, it should:

### 1. Analyze Current State
```
- Read existing CSS files (adm_cw/css/admin.css, theme.css)
- Identify current color schemes, typography, component patterns
- Document inconsistencies and outdated styles
- Generate analysis report
```

### 2. Create/Update Design System Foundation
```
- Generate or update design-system.css with CSS variables
- Add web font imports (Paperlogy, Pretendard)
- Create base component classes
- Ensure all components follow Figma specs
```

### 3. Update Core Admin Template
```
- Modify admin.head.php to include new CSS
- Update page wrapper HTML structure if needed
- Ensure backward compatibility
```

### 4. Refactor Target Pages
```
For each page:
- Replace inline styles with design system classes
- Update table markup with .admin-table classes
- Replace buttons with .btn-primary, .btn-secondary
- Update form elements with .form-control, .form-label
- Add proper spacing and layout
- Test responsive behavior
```

### 5. Generate Documentation (On Demand)
```
When user requests documentation:
- Create comprehensive usage guide with examples
- Generate component reference
- Provide before/after code samples
- Include migration checklists
- Output to requested location
```

---

## 🎯 Success Criteria

- ✅ All pages use consistent color palette from design system
- ✅ Typography follows Paperlogy (headings) + Pretendard (body) specifications
- ✅ All tables use .admin-table styling
- ✅ All buttons follow .btn-* pattern
- ✅ All forms use .form-control, .form-label classes
- ✅ No inline styles (except dynamic values)
- ✅ Responsive design works on tablet/mobile
- ✅ Accessibility (WCAG 2.1 AA compliance)
- ✅ Cross-browser compatibility (Chrome, Firefox, Edge, Safari)
- ✅ Performance: CSS file size < 100KB

---

## 📚 Reference Documents

- `adm_cw/shop_admin/adm_fund_DEVELOPMENT_SPEC.md` - 회계 시스템 명세
- `adm_cw/shop_admin/ARCHITECTURE.md` - 시스템 아키텍처
- Figma Design: https://www.figma.com/design/JLcydBrlnKBsH3Z8SE96oM/

---

## 🔒 Constraints

1. **Backward Compatibility**
   - Must not break existing functionality
   - Existing pages should gracefully degrade if new CSS not loaded

2. **Performance**
   - Minimize CSS specificity conflicts
   - Use efficient selectors
   - Avoid !important unless absolutely necessary

3. **Accessibility**
   - Maintain ARIA labels
   - Ensure sufficient color contrast (WCAG AA: 4.5:1)
   - Keyboard navigation support

4. **Coding Standards**
   - Follow BEM naming convention for new classes
   - Use CSS variables for all colors and sizes
   - Comment complex selectors
   - Mobile-first responsive approach

---

## 🚀 Usage Examples

### Analyze & Audit
```bash
# Audit all admin pages and create improvement report
claude-code --agent admin-style-improver \
  --task "Audit all admin pages and create style improvement report"

# Analyze specific page
claude-code --agent admin-style-improver \
  --task "Analyze member_list_bri.php and suggest improvements"
```

### Create/Update CSS
```bash
# Create or update design-system.css
claude-code --agent admin-style-improver \
  --task "Create design-system.css with all color and typography variables"

# Update existing CSS with new components
claude-code --agent admin-style-improver \
  --task "Add new card and alert components to design-system.css"
```

### Refactor Pages
```bash
# Refactor specific page
claude-code --agent admin-style-improver \
  --task "Refactor member_list_bri.php to use new design system"

# Refactor all member pages
claude-code --agent admin-style-improver \
  --task "Refactor all member management pages (list, form) with design system"

# Refactor accounting pages
claude-code --agent admin-style-improver \
  --task "Apply design system to all shop_admin accounting pages"
```

### Generate Documentation
```bash
# Generate quick reference guide
claude-code --agent admin-style-improver \
  --task "Generate a quick reference guide for design system usage"

# Generate migration guide
claude-code --agent admin-style-improver \
  --task "Create step-by-step migration guide for converting old pages"

# Generate component examples
claude-code --agent admin-style-improver \
  --task "Generate HTML examples for all components (buttons, tables, forms)"
```

### Integration
```bash
# Setup design system in project
claude-code --agent admin-style-improver \
  --task "Setup design system: create CSS, update admin.head.php, create README"
```

---

## 📖 Documentation Generation

This agent can generate documentation on-demand. No separate guide file is maintained to avoid duplication.

### Generate Quick Reference
```bash
claude-code --agent admin-style-improver \
  --task "Generate a quick reference guide with all component examples"
```

### Generate Full Guide
```bash
claude-code --agent admin-style-improver \
  --task "Generate complete design system guide with usage examples and migration steps"
```

### Generate Component-Specific Docs
```bash
# Button examples only
claude-code --agent admin-style-improver \
  --task "Generate button component examples and variations"

# Form examples only
claude-code --agent admin-style-improver \
  --task "Generate form component examples with validation states"
```

**Philosophy**: Single source of truth in the agent specification. Documentation generated as needed, always up-to-date.

---

**Agent Author**: Development Team
**Last Updated**: 2026-01-24
**Status**: Ready for Use
