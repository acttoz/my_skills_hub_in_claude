# Component Usage Guide

Detailed usage guide for all design system components.

---

## Buttons

### Basic Button Structure

```html
<button class="btn btn-{variant} btn-{size}">버튼 텍스트</button>
```

### Variants

#### Primary Button (기본 액션)

Use for primary actions: submit forms, save changes, confirm actions.

```html
<button class="btn btn-primary">등록</button>
<button class="btn btn-primary">저장</button>
<button class="btn btn-primary">확인</button>
```

**Style:**
- Background: `#003179` (navy)
- Text: `#ffffff` (white)
- Hover: `#0046ac` (lighter blue)

#### Secondary Button (보조 액션)

Use for secondary actions: cancel, go back, alternative actions.

```html
<button class="btn btn-secondary">취소</button>
<button class="btn btn-secondary">목록으로</button>
```

**Style:**
- Background: `#ffffff` (white)
- Text: `#003179` (navy)
- Border: 2px solid `#003179`
- Hover: Background changes to `#f1f3f7`

#### Warning Button (삭제/위험 액션)

Use for destructive actions: delete, remove, cancel membership.

```html
<button class="btn btn-warning">삭제</button>
<button class="btn btn-warning">회원탈퇴</button>
```

**Style:**
- Background: `#ff0004` (red)
- Text: `#ffffff` (white)

#### Success Button (승인 액션)

Use for approval actions: approve, accept, enable.

```html
<button class="btn btn-success">승인</button>
<button class="btn btn-success">활성화</button>
```

**Style:**
- Background: `#28a745` (green)
- Text: `#ffffff` (white)

### Sizes

```html
<button class="btn btn-primary btn-sm">작은 버튼</button>
<button class="btn btn-primary">기본 크기</button>
<button class="btn btn-primary btn-lg">큰 버튼</button>
```

**Sizes:**
- `.btn-sm` - Small (14px text, 8px/16px padding)
- Default - Medium (16px text, 12px/24px padding)
- `.btn-lg` - Large (18px text, 16px/32px padding)

### States

```html
<!-- Disabled state -->
<button class="btn btn-primary" disabled>비활성화</button>
```

### Button Groups

```html
<div class="d-flex gap-2">
  <button class="btn btn-primary">저장</button>
  <button class="btn btn-secondary">취소</button>
</div>
```

---

## Tables

### Basic Table Structure

```html
<table class="admin-table">
  <thead>
    <tr>
      <th>컬럼1</th>
      <th class="center">중앙정렬</th>
      <th class="right">오른쪽정렬</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>데이터1</td>
      <td class="center">데이터2</td>
      <td class="right">데이터3</td>
    </tr>
  </tbody>
</table>
```

### Alignment

```html
<!-- Default: Left aligned -->
<th>이름</th>
<td>홍길동</td>

<!-- Center aligned -->
<th class="center">상태</th>
<td class="center">활성</td>

<!-- Right aligned -->
<th class="right">금액</th>
<td class="right">10,000원</td>
```

### With Actions

```html
<table class="admin-table">
  <thead>
    <tr>
      <th>번호</th>
      <th>이름</th>
      <th class="center">관리</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>홍길동</td>
      <td class="center">
        <button class="btn btn-primary btn-sm">수정</button>
        <button class="btn btn-warning btn-sm">삭제</button>
      </td>
    </tr>
  </tbody>
</table>
```

### With Badges

```html
<table class="admin-table">
  <thead>
    <tr>
      <th>이름</th>
      <th class="center">상태</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>홍길동</td>
      <td class="center">
        <span class="badge badge-success">활성</span>
      </td>
    </tr>
    <tr>
      <td>김철수</td>
      <td class="center">
        <span class="badge badge-warning">대기</span>
      </td>
    </tr>
  </tbody>
</table>
```

---

## Forms

### Basic Form Group

```html
<div class="form-group">
  <label class="form-label">레이블</label>
  <input type="text" class="form-control" placeholder="입력하세요">
</div>
```

### Required Fields

```html
<div class="form-group">
  <label class="form-label required">이름</label>
  <input type="text" class="form-control" placeholder="이름을 입력하세요" required>
</div>
```

**Note:** `.required` class automatically adds red asterisk (*) after label.

### Input Types

#### Text Input

```html
<div class="form-group">
  <label class="form-label">이름</label>
  <input type="text" class="form-control" placeholder="이름 입력">
</div>
```

#### Email Input

