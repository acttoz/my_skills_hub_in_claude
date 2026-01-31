# admin.css 선택자 참조

## 변경 금지 선택자 (레이아웃)

아래 선택자들의 **레이아웃 속성**은 오버라이드하지 않습니다.

### 헤더 (#hd)

```css
/* 변경 금지 속성: position, width, height, padding, z-index */
#hd h1
#hd_top
#logo
#btn_gnb
#tnb, #tnb ul, #tnb li, #tnb a, #tnb button
```

### 네비게이션 (#gnb)

```css
/* 변경 금지 속성: position, width, height, padding-top, z-index */
#gnb
#gnb h2
#gnb .gnb_ul
#gnb .gnb_li button
#gnb .gnb_oparea
#gnb .on .gnb_oparea
#gnb.gnb_small
```

### 메인 컨테이너 (#container)

```css
/* 변경 금지 속성: padding, margin-top, min-width */
#container
#container.container-small
#container_wr
#container_title
.container_wr
.btn_fixed_top
```

### 푸터 (#ft)

```css
/* 변경 금지 속성: padding, text-align */
#ft
#ft p
.scroll_top
```

### 페이지네이션 (.pg_wrap)

```css
/* 변경 금지 속성: clear, margin, padding, text-align */
.pg_wrap
.pg
.pg_page, .pg_current
.pg_start, .pg_prev, .pg_next, .pg_end
```

## 스타일 오버라이드 가능 선택자

### 통계 영역

```css
.local_ov01, .local_ov     /* 통계 컨테이너 */
.ov_listall                /* 전체목록 링크 */
.btn_ov01                  /* 통계 버튼 */
.ov_txt                    /* 통계 텍스트 */
.ov_num                    /* 통계 숫자 */
```

### 검색 폼

```css
.local_sch01, .local_sch   /* 검색 폼 컨테이너 */
.local_sch select          /* 검색 셀렉트 */
.local_sch input[type="text"]  /* 검색 입력 */
.frm_input                 /* 공통 입력 필드 */
.btn_submit                /* 검색 버튼 */
```

### 설명 영역

```css
.local_desc01, .local_desc /* 설명 컨테이너 */
.local_desc p              /* 설명 텍스트 */
```

### 테이블

```css
.tbl_head01, .tbl_wrap     /* 테이블 컨테이너 */
.tbl_head01 table          /* 테이블 */
.tbl_head01 caption        /* 테이블 캡션 */
.tbl_head01 thead          /* 테이블 헤더 그룹 */
.tbl_head01 thead tr       /* 헤더 행 */
.tbl_head01 thead th       /* 헤더 셀 */
.tbl_head01 tbody          /* 테이블 바디 */
.tbl_head01 tbody tr       /* 바디 행 */
.tbl_head01 tbody td       /* 바디 셀 */
.tbl_head01 .bg0, .bg1     /* 행 배경 (홀짝) */
.tbl_head01 .empty_table   /* 빈 테이블 메시지 */

/* 테이블 셀 클래스 */
.td_chk                    /* 체크박스 셀 */
.td_num                    /* 번호 셀 */
.td_mng                    /* 관리 셀 */
.td_mng_s                  /* 작은 관리 셀 */
.td_mbname                 /* 회원명 셀 */
.td_tel                    /* 전화번호 셀 */
.td_date                   /* 날짜 셀 */
.td_left                   /* 좌측 정렬 셀 */
.td_center                 /* 중앙 정렬 셀 */
```

### 폼 테이블

```css
.tbl_frm01                 /* 폼 테이블 컨테이너 */
.tbl_frm01 table           /* 폼 테이블 */
.tbl_frm01 th              /* 폼 헤더 셀 (라벨) */
.tbl_frm01 td              /* 폼 데이터 셀 */
```

### 버튼

```css
.btn                       /* 공통 버튼 */
.btn_01                    /* Primary 버튼 (회원추가 등) */
.btn_02                    /* Secondary 버튼 (선택삭제 등) */
.btn_03                    /* 작은 버튼 (수정 등) */
```

### 필터/라디오 영역

```css
input[type="radio"]        /* 라디오 버튼 */
input[type="checkbox"]     /* 체크박스 */
strong                     /* 필터 레이블 */
```

### 섹션 타이틀

```css
#container_wr h2           /* 섹션 제목 */
#container_title           /* 페이지 제목 (fixed) */
```

## 관리자 페이지별 주요 요소

### member_list_bri.php (회원관리)

| 요소 | 선택자 |
|------|--------|
| 통계 영역 | `.local_ov01` |
| 검색 폼 | `#fsearch.local_sch01` |
| 설명 영역 | `.local_desc01` |
| 회원 테이블 | `.tbl_head01` |
| 버튼 영역 | `.btn_fixed_top` |
| 페이지네이션 | `.pg_wrap` |

### orderlist_bri.php (기부내역)

| 요소 | 선택자 |
|------|--------|
| 통계 영역 | `.local_ov01` |
| 검색 폼 | `.local_sch01` |
| 필터 영역 | 라디오 그룹 (기부상태, 결제수단) |
| 날짜 선택 | 날짜 입력 + 빠른선택 버튼 |
| 기부 테이블 | `.tbl_head01` (2행 헤더) |
| 페이지네이션 | `.pg_wrap` |

### orderform_bri.php (기부내역 수정)

| 요소 | 선택자 |
|------|--------|
| 상단 버튼 | `.btn_fixed_top` |
| 섹션 제목 | `h2` |
| 기부자정보 테이블 | `.tbl_frm01` |
| 결제정보 테이블 | `.tbl_frm01` |

## 오버라이드 우선순위

스타일 오버라이드 시 선택자 특이성(specificity)을 고려합니다.

```css
/* 낮은 특이성 - 일반 요소 */
.btn { }

/* 중간 특이성 - 복합 선택자 */
.tbl_head01 thead th { }

/* 높은 특이성 - ID 포함 */
#container_wr .tbl_head01 { }

/* 최고 특이성 - 필요시에만 */
#container_wr .tbl_head01 thead th { }
```

## 오버라이드 예제

### 테이블 스타일 오버라이드

```css
/* 기존 admin.css - 레이아웃만 정의 */
.tbl_head01 { }

/* 오버라이드 CSS - 시각적 스타일 추가 */
.tbl_head01 {
    background: var(--cwnu-white);
    border-radius: var(--cwnu-radius-lg);
    box-shadow: var(--cwnu-shadow-card);
    overflow: hidden;
}

.tbl_head01 thead th {
    background: var(--cwnu-primary-bg);
    color: var(--cwnu-primary-01);
    font-weight: 800;
}
```

### 버튼 스타일 오버라이드

```css
/* 기존 - 기본 스타일 */
.btn { }

/* 오버라이드 - Figma 디자인 적용 */
.btn.btn_01 {
    background: var(--cwnu-primary-01);
    color: var(--cwnu-white);
    border: 1px solid var(--cwnu-primary-01);
    border-radius: var(--cwnu-radius-full);
    font-family: var(--cwnu-font-body);
    font-weight: 800;
    font-size: 16px;
    line-height: 1.5;
}
```
