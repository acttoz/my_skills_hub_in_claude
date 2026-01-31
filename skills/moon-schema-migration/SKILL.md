---
name: schema-migration
description: "서로 다른 스키마의 테이블 간 데이터 마이그레이션을 자동화합니다. 원본/대상 테이블의 명세(spec)를 제공받아 필드 매핑 계획 작성, 마이그레이션 실행까지 수행합니다."
---

# Schema Migration Skill

서로 다른 스키마를 가진 테이블 간 데이터 마이그레이션을 자동화하는 스킬입니다.

## 트리거 조건

다음 키워드가 포함된 요청에서 이 스킬을 사용합니다:
- "테이블 마이그레이션"
- "스키마 마이그레이션"
- "데이터 이전"
- "테이블 데이터 복사"
- "DB 마이그레이션"

## 입력 요구사항

**두 테이블의 명세(spec)가 필요합니다:**

1. **원본 테이블 명세** - `db_migration/old/{source_table}.md` 또는 직접 제공
2. **대상 테이블 명세** - `db_migration/new/{target_table}.md` 또는 직접 제공

명세에는 다음 정보가 포함되어야 합니다:
- 컬럼명
- 데이터 타입
- NULL 허용 여부
- 키 정보 (PK, FK 등)
- **필드 설명/용도** (가장 중요 - 필드명만으로는 의미 파악 불가)

예시 입력:
```
원본: db_migration/old/member_info.md
대상: db_migration/new/g5_member.md
```

## 핵심 원칙

1. **명세 기반 매핑** - 필드명이 아닌 **필드 설명/용도**를 기준으로 매핑
2. **INSERT INTO SELECT 사용** - 동일 DB 내 마이그레이션은 가장 효율적인 방식
3. **여분 필드 활용** - 매칭되지 않는 필드는 여분 필드(mb1~mb10 등)에 매핑
4. **결과 문서화** - 마이그레이션 결과를 `db_migration/result/`에 기록

## Workflow

### Step 1: 명세 확인

제공된 원본/대상 테이블 명세 파일을 읽어 분석합니다.

```
- db_migration/old/{source_table}.md  → 원본 테이블 구조 및 필드 설명
- db_migration/new/{target_table}.md  → 대상 테이블 구조 및 필드 설명
```

명세가 없으면 사용자에게 요청:
> "마이그레이션을 진행하려면 원본 테이블과 대상 테이블의 명세가 필요합니다.
> 각 필드의 용도/설명이 포함된 명세를 제공해주세요."

### Step 2: 필드 매핑 (명세 기반)

**명세의 필드 설명을 기준으로** 매핑합니다. 필드명이 다르더라도 용도가 같으면 매핑.

#### 2.1 용도 기반 매칭 (핵심)

명세의 "설명" 컬럼을 비교하여 동일한 용도의 필드를 매핑:

| 원본 필드 | 원본 설명 | 대상 필드 | 대상 설명 | 매칭 |
|-----------|-----------|-----------|-----------|------|
| `mem_name` | 회원명 | `mb_name` | 이름 | O |
| `mem_email` | 이메일 | `mb_email` | 이메일 | O |
| `mem_hp` | 휴대폰 | `mb_hp` | 휴대폰번호 | O |
| `mem_company_name` | 회사명 | - | (해당 없음) | → 여분 필드 |

#### 2.2 타입 호환성 확인

| 원본 타입 | 대상 타입 | 호환 |
|-----------|-----------|------|
| varchar(n) | varchar(m) where m >= n | O |
| varchar | text | O |
| int | bigint | O |
| char | varchar | O |
| text | text | O |
| date | datetime | O (시간 부분 00:00:00) |
| datetime | date | O (시간 정보 손실) |

#### 2.3 계획 문서 생성

`db_migration/plan/{target_table}.md` 파일 생성:

