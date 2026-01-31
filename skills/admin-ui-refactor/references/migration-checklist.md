# Migration Checklist

Step-by-step guide for migrating legacy admin pages to the new design system.

---

## Pre-Migration Setup

### 1. Setup Design System (One-Time)

**If not already done, complete these steps once for the entire project:**

- [ ] Create `adm_cw/css/design-system.css` (copy from skill assets)
- [ ] Update `adm_cw/admin.head.php` to include design-system.css:
  ```php
  <link rel="stylesheet" href="<?php echo G5_ADMIN_URL ?>/css/design-system.css">
  ```
- [ ] Verify web fonts are loading (check browser DevTools)
- [ ] Test on a simple page to ensure CSS is working

### 2. Prepare Development Environment

- [ ] Create a git branch for the migration (e.g., `feature/design-system-migration`)
- [ ] Backup the database (if testing with real data)
- [ ] Setup local development environment
- [ ] Have Figma design reference open

---

## Page Migration Workflow

**Follow this workflow for EACH page you migrate:**

### Step 1: Analysis

- [ ] Read the target PHP file completely
- [ ] Identify all UI components used:
  - [ ] Tables
  - [ ] Forms
  - [ ] Buttons
  - [ ] Cards/containers
  - [ ] Alerts/messages
  - [ ] Pagination
- [ ] List all inline styles that need to be replaced
- [ ] Note any custom JavaScript that might be affected
- [ ] Screenshot the current page for comparison

**Optional:** Run audit script:
```bash
python scripts/audit_styles.py adm_cw/target_page.php
```

### Step 2: Backup

- [ ] Create a backup copy of the original file:
  ```bash
  cp adm_cw/target_page.php adm_cw/target_page.php.backup
  ```
- [ ] Commit the current state to git
- [ ] Create a test page URL to preview changes

### Step 3: Header & Container

- [ ] Update page header to use typography classes:
  ```html
  <!-- Before -->
  <h2 style="font-size:24px; font-weight:bold;">회원 목록</h2>

  <!-- After -->
  <h2 class="heading-h3-bold">회원 목록</h2>
  ```

- [ ] Wrap content in admin-card if needed:
  ```html
  <div class="admin-card">
    <div class="admin-card-header">섹션 제목</div>
    <div class="admin-card-body">
      <!-- Content -->
    </div>
  </div>
  ```

### Step 4: Replace Tables

- [ ] Replace table styles:
  ```html
  <!-- Before -->
  <table style="width:100%; border:1px solid #ccc;">
    <thead style="background:#333; color:#fff;">

  <!-- After -->
  <table class="admin-table">
    <thead>
  ```

- [ ] Add alignment classes to th/td:
  ```html
  <th class="center">상태</th>
  <td class="center">데이터</td>
  ```

- [ ] Remove all inline table styles

### Step 5: Replace Buttons

- [ ] Replace all buttons:
  ```html
  <!-- Before -->
  <button style="background:#003179; color:#fff; padding:10px 20px;">등록</button>

  <!-- After -->
  <button class="btn btn-primary">등록</button>
  ```

- [ ] Apply correct variant:
  - Primary: Main actions (저장, 등록, 확인)
  - Secondary: Cancel/back (취소, 목록)
  - Warning: Delete/dangerous (삭제, 탈퇴)
  - Success: Approve (승인, 활성화)

- [ ] Add size classes if needed (`.btn-sm`, `.btn-lg`)

### Step 6: Replace Forms

- [ ] Wrap each field in `.form-group`:
  ```html
  <div class="form-group">
    <label class="form-label required">이름</label>
    <input type="text" class="form-control" name="name">
  </div>
  ```

- [ ] Replace all input/select/textarea:
  ```html
  <!-- Before -->
  <input type="text" style="width:100%; padding:8px; border:1px solid #ddd;">

  <!-- After -->
  <input type="text" class="form-control">
  ```

- [ ] Add `.required` to mandatory field labels
- [ ] Replace error messages with `.form-error-message`
- [ ] Replace help text with `.form-help-text`

### Step 7: Replace Badges/Status Indicators

