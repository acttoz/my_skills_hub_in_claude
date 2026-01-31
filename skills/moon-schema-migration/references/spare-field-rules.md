# 여분 필드 규칙 (Spare Field Rules)

그누보드(Gnuboard) 및 관련 테이블의 여분 필드 패턴을 정의합니다.

## 테이블별 여분 필드 패턴

| 테이블 유형 | 테이블 패턴 | 여분 필드 패턴 | 기본 필드 수 | 예시 |
|-------------|-------------|----------------|--------------|------|
| 회원 (member) | `g5_member` | `mb1` ~ `mb10` | 10개 | mb1, mb2, ..., mb10 |
| 게시글 (write) | `g5_write_*` | `wr1` ~ `wr10` | 10개 | wr1, wr2, ..., wr10 |
| 주문 (order) | `g5_shop_order` | `od1` ~ `od10` | 10개 | od1, od2, ..., od10 |
| 상품 (item) | `g5_shop_item` | `it1` ~ `it10` | 10개 | it1, it2, ..., it10 |
| 장바구니 (cart) | `g5_shop_cart` | `ct1` ~ `ct10` | 10개 | ct1, ct2, ..., ct10 |

## 여분 필드 확장 규칙

### 기본 여분 필드가 부족한 경우

10개의 기본 여분 필드가 모두 사용된 경우, 새 컬럼을 추가합니다:

```sql
-- 회원 테이블 예시: mb11 ~ mb20 추가
ALTER TABLE g5_member ADD COLUMN mb11 TEXT;
ALTER TABLE g5_member ADD COLUMN mb12 TEXT;
-- ...

-- 게시글 테이블 예시: wr11 ~ wr20 추가
ALTER TABLE g5_write_board ADD COLUMN wr11 TEXT;
ALTER TABLE g5_write_board ADD COLUMN wr12 TEXT;
-- ...
```

### 데이터 타입 선택 기준

| 원본 타입 | 추가 컬럼 타입 | 설명 |
|-----------|----------------|------|
| varchar(n) where n ≤ 255 | TEXT | 안전하게 TEXT 사용 |
| varchar(n) where n > 255 | TEXT | TEXT 사용 |
| text, longtext | TEXT | 동일 타입 유지 |
| int, bigint | TEXT | TEXT로 저장 후 캐스팅 |
| date, datetime | TEXT | 문자열로 저장 |
| char(n) | TEXT | TEXT 사용 |

### 여분 필드 사용 우선순위

1. **빈 여분 필드 우선**: 이미 값이 없는(NULL 또는 '') 여분 필드 먼저 사용
2. **순차 사용**: mb1 → mb2 → mb3 ... 순서대로 사용
3. **확장 필드**: 기본 10개 초과 시 mb11, mb12... 순차 추가

## 여분 필드 매핑 예시

### 원본: member_info → 대상: g5_member

```sql
-- 매칭되지 않는 원본 필드들을 여분 필드에 매핑
INSERT INTO g5_member (
    mb_id, mb_name, mb_email, mb_hp,
    -- 여분 필드 매핑
    mb1,               -- mem_company_name
    mb2,               -- mem_company_part
    mb3,               -- birth_gubun (양력/음력)
    mb4,               -- mem_company_tel
    mb5,               -- mem_company_fax
    mb6,               -- mem_company_addr
    mb7,               -- mem_relation_type
    mb8,               -- gradu_type
    mb9,               -- gradu_info_enter (입학년도)
    mb10               -- gradu_info_out (졸업년도)
)
SELECT 
    mem_id, mem_name, mem_email, mem_hp,
    mem_company_name, mem_company_part, birth_gubun,
    mem_company_tel, mem_company_fax, mem_company_addr,
    mem_relation_type, gradu_type, gradu_info_enter, gradu_info_out
FROM member_info;
```

### 10개 초과 시 컬럼 추가 후 매핑

```sql
-- 먼저 컬럼 추가
ALTER TABLE g5_member ADD COLUMN mb11 TEXT COMMENT '졸업 학과명';
ALTER TABLE g5_member ADD COLUMN mb12 TEXT COMMENT '졸업 대학명';
ALTER TABLE g5_member ADD COLUMN mb13 TEXT COMMENT '조직 정보';

-- 그 후 마이그레이션
INSERT INTO g5_member (..., mb11, mb12, mb13)
SELECT ..., gradu_info_part, gradu_info_college, orga_info
FROM member_info;
```

## 여분 필드 용도 문서화

마이그레이션 후 반드시 `db_migration/result/{table_name}.md`에 여분 필드 용도를 문서화:

```markdown
## 여분 필드 사용 내역

| 여분 필드 | 원본 필드 | 설명 |
|-----------|-----------|------|
| mb1 | mem_company_name | 회사명 |
| mb2 | mem_company_part | 부서 |
| mb3 | birth_gubun | 양력/음력 구분 |
```

## 주의사항

1. **기존 데이터 확인**: 여분 필드에 기존 데이터가 있는지 반드시 확인
2. **백업 필수**: 마이그레이션 전 대상 테이블 백업
3. **COMMENT 활용**: ALTER TABLE 시 COMMENT로 원본 필드 정보 기록
4. **중복 방지**: 동일 데이터 재삽입 방지를 위한 조건 확인
