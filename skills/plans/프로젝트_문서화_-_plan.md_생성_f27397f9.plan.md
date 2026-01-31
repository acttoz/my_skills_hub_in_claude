---
name: 프로젝트 문서화 - plan.md 생성
overview: 프로젝트의 성격, 기능, 목적을 상세히 정리한 plan.md 문서를 생성합니다.
todos:
  - id: analyze-code
    content: 제공된 파일들을 분석하여 프로젝트의 전체 구조와 기능 파악
    status: completed
  - id: create-document
    content: plan.md 파일 생성 및 프로젝트 문서 작성
    status: completed
---

# 프로젝트 문서화 계획

## 작업 개요

`sub/year.php`, `skin/board/calendar/list.skin.php`, `skin/board/calendar/write.skin.php` 파일과 관련 코드를 분석하여 프로젝트의 성격, 기능, 목적을 상세히 정리한 `plan.md` 문서를 생성합니다.

## 문서 구성

### 1. 프로젝트 개요

- 프로젝트명: 강의 로그 관리 시스템 (Lecture Log Management System)
- 기반 프레임워크: 그누보드 5.x (Grunuboard)
- 개발 환경: PHP 8.1, MySQL, Docker
- 목적: 강의 일정 및 수강료 관리, 통계 분석

### 2. 주요 기능

- 강의 일정 관리 (캘린더 뷰)
- 강의 정보 입력/수정/조회
- 통계 기능 (일별, 주별, 월별, 연간)
- 강의종류 관리
- 입금 상태 관리
- 사용자별 데이터 필터링

### 3. 데이터베이스 구조

- `g5_write_calendar` 테이블 구조
- 각 필드(wr_1~wr_10)의 용도 설명
- `g5_lecture_categories` 테이블 (강의종류 관리)

### 4. 주요 파일 및 기능 설명

- `skin/board/calendar/list.skin.php`: 캘린더 뷰 (FullCalendar)
- `skin/board/calendar/write.skin.php`: 강의 입력/수정 폼
- `skin/board/calendar/view.skin.php`: 강의 상세 보기
- `sub/year.php`: 연간 통계 페이지 (Google Charts)
- `bbs/calendar_ajax.php`: AJAX 이벤트 로드
- `bbs/lecture_category_list.php`: 강의종류 목록 API

### 5. 사용자 권한 및 보안

- 관리자 vs 일반 사용자 권한 차이
- 데이터 필터링 로직
- 로그인 필수 기능

### 6. 기술 스택

- 백엔드: PHP 8.1
- 프론트엔드: JavaScript, FullCalendar, Google Charts
- 데이터베이스: MySQL
- 프레임워크: 그누보드 5.x

### 7. 데이터 흐름도

- 강의 등록 프로세스
- 통계 계산 로직
- 캘린더 이벤트 로드 프로세스

## 구현 세부사항

### 문서 작성 내용

1. **프로젝트 소개**: 시스템의 목적과 사용 대상
2. **기능 상세 설명**: 각 기능별 상세 설명
3. **데이터 구조**: 테이블 구조와 필드 설명
4. **파일 구조**: 주요 파일의 역할과 위치
5. **사용자 인터페이스**: 주요 화면 설명
6. **통계 기능**: 통계 계산 방식과 표시 방법
7. **보안 및 권한**: 접근 제어 메커니즘

### 참고 파일

- `sub/year.php`: 연간 통계 페이지
- `skin/board/calendar/list.skin.php`: 캘린더 목록 뷰
- `skin/board/calendar/write.skin.php`: 강의 작성/수정 폼
- `bbs/calendar_ajax.php`: AJAX 이벤트 로드
- `bbs/lecture_category_list.php`: 강의종류 API
- `data/dbconfig.php`: 데이터베이스 설정

## 예상 결과물

`plan.md` 파일에 다음 내용이 포함됩니다:

- 프로젝트 개요 및 목적
- 주요 기능 상세 설명
- 데이터베이스 스키마 설명
- 주요 파일 구조 및 역할
- 사용자 권한 및 보안 정책
- 기술 스택 및 아키텍처
- 데이터 흐름도 (Mermaid 다이어그램)
- 향후 개선 방향 (선택사항)