# 관리자 페이지 UI 구현 규칙

## 📌 기본 원칙
- 레퍼런스의 기능이나 설명 부분을 UI로 구현하면 안됨
- 레퍼런스의 디자인은 무시하고 텍스트와 위치 레이아웃만 동일하게 구현

## 1. 스타일시트 사용 규칙
- **기존 CSS 파일 사용**: `adm_cw/css/admin.css`의 기존 컴포넌트를 우선 사용
- **스타일 추가 위치**: 필요한 스타일은 반드시 `adm_cw/css/admin.css` 파일에만 추가
- **인라인 스타일 금지**: HTML에 인라인 스타일(`style=""`) 사용 금지 (테이블 컬럼 너비 제외)

## 2. HTML 구조 규칙
- 다른 관리자 페이지와 태그 구조, 선택자 등 요소들 통일해서 구현
- 참고 파일:
  - `adm_cw/member_list_bri.php`
  - `adm_cw/shop_admin/orderlist.php`

## 3. 톤앤매너 유지
- 기존 관리자 페이지의 디자인 톤앤매너를 그대로 유지
- 색상, 간격, 폰트, 버튼 스타일 등 일관성 유지

## 4. 표 수정 규칙
- 열에 들어갈 내용을 감안하여 여유있게 셀 너비 적절히 조절
- 권장 너비:
  - 체크박스: 40px
  - 번호: 60px
  - 상태/플래그: 80px
  - 날짜: 100px
  - 전화번호: 130px
  - 이름/제목: flex 또는 min-width
  - 버튼: 80~100px

## 5. 공통 클래스 패턴

### 배지(Badge)
```html
<span class="badge badge-primary">Primary</span>
<span class="badge badge-secondary">Secondary</span>
<span class="badge badge-info">Info</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-warning">Warning</span>
```

### 버튼
```html
<button type="submit" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<a href="#" class="btn btn-sm btn-primary">Small</a>
```

### 폼 컨트롤
```html
<select class="form-control" style="width:auto;">
<input type="text" class="form-control" style="width:200px;">
```

### 레이아웃
```html
<div class="d-flex align-center gap-2">
<div class="text-center">
<div class="text-muted">
```