- [ ] Replace status indicators:
  ```html
  <!-- Before -->
  <span style="background:#28a745; color:#fff; padding:4px 8px; border-radius:4px;">활성</span>

  <!-- After -->
  <span class="badge badge-success">활성</span>
  ```

### Step 8: Replace Alerts/Messages

- [ ] Replace success/error messages:
  ```html
  <!-- Before -->
  <div style="background:#d4edda; padding:12px; border:1px solid #c3e6cb;">
    성공적으로 저장되었습니다.
  </div>

  <!-- After -->
  <div class="alert alert-success">
    성공적으로 저장되었습니다.
  </div>
  ```

### Step 9: Update Pagination

- [ ] Replace pagination HTML:
  ```html
  <!-- After -->
  <ul class="pagination">
    <li class="pagination-item">
      <a href="?page=1" class="pagination-link">«</a>
    </li>
    <li class="pagination-item">
      <a href="?page=1" class="pagination-link active">1</a>
    </li>
    <!-- ... -->
  </ul>
  ```

### Step 10: Remove Inline Styles

- [ ] Search for all `style="` attributes
- [ ] Replace with design system classes
- [ ] Keep only dynamic styles (e.g., `style="width:<?php echo $dynamic_width ?>%"`)

**Common replacements:**

| Inline Style | Design System Class |
|--------------|---------------------|
| `style="text-align:center"` | `class="text-center"` |
| `style="margin-top:20px"` | `class="mt-3"` |
| `style="margin-bottom:20px"` | `class="mb-3"` |
| `style="padding:20px"` | `class="p-3"` |
| `style="color:#003179"` | `class="text-primary"` |
| `style="color:#ff0004"` | `class="text-warning"` |
| `style="display:flex"` | `class="d-flex"` |

### Step 11: Test Functionality

- [ ] Load the page in browser
- [ ] Test all forms (submit, validation)
- [ ] Test all buttons (click, actions)
- [ ] Test search functionality
- [ ] Test pagination
- [ ] Test filters/sorting
- [ ] Verify data displays correctly
- [ ] Check console for JavaScript errors

### Step 12: Test Responsiveness

- [ ] Test on mobile (Chrome DevTools)
- [ ] Test on tablet (768px - 1024px)
- [ ] Test on desktop (1024px+)
- [ ] Verify tables are scrollable on mobile if needed
- [ ] Verify buttons stack properly on mobile

### Step 13: Accessibility Check

- [ ] Tab through all interactive elements
- [ ] Verify focus indicators are visible
- [ ] Check color contrast (use browser extension)
- [ ] Verify all form labels are present
- [ ] Test screen reader (optional but recommended)

### Step 14: Code Cleanup

- [ ] Remove commented-out old code
- [ ] Remove unused CSS classes
- [ ] Format code properly (indentation)
- [ ] Add comments for complex sections if needed

### Step 15: Documentation

- [ ] Take "after" screenshot
- [ ] Document any issues encountered
- [ ] Note any custom styles that couldn't be replaced
- [ ] Update related documentation if needed

### Step 16: Review & Commit

- [ ] Compare before/after screenshots
- [ ] Review all changes in diff
- [ ] Test one more time
- [ ] Commit changes with descriptive message:
  ```bash
  git add adm_cw/target_page.php
  git commit -m "Refactor target_page.php to use design system

  - Replaced inline styles with design system classes
  - Updated tables to use .admin-table
  - Replaced buttons with .btn-* classes
  - Updated forms with .form-control and .form-label
  - Tested functionality and responsiveness"
  ```

---

## Common Issues & Solutions

### Issue 1: Table Too Wide on Mobile

**Problem:** Table overflows on mobile devices.

**Solution:** Wrap table in scrollable container:
```html
<div style="overflow-x: auto;">
  <table class="admin-table">
    <!-- ... -->
  </table>
</div>
```

### Issue 2: Buttons Too Wide on Mobile

**Problem:** Buttons take full width on mobile.

**Solution:** This is intentional for better mobile UX. To prevent:
```html
<div class="d-flex gap-2">
  <button class="btn btn-primary" style="width:auto;">버튼</button>
</div>
```

