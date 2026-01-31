---
name: restore-staggered-product-grid-links
overview: Fix the product lineup section so left and right product cards are vertically staggered again while keeping the new board links.
todos:
  - id: fix-desktop-nth-child
    content: Update nth-child selectors in theme/basic/css/main.css so staggered layout is based on products-grid direct children and works with anchor-wrapped product items.
    status: completed
  - id: verify-mobile-layout
    content: Check theme/basic/css/main_mobile.css section7 styles to ensure mobile single-column layout remains correct after desktop CSS changes.
    status: completed
  - id: visual-check-section7
    content: Visually verify section7 in the browser to confirm left/right product cards are staggered again and hover/link behaviors work as expected.
    status: completed
isProject: false
---

### 목표

- `section7`의 제품 카드들이 링크 추가 이후 모두 같은 수직 위치로 정렬된 문제를 해결하고, **좌/우 카드가 다시 계단식(교차) 높이**를 가지도록 복구합니다.
- 기존에 추가한 `autofilms` 게시판 링크 구조는 그대로 유지합니다.

### 현재 구조 및 문제 원인

- 마크업: `[theme/basic/index.php]`의 `section7` 내 제품 그리드는 다음 구조입니다.

```html
<div class="products-grid">
    <a href="..."><div class="product-item">...</div></a>
    <a href="..."><div class="product-item">...</div></a>
    ...
</div>
```

- 스타일: `[theme/basic/css/main.css]`에서 그리드와 카드 레이아웃을 이렇게 정의합니다.

```css
.section7 .products-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 40px;
}

.section7 .product-item:nth-child(odd) {
    margin-bottom: 200px;
}

.section7 .product-item:nth-child(even) {
    margin-top: 200px;
}
```

- 원래는 `.products-grid`의 **직접 자식**이 `.product-item`였기 때문에 `nth-child`가 정상적으로 동작해 카드 높이가 교차되었습니다.
- 링크 추가 후 구조가 `a > .product-item`로 바뀌면서, `.product-item`은 그리드의 **손자 요소**가 되었고, `nth-child` 계산 대상에서 빠져 **모든 카드가 같은 높이**에 놓이게 되었습니다.

### 수정 방향

- 마크업은 유지하고, **CSS 셀렉터만 수정**해서 `nth-child`가 다시 그리드 칸 기준으로 동작하게 합니다.
- 즉, `.products-grid`의 직접 자식(현재는 `<a>`)에 대해 `nth-child`를 적용하고, 그 안의 `.product-item`에 margin을 주는 방식으로 변경합니다.

### 구체적인 변경 계획

1. **데스크톱 레이아웃 CSS 수정**
  - 파일: `[theme/basic/css/main.css]`
  - 아래 코드 블록을 찾습니다.

```css
.section7 .product-item:nth-child(odd) {
    margin-bottom: 200px;
}

.section7 .product-item:nth-child(even) {
    margin-top: 200px;
}
```

- 이를 다음과 같이 변경합니다.

```css
.section7 .products-grid > *:nth-child(odd) .product-item {
    margin-bottom: 200px;
}

.section7 .products-grid > *:nth-child(even) .product-item {
    margin-top: 200px;
}
```

- 이렇게 하면 `products-grid`의 각 칸(현재는 `<a>`)의 홀수/짝수 순서를 기준으로, 내부의 `.product-item`에 위/아래 margin이 적용되어 **좌우 카드가 다시 계단식으로 보이게** 됩니다.

1. **모바일 스타일 확인**
  - 파일: `[theme/basic/css/main_mobile.css]`
  - `.section7 .products-grid` 정의만 있고, `nth-child`를 이용한 수직 오프셋은 없으므로 **모바일 단일 컬럼에서는 변화가 없고**, 레이아웃이 깨지지 않는지만 확인합니다.
2. **시각 확인 및 미세 조정(선택)**
  - 프론트에서 `section7`을 확인해서, 링크 추가 전과 비슷하게 **교차 높이·간격(200px)이 자연스러운지** 체크합니다.
  - 필요하면 `margin-top`/`margin-bottom` 값(예: 180px, 220px 등)을 디자이너 피드백에 맞춰 소폭 조정할 수 있도록 합니다.

### TODO

- `fix-desktop-nth-child`
  - `[theme/basic/css/main.css]`에서 `nth-child` 셀렉터를 `products-grid`의 직접 자식 기준으로 수정하여 계단형 레이아웃을 복원한다.
- `verify-mobile-layout`
  - `[theme/basic/css/main_mobile.css]`의 `section7` 부분을 확인해 모바일 1열 레이아웃이 이상 없는지 검증한다.
- `visual-check-section7`
  - 메인 페이지의 `section7`을 브라우저에서 확인해 제품 카드 좌/우 교차 배치와 hover 효과가 의도대로 동작하는지 최종 검수한다.

