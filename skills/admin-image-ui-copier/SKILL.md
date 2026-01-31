---
name: admin-image-ui-copier
description: "이미지와 레이아웃이 다른 관리자 페이지 HTML을 수정합니다. adm_cw/css/admin.css의 클래스를 활용하고, 필요시 새 스타일을 추가합니다."
---

# Admin Image UI Copier

참조 이미지를 분석하여 관리자 페이지의 **레이아웃과 구조**를 이미지와 동일하게 HTML을 수정합니다.

## 핵심 원칙

1. **레이아웃만 수정** - 기능 구현 X, 레이아웃/구조만 맞춤
2. **admin.css 클래스 활용** - `adm_cw/css/admin.css`의 기존 클래스 사용
3. **필요시 스타일 추가** - admin.css에 없는 스타일은 추가
4. **인라인 스타일 금지** - 테이블 컬럼 너비 외 인라인 스타일 사용 안 함

## Workflow

### Step 1: 이미지 분석
1. 레이아웃 구조 파악 (컬럼, 행, 섹션)
2. 요소 위치 및 계층 구조 확인
3. 테이블 컬럼 순서/구성 확인

### Step 2: 대상 파일 확인
1. 수정할 PHP 파일 확인
2. 현재 HTML 구조와 이미지 비교
3. 차이점 목록화

### Step 3: HTML 수정
admin.css의 기존 클래스를 활용하여 HTML 수정

### Step 4: 스타일 추가 (필요시)
admin.css에 필요한 클래스가 없으면 `adm_cw/css/admin.css`에 추가

## admin.css 주요 클래스

### 레이아웃 영역
```css
.local_ov, .local_ov01   /* 상단 통계/버튼 영역 */
.local_sch, .local_sch01 /* 검색 폼 영역 */
.local_sch03             /* 복합 검색 영역 */
.local_desc, .local_desc01 /* 안내문 영역 */
.btn_fixed_top           /* 상단 고정 버튼 */
```

### 테이블
```css
.tbl_wrap, .tbl_head01   /* 테이블 래퍼 */
.td_chk                  /* 체크박스 셀 */
.td_num                  /* 숫자 셀 (우측 정렬) */
.td_mng                  /* 관리 버튼 셀 */
.td_mbname               /* 이름 셀 (좌측 정렬) */
.td_tel                  /* 전화번호 셀 */
.td_date                 /* 날짜 셀 */
.td_center               /* 중앙 정렬 */
.empty_table             /* 빈 테이블 */
```

### 폼
```css
.tbl_frm01               /* 폼 테이블 */
.frm_input               /* 입력 필드 */
.frm_radio_inline        /* 라디오 버튼 인라인 */
```

### 버튼
```css
.btn                     /* 기본 버튼 */
.btn_01, .btn-primary    /* Primary 버튼 (파란색) */
.btn_02, .btn-secondary  /* Secondary 버튼 (아웃라인) */
.btn_03                  /* 작은 버튼 */
.btn_submit              /* 제출 버튼 (그라데이션) */
.btn_sch2                /* 검색 버튼 */
.btn-danger              /* 위험 버튼 (빨간색) */
.btn-success             /* 성공 버튼 (초록색) */
.btn-excel               /* 엑셀 버튼 */
```

### 배지
```css
.badge                   /* 기본 배지 */
.badge-primary           /* Primary 배지 */
.badge-secondary         /* Secondary 배지 */
.badge-success           /* 성공 배지 */
.badge-danger            /* 위험 배지 */
.badge-warning           /* 경고 배지 */
.badge-info              /* 정보 배지 */
.badge-light             /* 라이트 배지 */
.badge-outline           /* 아웃라인 배지 */
```

### 통계 배지
```css
.btn_ov01                /* 통계 배지 컨테이너 */
.ov_txt                  /* 통계 라벨 텍스트 */
.ov_num                  /* 통계 숫자 */
.btn_ov02                /* 버튼 그룹 */
```

### 기타
```css
.section-title           /* 섹션 타이틀 */
.pg_wrap, .pg            /* 페이지네이션 */
.modal-overlay           /* 모달 오버레이 */
.modal-content           /* 모달 콘텐츠 */
```

## CSS 변수 (Design Tokens)

```css
/* 색상 */
--cwnu-primary-1: #003179;     /* 메인 파란색 */
--cwnu-primary-2: #0046ac;     /* 밝은 파란색 */
--cwnu-primary-bg: #f1f3f7;    /* 배경색 */
--cwnu-white: #ffffff;
--cwnu-gray-100: #f9f9f9;
--cwnu-gray-200: #dddddd;
--cwnu-warning: #ff0004;

/* 간격 */
--cwnu-spacing-xs: 4px;
--cwnu-spacing-sm: 8px;
--cwnu-spacing-md: 12px;
--cwnu-spacing-lg: 16px;
--cwnu-spacing-xl: 20px;

/* gap */
--cwnu-gap-sm: 4px;
--cwnu-gap-md: 8px;
--cwnu-gap-lg: 10px;

/* Border Radius */
--cwnu-radius-sm: 4px;
--cwnu-radius-md: 8px;
--cwnu-radius-lg: 12px;
--cwnu-radius-full: 1000px;

/* 폼 높이 */
--cwnu-form-height: 40px;
```

## 테이블 컬럼 너비 가이드

| 컬럼 타입 | 권장 너비 |
|----------|----------|
| 체크박스 | `width:40px;` |
| 번호/ID | `width:60px;` |
| 상태/Y/N | `width:80px;` |
| 날짜 | `width:100px;` |
| 전화번호 | `width:130px;` |
| 이름/제목 | flex (고정 X) |
| 버튼 영역 | `width:80px;` ~ `width:100px;` |

## 완료 체크리스트

- [ ] 레이아웃이 이미지와 동일한가?
- [ ] 컬럼 순서가 일치하는가?
- [ ] admin.css 기존 클래스를 활용했는가?
- [ ] 인라인 스타일 없이 작성했는가? (컬럼 너비 제외)
- [ ] 새 스타일이 필요하면 admin.css에 추가했는가?