### Issue 3: Form Labels Not Aligning

**Problem:** Labels and inputs not aligned properly.

**Solution:** Ensure each field is wrapped in `.form-group`:
```html
<div class="form-group">
  <label class="form-label">레이블</label>
  <input type="text" class="form-control">
</div>
```

### Issue 4: Colors Don't Match Exactly

**Problem:** Custom colors in old design don't match design system.

**Solution:** Use closest design system color. If truly needed, document the exception:
```html
<!-- Exception: Client-specific branding color -->
<div style="background: #custom-color;">
```

### Issue 5: JavaScript Selectors Broken

**Problem:** JavaScript relies on old class names.

**Solution:** Update JavaScript selectors OR add data attributes:
```html
<button class="btn btn-primary" data-action="submit">버튼</button>
```

```javascript
// JavaScript
document.querySelector('[data-action="submit"]').addEventListener('click', ...);
```

### Issue 6: Print Styles Broken

**Problem:** Page doesn't print correctly.

**Solution:** Add print-specific styles if needed:
```css
@media print {
  .btn { display: none; }
  .admin-table { box-shadow: none; }
}
```

---

## Quality Checklist

**Before marking a page as "complete", verify:**

- [ ] ✅ All inline styles removed (except dynamic values)
- [ ] ✅ All tables use `.admin-table`
- [ ] ✅ All buttons use `.btn-*` classes
- [ ] ✅ All forms use `.form-control`, `.form-label`
- [ ] ✅ All headings use typography classes
- [ ] ✅ Color palette matches design system
- [ ] ✅ Spacing uses design system utilities
- [ ] ✅ Functionality works correctly
- [ ] ✅ Responsive on mobile/tablet
- [ ] ✅ Passes accessibility checks
- [ ] ✅ No console errors
- [ ] ✅ Code is clean and formatted
- [ ] ✅ Changes are committed to git

---

## Batch Migration Strategy

**For migrating multiple pages:**

### Priority 1: Core Pages (Week 1)
1. `member_list_bri.php` - Member list
2. `member_form_bri.php` - Member form
3. `admin.menu*.php` - Navigation menus

### Priority 2: Shop/Donation Pages (Week 2)
4. `shop_admin/itemlist_bri.php` - Item list
5. `shop_admin/itemform_bri.php` - Item form
6. `shop_admin/orderlist_bri.php` - Order list
7. `shop_admin/orderform_bri.php` - Order form

### Priority 3: Accounting Pages (Week 3)
8. `shop_admin/incomelist.php` - Income list
9. `shop_admin/expenselist.php` - Expense list
10. `shop_admin/ledgerlist.php` - Ledger list
11. `shop_admin/fundstatuslist.php` - Fund status

### Priority 4: Configuration & Reports (Week 4)
12. Configuration pages
13. Report pages
14. Statistics pages

**Tips:**
- Migrate 2-3 pages per day maximum
- Test each page thoroughly before moving to next
- Keep a migration log (spreadsheet or markdown file)
- Get user feedback after each priority group

---

## Migration Log Template

Keep track of your progress:

```markdown
# Design System Migration Log

## Completed
- [x] member_list_bri.php - 2026-01-24 - No issues
- [x] member_form_bri.php - 2026-01-24 - Custom validation JS updated

## In Progress
- [ ] itemlist_bri.php - Started 2026-01-25

## Pending
- [ ] orderlist_bri.php
- [ ] orderform_bri.php
- ...

## Issues
1. member_form_bri.php - Daum postcode integration needed custom modal styling
2. ...
```

---

## Post-Migration

**After all pages are migrated:**

- [ ] Remove old CSS files (admin.css, theme.css) if no longer needed
- [ ] Update documentation
- [ ] Create design system usage guide for new developers
- [ ] Archive backup files
- [ ] Deploy to staging for QA testing
- [ ] Get stakeholder approval
- [ ] Deploy to production
- [ ] Monitor for issues
- [ ] Collect user feedback

**Congratulations on completing the migration!** 🎉
