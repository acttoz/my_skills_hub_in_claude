---
name: admin-ui-refactor
description: Refactor Korean university fund admin pages to modern Figma design system with Paperlogy/Pretendard typography and consistent UI components. Use when modernizing Gnuboard-based admin interfaces or applying design system to legacy PHP admin pages.
---

# Admin UI Refactor Skill

Refactor legacy Gnuboard-based admin pages to modern, accessible UI using the university fund design system with Paperlogy/Pretendard typography and standardized components.

## When to Use This Skill

Use this skill when:
- Modernizing `adm_cw` folder admin pages to match Figma design system
- Creating or updating `design-system.css` with CSS variables
- Applying consistent color palette and typography to admin interfaces
- Refactoring tables, forms, buttons to use standardized component classes
- Analyzing admin pages for style inconsistencies
- Generating design system documentation or component examples

## How to Use This Skill

### 1. Design System Foundation

The design system is defined in `references/design-specs.md`. Key elements:

**Color Palette:**
- Primary: `#003179` (navy), `#0046ac` (blue)
- Grayscale: `#f9f9f9`, `#dddddd`, `#f2f2f2`
- Semantic: `#ff0004` (warning)

**Typography:**
- Headings: Paperlogy (300, 700, 800 weights)
- Body: Pretendard (400, 800 weights)

**Components:**
- Buttons: `.btn-primary`, `.btn-secondary`, `.btn-warning`
- Tables: `.admin-table`
- Forms: `.form-control`, `.form-label`, `.form-group`
- Cards: `.admin-card`, `.admin-card-header`
- Badges: `.badge-primary`, `.badge-secondary`

Refer to `references/design-specs.md` for complete specifications.

### 2. Creating design-system.css

When creating the design system CSS file:

1. Copy `assets/design-system.css` to `adm_cw/css/design-system.css`
2. Verify all CSS variables are defined at `:root`
3. Ensure web fonts (Paperlogy, Pretendard) are imported
4. Include all component classes

Example:
```css
@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;800&display=swap');

:root {
  --color-primary-1: #003179;
  --color-primary-2: #0046ac;
  /* ... more variables ... */
}

.btn-primary {
  background: var(--color-primary-1);
  /* ... */
}
```

### 3. Refactoring Pages

When refactoring admin pages:

1. **Analyze current state** - Run `scripts/audit_styles.py` to identify issues
2. **Update HTML structure** - Replace inline styles with design system classes
3. **Update admin.head.php** - Include design-system.css if not already included
4. **Test components** - Verify all components render correctly

**Example refactoring:**

Before:
```html
<table style="width:100%; border:1px solid #ccc;">
  <thead style="background:#333; color:#fff;">
    <th>이름</th>
  </thead>
</table>
```

After:
```html
<table class="admin-table">
  <thead>
    <th>이름</th>
  </thead>
</table>
```

### 4. Component Examples

Reference `assets/component-examples.html` for complete component usage examples.

View component guide at `references/component-guide.md` for detailed usage patterns.

### 5. Auditing Pages

To analyze admin pages for style inconsistencies:

```bash
python scripts/audit_styles.py adm_cw/member_list_bri.php
```

The script identifies:
- Inline styles that should use CSS classes
- Inconsistent color usage
- Missing design system classes
- Accessibility issues

### 6. Migration Workflow

Follow this workflow when refactoring pages:

1. **Read** `references/migration-checklist.md` for step-by-step guide
2. **Audit** the target page with audit script
3. **Backup** original file
4. **Refactor** HTML markup to use design system classes
5. **Test** visual appearance and functionality
6. **Validate** accessibility and responsiveness

## Target Files in Project

**Core Admin Files:**
- `adm_cw/admin.head.php` - Include design-system.css here
- `adm_cw/css/admin.css` - Legacy CSS file
- `adm_cw/css/design-system.css` - New design system CSS

**Page Files to Refactor:**
- `adm_cw/member_list_bri.php` - Member list
- `adm_cw/member_form_bri.php` - Member form
- `adm_cw/shop_admin/itemlist_bri.php` - Donation items
- `adm_cw/shop_admin/orderlist_bri.php` - Order list
- Other `shop_admin/*.php` files

**Menu Files:**
- `adm_cw/admin.menu*.php` - Admin navigation menus

## Best Practices

1. **Always use CSS variables** - Never hardcode colors or font sizes
2. **Mobile-first** - Design for mobile, enhance for desktop
3. **Accessibility** - Maintain WCAG 2.1 AA compliance (4.5:1 contrast ratio)
4. **Performance** - Minimize CSS specificity, avoid !important
5. **BEM naming** - Use Block Element Modifier convention for new classes
6. **No inline styles** - Use design system classes instead
7. **Backward compatibility** - Ensure existing functionality remains intact

## Success Criteria

A successfully refactored page should:
- ✅ Use consistent color palette from design system
- ✅ Apply correct typography (Paperlogy headings, Pretendard body)
- ✅ Use `.admin-table` for all data tables
- ✅ Use `.btn-*` classes for all buttons
- ✅ Use `.form-control` for all form inputs
- ✅ Have no inline styles (except dynamic values)
- ✅ Be responsive on mobile/tablet
- ✅ Pass WCAG 2.1 AA accessibility checks

## Example Tasks

**Create design system CSS:**
"Create the design-system.css file with all color variables and components"

**Refactor specific page:**
"Refactor member_list_bri.php to use the new design system"

**Audit pages:**
"Audit all member management pages and create an improvement report"

**Generate documentation:**
"Generate a quick reference guide for the design system components"

**Setup project:**
"Setup the design system: create CSS, update admin.head.php, and create component examples"

## Notes

- This skill is specifically designed for the Changwon University fund management system
- The design system follows Korean web standards and accessibility guidelines
- All Korean text should be preserved as-is
- The system uses Gnuboard 5 framework conventions
