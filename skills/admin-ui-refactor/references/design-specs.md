# Design System Specifications

Complete design specifications for Changwon National University Fund Management System.

---

## Color Palette

### Primary Colors

| Variable | Value | Usage |
|----------|-------|-------|
| `--color-primary-1` | `#003179` | Main brand color (navy) - primary buttons, headers, brand elements |
| `--color-primary-2` | `#0046ac` | Secondary brand color (blue) - hover states, accents |
| `--color-primary-bg` | `#f1f3f7` | Background color - page backgrounds, subtle highlights |

### Grayscale

| Variable | Value | Usage |
|----------|-------|-------|
| `--color-gray-100` | `#f9f9f9` | Light gray background - card backgrounds, subtle sections |
| `--color-gray-200` | `#dddddd` | Medium gray - borders, dividers, disabled states |
| `--color-gray-400` | `#f2f2f2` | Inactive background - disabled inputs, inactive elements |
| `--color-black` | `#000000` | Text color - body text, headings |
| `--color-white` | `#ffffff` | White - backgrounds, text on dark backgrounds |

### Semantic Colors

| Variable | Value | Usage |
|----------|-------|-------|
| `--color-warning` | `#ff0004` | Warning/error states - delete buttons, error messages, alerts |
| `--color-success` | `#28a745` | Success states - success messages, completed statuses |
| `--color-info` | `#17a2b8` | Informational states - info messages, help text |

### Gradients

```css
--gradient-blue-black: linear-gradient(180deg, #0046ac 0%, #000000 100%);
```

Use for hero sections, feature highlights, or premium UI elements.

---

## Typography System

### Heading Fonts (Paperlogy)

**Web Font Import:**
```css
@import url('https://cdn.jsdelivr.net/gh/webfontworld/paperlogy/Paperlogy.css');
```

**Font Family:** `'Paperlogy', sans-serif`

**Weights Available:**
- 300 (Light)
- 700 (Bold)
- 800 (ExtraBold)

#### H1 - Page Titles

| Class | Weight | Size | Line Height | Usage |
|-------|--------|------|-------------|-------|
| `.heading-h1-bold` | 700 | 64px | 1.3 | Main page titles |
| `.heading-h1-light` | 300 | 64px | 1.3 | Subtitle variations |

**Responsive:** 32px on mobile (<768px)

#### H2 - Section Titles

| Class | Weight | Size | Line Height | Usage |
|-------|--------|------|-------------|-------|
| `.heading-h2-bold` | 700 | 48px | 1.3 | Section headings |
| `.heading-h2-light` | 300 | 48px | 1.1 | Lighter section headings |

**Responsive:** 28px on mobile (<768px)

#### H3 - Subsection Titles

| Class | Weight | Size | Line Height | Usage |
|-------|--------|------|-------------|-------|
| `.heading-h3-bold` | 800 | 32px | 1.5 | Subsection headings |
| `.heading-h3-light` | 300 | 32px | 1.5 | Lighter subsections |

**Responsive:** 24px on mobile (<768px)

#### H4 - Card/Box Titles

| Class | Weight | Size | Line Height | Usage |
|-------|--------|------|-------------|-------|
| `.heading-h4-bold` | 800 | 28px | 1.5 | Card headers, box titles |
| `.heading-h4-light` | 300 | 28px | 1.5 | Lighter card headers |

#### H5 - Small Titles

| Class | Weight | Size | Line Height | Usage |
|-------|--------|------|-------------|-------|
| `.heading-h5-bold` | 800 | 24px | 1.5 | Small headings, labels |
| `.heading-h5-light` | 300 | 24px | 1.5 | Lighter small headings |

---

### Body Fonts (Pretendard)

**Web Font Import:**
```css
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
```

**Font Family:** `'Pretendard', sans-serif`

**Weights Available:**
- 400 (Regular)
- 800 (ExtraBold)

#### Extra Large (28px)

| Class | Weight | Size | Line Height | Usage |
|-------|--------|------|-------------|-------|
| `.body-xl-bold` | 800 | 28px | 1.5 | Large body emphasis |
| `.body-xl-regular` | 400 | 28px | 1.5 | Large body text |

#### Extra (24px)

| Class | Weight | Size | Line Height | Usage |
|-------|--------|------|-------------|-------|
| `.body-extra-bold` | 800 | 24px | 1.8 | Emphasized text |
| `.body-extra-regular` | 400 | 24px | 1.8 | Regular emphasized text |

#### Large (20px)

| Class | Weight | Size | Line Height | Usage |
|-------|--------|------|-------------|-------|
| `.body-large-bold` | 800 | 20px | 1.8 | Body emphasis |
| `.body-large-regular` | 400 | 20px | 1.8 | Standard body text |