```html
<div class="form-group">
  <label class="form-label">이메일</label>
  <input type="email" class="form-control" placeholder="email@example.com">
</div>
```

#### Number Input

```html
<div class="form-group">
  <label class="form-label">금액</label>
  <input type="number" class="form-control" placeholder="0">
</div>
```

#### Select Dropdown

```html
<div class="form-group">
  <label class="form-label">회원등급</label>
  <select class="form-control">
    <option value="">선택하세요</option>
    <option value="1">일반회원</option>
    <option value="2">우수회원</option>
    <option value="3">VIP회원</option>
  </select>
</div>
```

#### Textarea

```html
<div class="form-group">
  <label class="form-label">메모</label>
  <textarea class="form-control" rows="4" placeholder="메모를 입력하세요"></textarea>
</div>
```

### Error States

```html
<div class="form-group">
  <label class="form-label">이메일</label>
  <input type="email" class="form-control error" value="invalid-email">
  <span class="form-error-message">올바른 이메일 주소를 입력하세요.</span>
</div>
```

### Help Text

```html
<div class="form-group">
  <label class="form-label">비밀번호</label>
  <input type="password" class="form-control">
  <span class="form-help-text">8자 이상, 영문/숫자/특수문자 조합</span>
</div>
```

### Checkbox & Radio

```html
<!-- Checkbox -->
<div class="form-group">
  <label>
    <input type="checkbox" name="agree">
    개인정보 수집에 동의합니다.
  </label>
</div>

<!-- Radio -->
<div class="form-group">
  <label class="form-label">성별</label>
  <label>
    <input type="radio" name="gender" value="M"> 남성
  </label>
  <label>
    <input type="radio" name="gender" value="F"> 여성
  </label>
</div>
```

---

## Cards

### Basic Card

```html
<div class="admin-card">
  <div class="admin-card-header">카드 제목</div>
  <div class="admin-card-body">
    <p>카드 본문 내용입니다.</p>
  </div>
</div>
```

### Card with Footer

```html
<div class="admin-card">
  <div class="admin-card-header">회원 정보</div>
  <div class="admin-card-body">
    <p>이름: 홍길동</p>
    <p>이메일: hong@example.com</p>
  </div>
  <div class="admin-card-footer">
    <button class="btn btn-primary">수정</button>
    <button class="btn btn-secondary">취소</button>
  </div>
</div>
```

### Card with Form

```html
<div class="admin-card">
  <div class="admin-card-header">회원 등록</div>
  <div class="admin-card-body">
    <form>
      <div class="form-group">
        <label class="form-label required">이름</label>
        <input type="text" class="form-control">
      </div>
      <div class="form-group">
        <label class="form-label required">이메일</label>
        <input type="email" class="form-control">
      </div>
    </form>
  </div>
  <div class="admin-card-footer">
    <button class="btn btn-primary">등록</button>
    <button class="btn btn-secondary">취소</button>
  </div>
</div>
```

---

## Badges

### Basic Badge

```html
<span class="badge badge-primary">배지</span>
```

### Variants

```html
<span class="badge badge-primary">Primary</span>
<span class="badge badge-secondary">Secondary</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-warning">Warning</span>
<span class="badge badge-info">Info</span>
```

### Usage in Tables

```html
<td class="center">
  <span class="badge badge-success">활성</span>
</td>
<td class="center">
  <span class="badge badge-warning">대기</span>
</td>
```

### Status Badges

```html
<!-- 회원 상태 -->
<span class="badge badge-success">정상</span>
<span class="badge badge-warning">대기</span>
<span class="badge badge-info">휴면</span>

<!-- 결제 상태 -->
<span class="badge badge-success">완료</span>
<span class="badge badge-warning">대기</span>
<span class="badge badge-info">처리중</span>

<!-- 기부 상태 -->
<span class="badge badge-success">승인</span>
<span class="badge badge-warning">보류</span>
```

---

## Alerts

### Alert Types

```html
<!-- Success -->
<div class="alert alert-success">
  성공적으로 처리되었습니다.
</div>

<!-- Warning -->
<div class="alert alert-warning">
  주의가 필요한 사항입니다.
</div>

<!-- Error -->
<div class="alert alert-error">
  오류가 발생했습니다. 다시 시도해주세요.
</div>

<!-- Info -->
<div class="alert alert-info">
  참고 정보입니다.
</div>
```

### Alert Usage

```html
<!-- After form submission -->
<?php if($success): ?>
<div class="alert alert-success">
  회원 정보가 성공적으로 저장되었습니다.
</div>
<?php endif; ?>

<?php if($error): ?>
<div class="alert alert-error">
  <?php echo $error_message; ?>
</div>
<?php endif; ?>
```

