---
name: 강의종류 통계 추가
overview: sub/year.php 파일에 강의종류별 통계 차트를 추가합니다. 왼쪽 패널의 월별 통계 테이블 아래에 강의종류별 건수 차트를 배치합니다.
todos:
  - id: add_category_query
    content: 강의종류별 통계 SQL 쿼리 추가 및 데이터 처리 로직 구현
    status: completed
  - id: add_category_chart_html
    content: 왼쪽 패널에 강의종류 차트 HTML 구조 추가
    status: completed
    dependencies:
      - add_category_query
  - id: add_category_chart_js
    content: Google Charts를 사용한 강의종류별 건수 차트 JavaScript 구현
    status: completed
    dependencies:
      - add_category_chart_html
  - id: verify_styling
    content: CSS 스타일 확인 및 필요시 추가
    status: completed
    dependencies:
      - add_category_chart_html
---

# 강의종류 통계 추가

## 개요

`sub/year.php` 파일에 강의종류별 통계 차트를 추가합니다. 사용자 선택에 따라 왼쪽 패널에 강의종류별 건수 차트만 추가합니다.

## 구현 내용

### 1. 데이터 조회 쿼리 추가

- `sub/year.php`의 기존 월별 통계 쿼리 아래에 강의종류별 통계 쿼리 추가
- `wr_8` 컬럼을 기준으로 강의종류별 건수 집계
- 연도 필터링 및 작성자 필터링 적용 (관리자가 아닌 경우)
- SQL 쿼리:
  ```sql
  SELECT 
      wr_8 as category,
      COUNT(*) as lecture_count
  FROM g5_write_calendar 
  WHERE YEAR(wr_1) = '$year' AND wr_1 != '' AND wr_8 != ''{$author_filter}
  GROUP BY wr_8
  ORDER BY lecture_count DESC, wr_8 ASC
  ```


### 2. PHP 데이터 처리

- 강의종류별 통계 데이터를 배열로 저장
- 차트 데이터 생성용 배열 준비

### 3. HTML 구조 추가

- 왼쪽 패널(`.left-panel`) 내부, 월별 통계 테이블 아래에 강의종류 차트 섹션 추가
- 기존 `.chart1` 스타일과 유사한 구조 사용
- 차트 컨테이너 div 추가: `<div id="chart_div_category"></div>`

### 4. JavaScript 차트 구현

- Google Charts를 사용하여 강의종류별 건수 차트 생성
- 기존 차트들과 동일한 스타일 적용
- Column Chart 또는 Pie Chart 중 선택 (Column Chart 권장 - 기존 차트와 일관성)
- 차트 옵션:
  - 색상: 기존 차트들과 구분되는 색상 사용
  - 범례: 강의종류명 표시
  - 정렬: 건수 내림차순

### 5. CSS 스타일 (필요시)

- `sub/year.css`에 추가 스타일이 필요한지 확인
- 기존 `.chart1` 스타일이 재사용 가능한지 확인

## 파일 수정

- `sub/year.php`: 강의종류 통계 쿼리, 데이터 처리, HTML, JavaScript 추가
- `sub/year.css`: 필요시 스타일 추가 (기존 스타일 재사용 가능하면 수정 불필요)

## 참고사항

- 기존 코드의 `$author_filter` 변수를 재사용하여 작성자 필터링 유지
- 빈 강의종류(`wr_8 = ''`)는 제외
- 강의종류가 없는 경우 빈 차트 표시 또는 메시지 표시