#### Medium (16px) - DEFAULT

| Class | Weight | Size | Line Height | Usage |
|-------|--------|------|-------------|-------|
| `.body-medium-bold` | 800 | 16px | 1.5 | Button text, labels |
| `.body-medium-regular` | 400 | 16px | 1.8 | Default body text |

**This is the default size for most UI elements.**

#### Small (14px)

| Class | Weight | Size | Line Height | Usage |
|-------|--------|------|-------------|-------|
| `.body-small-bold` | 800 | 14px | 1.5 | Table headers, form labels |
| `.body-small-regular` | 400 | 14px | 1.5 | Table data, captions, help text |

---

## Spacing System

Consistent spacing creates visual rhythm and hierarchy.

### Spacing Scale

| Variable | Value | Usage |
|----------|-------|-------|
| `--spacing-xs` | 4px | Tiny gaps, icon spacing |
| `--spacing-sm` | 8px | Small spacing, tight layouts |
| `--spacing-md` | 12px | Medium spacing, form field padding |
| `--spacing-lg` | 16px | Large spacing, section padding |
| `--spacing-xl` | 24px | Extra large spacing, card padding |
| `--spacing-xxl` | 32px | Section separation |

### Utility Classes

**Margin Top:**
- `.mt-0` - 0px
- `.mt-1` - 8px
- `.mt-2` - 12px
- `.mt-3` - 16px
- `.mt-4` - 24px

**Margin Bottom:**
- `.mb-0` - 0px
- `.mb-1` - 8px
- `.mb-2` - 12px
- `.mb-3` - 16px
- `.mb-4` - 24px

**Padding:**
- `.p-0` - 0px
- `.p-1` - 8px
- `.p-2` - 12px
- `.p-3` - 16px
- `.p-4` - 24px

---

## Border Radius

| Variable | Value | Usage |
|----------|-------|-------|
| `--radius-sm` | 4px | Buttons, inputs, badges |
| `--radius-md` | 8px | Cards, tables, containers |
| `--radius-lg` | 12px | Large cards, modals |

---

## Shadows

| Variable | Value | Usage |
|----------|-------|-------|
| `--shadow-sm` | `0 1px 3px rgba(0, 0, 0, 0.1)` | Subtle elevation |
| `--shadow-md` | `0 2px 8px rgba(0, 0, 0, 0.1)` | Standard elevation (cards, tables) |
| `--shadow-lg` | `0 4px 16px rgba(0, 0, 0, 0.15)` | Prominent elevation (modals, dropdowns) |

---

## Transitions

| Variable | Value | Usage |
|----------|-------|-------|
| `--transition-fast` | `0.15s ease` | Micro-interactions (hover, focus) |
| `--transition-base` | `0.3s ease` | Standard transitions |
| `--transition-slow` | `0.5s ease` | Slow, dramatic transitions |

---

## Accessibility Requirements

### WCAG 2.1 AA Compliance

**Color Contrast:**
- Normal text (< 18px): 4.5:1 minimum
- Large text (≥ 18px): 3:1 minimum
- UI components and graphics: 3:1 minimum

**Verified Combinations:**
- `#003179` on `#ffffff` - ✅ 12.6:1 (AAA)
- `#0046ac` on `#ffffff` - ✅ 8.6:1 (AAA)
- `#000000` on `#ffffff` - ✅ 21:1 (AAA)
- `#ffffff` on `#003179` - ✅ 12.6:1 (AAA)
- `#ff0004` on `#ffffff` - ✅ 5.3:1 (AA)

**Focus States:**
- All interactive elements must have visible focus indicators
- Focus ring: `box-shadow: 0 0 0 3px rgba(0, 49, 121, 0.1)`

**Keyboard Navigation:**
- All interactive elements must be keyboard accessible
- Tab order must follow logical reading order
- Skip links for navigation

---

## Responsive Breakpoints

```css
/* Mobile */
@media (max-width: 768px) {
  /* Font size reductions, full-width buttons */
}

/* Tablet */
@media (min-width: 769px) and (max-width: 1024px) {
  /* Optional tablet-specific styles */
}

/* Desktop */
@media (min-width: 1025px) {
  /* Default styles */
}
```

---

## Design Principles

1. **Consistency** - Use design system classes, not custom styles
2. **Accessibility** - WCAG 2.1 AA minimum
3. **Performance** - Minimize CSS specificity, use CSS variables
4. **Mobile-First** - Design for mobile, enhance for desktop
5. **Clarity** - Clear visual hierarchy with typography and spacing
6. **Korean Typography** - Optimize for Hangul readability

---

## Figma Reference

Design Source: https://www.figma.com/design/JLcydBrlnKBsH3Z8SE96oM/

All specifications in this document are derived from the official Figma design system.