```markdown
# {target_table} 마이그레이션 계획

## 테이블 정보

| 항목 | 원본 | 대상 |
|------|------|------|
| 테이블명 | {source_table} | {target_table} |
| 총 건수 | {source_count} | {target_count} |
| 컬럼 수 | {source_columns} | {target_columns} |

## 원본 테이블 구조

| 필드명 | 타입 | Null | Key | Default | 설명 |
|--------|------|------|-----|---------|------|
| ... | ... | ... | ... | ... | ... |

## 대상 테이블 구조

| 필드명 | 타입 | Null | Key | Default | 설명 |
|--------|------|------|-----|---------|------|
| ... | ... | ... | ... | ... | ... |

## 필드 매핑

### 직접 매핑 (매칭된 필드)

| 원본 필드 | 대상 필드 | 매핑 유형 | 타입 호환 | 비고 |
|-----------|-----------|-----------|-----------|------|
| mem_id | mb_id | 의미 매칭 | O | 회원 아이디 |
| mem_name | mb_name | 의미 매칭 | O | 이름 |
| ... | ... | ... | ... | ... |

### 여분 필드 매핑 (매칭 안 된 필드)

| 원본 필드 | 여분 필드 | 원본 타입 | 설명 |
|-----------|-----------|-----------|------|
| mem_company_name | mb1 | varchar(50) | 회사명 |
| mem_company_part | mb2 | varchar(50) | 부서 |
| ... | ... | ... | ... |

### 매핑 제외 필드

| 원본 필드 | 제외 사유 |
|-----------|-----------|
| ... | ... |

## 추가 필요 컬럼

여분 필드가 부족한 경우:

| 컬럼명 | 타입 | 원본 필드 | 설명 |
|--------|------|-----------|------|
| mb11 | TEXT | gradu_info_part | 졸업 학과명 |
| ... | ... | ... | ... |

## 마이그레이션 쿼리 (예정)

### ALTER TABLE (컬럼 추가)

```sql
-- 필요시 실행
ALTER TABLE {target_table} ADD COLUMN mb11 TEXT COMMENT 'gradu_info_part: 졸업 학과명';
```

### INSERT INTO SELECT

```sql
INSERT INTO {target_table} (
    mb_id, mb_name, mb_email, ...
    mb1, mb2, mb3, ...
)
SELECT 
    mem_id, mem_name, mem_email, ...
    mem_company_name, mem_company_part, ...
FROM {source_table}
WHERE NOT EXISTS (
    SELECT 1 FROM {target_table} WHERE mb_id = {source_table}.mem_id
);
```
```

### Step 3: 여분 필드 할당

매칭되지 않는 필드는 여분 필드에 할당합니다.

```
여분 필드 규칙:
- g5_member: mb1 ~ mb10
- g5_write_*: wr1 ~ wr10
- g5_shop_order: od1 ~ od10
- g5_shop_item: it1 ~ it10
```

### Step 4: 컬럼 추가 (필요 시)

여분 필드가 부족한 경우 ALTER TABLE로 컬럼 추가:

```sql
-- MCP execute_sql로 실행
ALTER TABLE {target_table} ADD COLUMN mb11 TEXT COMMENT '{원본_필드명}: {설명}';
ALTER TABLE {target_table} ADD COLUMN mb12 TEXT COMMENT '{원본_필드명}: {설명}';
```

### Step 5: 마이그레이션 쿼리 실행

```sql
-- 데이터 마이그레이션
INSERT INTO {target_table} (
    -- 매칭된 필드
    mb_id, mb_name, mb_email, mb_hp,
    -- 여분 필드
    mb1, mb2, mb3, mb4, mb5
)
SELECT 
    -- 원본 필드
    mem_id, mem_name, mem_email, mem_hp,
    -- 여분 필드에 매핑
    mem_company_name, mem_company_part, birth_gubun, mem_company_tel, mem_company_fax
FROM {source_table}
WHERE NOT EXISTS (
    SELECT 1 FROM {target_table} WHERE mb_id = {source_table}.mem_id
);
```

### Step 6: 검증

```sql
-- 원본 테이블 건수
SELECT COUNT(*) as source_count FROM {source_table};

-- 대상 테이블 건수 (마이그레이션 후)
SELECT COUNT(*) as target_count FROM {target_table};

-- 마이그레이션된 데이터 샘플 확인
SELECT * FROM {target_table} ORDER BY mb_datetime DESC LIMIT 5;
```

### Step 7: 결과 문서 생성

`db_migration/result/{target_table}.md` 파일 생성:

```markdown
# {target_table} 마이그레이션 결과

## 마이그레이션 정보

| 항목 | 값 |
|------|-----|
| 원본 테이블 | {source_table} |
| 대상 테이블 | {target_table} |
| 마이그레이션 일시 | {datetime} |
| 원본 건수 | {source_count} |
| 마이그레이션 건수 | {migrated_count} |
| 계획 문서 | db_migration/plan/{target_table}.md |

## 필드 매핑 요약

| 매핑 유형 | 필드 수 |
|-----------|---------|
| 직접 매핑 | {direct_count} |
| 여분 필드 | {spare_count} |
| 추가 컬럼 | {added_count} |
| 제외 | {excluded_count} |

## 여분 필드 사용 내역

| 여분 필드 | 원본 필드 | 원본 타입 | 설명 |
|-----------|-----------|-----------|------|
| mb1 | mem_company_name | varchar(50) | 회사명 |
| mb2 | mem_company_part | varchar(50) | 부서 |
| ... | ... | ... | ... |

## 추가된 컬럼

| 컬럼명 | 타입 | 원본 필드 | 설명 |
|--------|------|-----------|------|
| mb11 | TEXT | gradu_info_part | 졸업 학과명 |
| ... | ... | ... | ... |

## 실행된 쿼리

### ALTER TABLE (컬럼 추가)

```sql
ALTER TABLE {target_table} ADD COLUMN mb11 TEXT COMMENT 'gradu_info_part: 졸업 학과명';
```

### INSERT INTO SELECT (데이터 마이그레이션)

```sql
INSERT INTO {target_table} (...)
SELECT ... FROM {source_table};
```

## 검증 결과

| 검증 항목 | 결과 |
|-----------|------|
| 마이그레이션 건수 일치 | O/X |
| 샘플 데이터 확인 | O/X |
```

