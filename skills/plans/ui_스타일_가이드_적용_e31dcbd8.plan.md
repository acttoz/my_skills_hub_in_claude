---
name: UI 스타일 가이드 적용
overview: UI.md에 정의된 디자인 가이드를 모든 파일에 적용하여 일관된 UI를 구현합니다.
todos:
  - id: add-fonts
    content: head.sub.php에 Pretendard 폰트 @font-face 선언 추가
    status: completed
  - id: update-default-css
    content: css/default.css에 UI.md 가이드 적용 (컬러, 폰트, 버튼, 카드, 간격, 보더, 그림자, 트랜지션)
    status: completed
  - id: update-calendar-css
    content: skin/board/calendar/style.css에 Primary Green 컬러 및 UI.md 가이드 적용
    status: completed
  - id: update-year-css
    content: sub/year.css에 Primary Green 컬러 및 UI.md 가이드 적용
    status: completed
  - id: update-header-footer
    content: head.php의 헤더 배경색을 Primary Green으로 변경
    status: completed
---

# UI 스타일 가이드 적용 계획

## 작업 범위

UI.md에 정의된 컬러 팔레트, 타이포그래피, 컴포넌트 스타일을 모든 파일에 적용합니다.

## 주요 변경 사항

### 1. 폰트 및 기본 스타일 ([head.sub.php](head.sub.php))

- Pretendard 폰트 @font-face 선언 추가 (UI.md 39-102줄 참조)
- `<head>` 섹션에 폰트 로드 코드 추가

### 2. 메인 CSS 파일 ([css/default.css](css/default.css))

- **폰트 패밀리**: 'Malgun Gothic', dotum → 'Pretendard' 우선 적용
- **컬러 팔레트 업데이트**:
- Primary Green (#2d5016) 적용: 버튼, 링크, 액센트 요소
- 배경색: White (#ffffff), Light Gray (#f5f5f5, #fafafa)
- 텍스트 색상: Dark Gray (#1a1a1a, #2d2d2d), Medium Gray (#666666, #808080)
- **버튼 스타일**:
- Primary Button: 배경 #2d5016, 텍스트 #ffffff, 패딩 14px 32px, border-radius 4px
- Secondary Button: 배경 white, 텍스트 #2d5016, 보더 1px solid #2d5016
- 호버 효과: 배경색 #3d6026, transition 0.3s ease
- **컨테이너 너비**: 1200px 유지 (UI.md 가이드에 맞춤)
- **간격**: 패딩/마진을 8px, 16px, 24px, 40-60px 단위로 정리
- **보더 라디우스**: 4px (버튼/입력), 8px (카드), 12px (모달)
- **박스 섀도우**: 0 2px 8px rgba(0,0,0,0.05) (카드), 0 4px 16px rgba(0,0,0,0.15) (호버)
- **트랜지션**: 모든 인터랙티브 요소에 0.3s ease 적용

### 3. 달력 게시판 스타일 ([skin/board/calendar/style.css](skin/board/calendar/style.css))

- Primary Green 컬러 적용
- 버튼 스타일을 UI.md 가이드에 맞게 수정
- 카드 스타일 적용 (border-radius 8px, padding 24px)
- 트랜지션 및 호버 효과 추가

### 4. 연간 통계 페이지 ([sub/year.css](sub/year.css))

- Primary Green (#2d5016) 컬러로 변경 (현재 #007bff 사용 중)
- 버튼 스타일을 UI.md Primary Button 스타일로 변경
- 카드 스타일 적용
- 폰트를 Pretendard로 변경

### 5. 헤더/푸터 ([head.php](head.php), [tail.php](tail.php))

- HTML 구조는 유지, 스타일은 default.css에서 관리
- 헤더 배경색을 Primary Green으로 변경 (현재 #212020)

### 6. 회원 관련 스킨 ([skin/member/basic/*.php](skin/member/basic/))

- HTML 구조는 유지
- 스타일은 default.css의 폼 스타일로 통일
- 버튼 클래스에 UI.md 가이드 적용

## 구현 세부사항

### 컬러 매핑

- 기존 파란색 계열 (#3a8afd, #007bff 등) → Primary Green (#2d5016)
- 호버 색상: #3d6026
- 배경: #ffffff, #f5f5f5
- 텍스트: #1a1a1a (주요), #666666 (보조)

### 컴포넌트 클래스

- `.btn-primary`: Primary Button 스타일
- `.btn-secondary`: Secondary Button 스타일
- `.card`: 카드 스타일 (border-radius 8px, padding 24px, shadow)

### 반응형

- 모바일 브레이크포인트: max-width: 768px
- 기존 반응형 스타일 유지하면서 UI.md 가이드 적용