---

## Pagination

### Basic Pagination

```html
<ul class="pagination">
  <li class="pagination-item">
    <a href="?page=1" class="pagination-link">«</a>
  </li>
  <li class="pagination-item">
    <a href="?page=1" class="pagination-link active">1</a>
  </li>
  <li class="pagination-item">
    <a href="?page=2" class="pagination-link">2</a>
  </li>
  <li class="pagination-item">
    <a href="?page=3" class="pagination-link">3</a>
  </li>
  <li class="pagination-item">
    <a href="?page=3" class="pagination-link">»</a>
  </li>
</ul>
```

### Gnuboard Pagination Integration

```php
<!-- Replace existing pagination HTML with: -->
<ul class="pagination">
  <?php echo get_paging($config['cf_write_pages'], $page, $total_page, '?page='); ?>
</ul>
```

---

## Layout Utilities

### Flexbox

```html
<!-- Horizontal layout -->
<div class="d-flex justify-between align-center gap-2">
  <span>Left</span>
  <span>Right</span>
</div>

<!-- Vertical layout -->
<div class="d-flex flex-column gap-3">
  <div>Item 1</div>
  <div>Item 2</div>
</div>

<!-- Centered content -->
<div class="d-flex justify-center align-center">
  <span>Centered</span>
</div>
```

### Spacing

```html
<!-- Margin top -->
<div class="mt-4">24px margin top</div>

<!-- Margin bottom -->
<div class="mb-3">16px margin bottom</div>

<!-- Padding -->
<div class="p-3">16px padding all sides</div>
```

### Text Utilities

```html
<!-- Alignment -->
<p class="text-left">왼쪽 정렬</p>
<p class="text-center">가운데 정렬</p>
<p class="text-right">오른쪽 정렬</p>

<!-- Colors -->
<p class="text-primary">Primary 색상</p>
<p class="text-warning">Warning 색상</p>
<p class="text-muted">Muted 색상</p>
```

---

## Common Patterns

### Search Form + Results Table

```html
<!-- Search form -->
<div class="admin-card mb-4">
  <div class="admin-card-header">회원 검색</div>
  <div class="admin-card-body">
    <form class="d-flex gap-2">
      <div class="form-group" style="flex: 1;">
        <input type="text" class="form-control" name="keyword" placeholder="이름 또는 이메일">
      </div>
      <button type="submit" class="btn btn-primary">검색</button>
    </form>
  </div>
</div>

<!-- Results table -->
<table class="admin-table">
  <thead>
    <tr>
      <th>번호</th>
      <th>이름</th>
      <th>이메일</th>
      <th class="center">상태</th>
      <th class="center">관리</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>홍길동</td>
      <td>hong@example.com</td>
      <td class="center"><span class="badge badge-success">활성</span></td>
      <td class="center">
        <button class="btn btn-primary btn-sm">수정</button>
        <button class="btn btn-warning btn-sm">삭제</button>
      </td>
    </tr>
  </tbody>
</table>
```

### Form with Validation

```html
<form id="memberForm">
  <div class="admin-card">
    <div class="admin-card-header">회원 정보</div>
    <div class="admin-card-body">
      <div class="form-group">
        <label class="form-label required">이름</label>
        <input type="text" class="form-control" name="name" required>
      </div>

      <div class="form-group">
        <label class="form-label required">이메일</label>
        <input type="email" class="form-control" name="email" required>
        <span class="form-error-message" style="display:none;">올바른 이메일을 입력하세요.</span>
      </div>

      <div class="form-group">
        <label class="form-label">전화번호</label>
        <input type="tel" class="form-control" name="phone">
        <span class="form-help-text">하이픈(-) 없이 입력하세요</span>
      </div>
    </div>

    <div class="admin-card-footer">
      <button type="submit" class="btn btn-primary">저장</button>
      <button type="button" class="btn btn-secondary" onclick="history.back()">취소</button>
    </div>
  </div>
</form>
```

---

## Best Practices

1. **Always use design system classes** - Never add inline styles
2. **Use semantic HTML** - `<button>` for buttons, `<label>` for labels
3. **Maintain accessibility** - Add proper labels, ARIA attributes
4. **Be consistent** - Use the same patterns throughout the admin
5. **Test responsiveness** - Check mobile/tablet views
6. **Validate forms** - Show clear error messages
7. **Use appropriate variants** - Primary for main actions, warning for deletions