## MCP 사용법

### MySQL MCP 서버

```
Server: user-MySQL_Server_changwon_fund_db
Database: changwon_fund_db (단일 DB, DB 간 마이그레이션 미지원)
Tool: execute_sql
```

### 쿼리 실행 예시

```javascript
// 테이블 구조 확인
CallMcpTool({
  server: "user-MySQL_Server_changwon_fund_db",
  toolName: "execute_sql",
  arguments: { query: "DESCRIBE g5_member" }
})

// 샘플 데이터 확인
CallMcpTool({
  server: "user-MySQL_Server_changwon_fund_db",
  toolName: "execute_sql",
  arguments: { query: "SELECT * FROM member_info LIMIT 5" }
})

// 데이터 마이그레이션
CallMcpTool({
  server: "user-MySQL_Server_changwon_fund_db",
  toolName: "execute_sql",
  arguments: { query: "INSERT INTO g5_member (...) SELECT ... FROM member_info" }
})
```

## 체크리스트

### 명세 확인 (Step 1)
- [ ] 원본 테이블 명세 확인 (`db_migration/old/`)
- [ ] 대상 테이블 명세 확인 (`db_migration/new/`)
- [ ] 각 필드의 설명/용도가 명시되어 있는지 확인

### 매핑 계획 (Step 2)
- [ ] 용도 기반 필드 매핑 완료
- [ ] 여분 필드 할당 계획 작성
- [ ] 추가 컬럼 필요 여부 확인
- [ ] `db_migration/plan/{target_table}.md` 생성
- [ ] 마이그레이션 쿼리 작성

### 실행 단계 (Step 3-5)
- [ ] ALTER TABLE 실행 (필요 시)
- [ ] INSERT INTO SELECT 실행
- [ ] 건수 검증

### 완료 단계 (Step 6-7)
- [ ] 샘플 데이터 확인
- [ ] `db_migration/result/{target_table}.md` 생성

## 주의사항

1. **백업 필수**: 대상 테이블에 기존 데이터가 있다면 마이그레이션 전 백업
2. **중복 방지**: WHERE NOT EXISTS 조건으로 중복 삽입 방지
3. **트랜잭션**: 대량 데이터는 배치 단위로 처리 고려
4. **인코딩**: 원본/대상 테이블 문자셋 일치 확인 (UTF-8)
5. **NULL 처리**: 원본의 NULL 값이 대상 테이블 제약조건과 호환되는지 확인

## 폴더 구조

```
db_migration/
├── old/            # 원본 테이블 명세 (입력 - 사용자가 제공)
│   └── {source_table}.md
├── new/            # 대상 테이블 명세 (입력 - 사용자가 제공)
│   └── {target_table}.md
├── plan/           # 마이그레이션 계획 문서 (Step 2에서 생성)
│   └── {target_table}.md
└── result/         # 마이그레이션 결과 문서 (Step 7에서 생성)
    └── {target_table}.md
```

## 명세 파일 형식

원본/대상 테이블 명세는 다음 형식을 따릅니다:

```markdown
# {테이블명} 테이블 명세

## 기본 정보
- 테이블명: {table_name}
- 설명: {table_description}
- 레코드 수: {row_count} (선택사항)

## 컬럼 정보

| 컬럼명 | 타입 | NULL | 키 | 설명 |
|--------|------|------|-----|------|
| mem_id | varchar(20) | NO | PRI | 회원 아이디 |
| mem_name | varchar(100) | NO | | 회원명 |
| mem_email | varchar(50) | YES | | 이메일 주소 |
| mem_company_name | varchar(50) | YES | | 소속 회사명 |
| ... | ... | ... | ... | ... |
```

**필수 정보:**
- 컬럼명
- 데이터 타입
- **설명** (용도 파악을 위해 가장 중요)
