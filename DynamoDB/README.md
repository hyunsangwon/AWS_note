# DynamoDB study on 2019-11-25 :pencil2:

## 내가 느꼈던 DynamoDB
- RDBMS에 익숙해져서 처음에 매우 이해가 안갔음(몽고 디비를 했는데도 불구하고)
- Partition Key와 Sort Key를 잘 이해하면 쭉쭉 이해가 잘됨.
- 고급용어들은 아직도 이해가 잘 안감..
- 테이블 2-3개 만들어보고 쿼리 날려보고 인덱스 막 넣고 막 데이터 넣어보니 그제야 개념들이 이해가기 시작

## DynamoDB ?
- AWS에서 제공하는 NoSQL DB

## DynamoDB 특징
- RDS처럼 DB관리가 편하고, 더 좋은점은 오토스케일링도 해준다. (유지보수 불필요)
- 샤딩(DB를 분할하여 저장하는 방법)도 제공해준다.
- 쉽게 아는 데이터베이스 생성후 테이블 생성이 아닌 바로 테이블 생성! (테이블 단위로 관리)
- 한 테이블당 Partition Key(PK로 생각하자)가 존재 해야한다.
- Sort Key는 추가적으로 생성할 수 있고 Sort Key가 있어야 범위 관련 쿼리가 가능( **처음에 매우 당황 했던 개념..** )
- RDBMS에서 알던 row를 items라고 부르며 items 마다 다른 컬럼(Attribute)값을 가질 수 있음.
- Partition Key로는 equl 조회 밖에 못함!
- 다른 컬럼에 범위 쿼리를 작성하고 싶을때는 인덱스 작업이 필요하며 이를 Secondary Index라고 부름(아래에 이어서 정리)
- Read, Write 당 가격을 책정 Write가 가장 비싸므로 작업시 큰 데이터를 한번에 넣어야 함.(JSON 지원)
- 조회 방법은 크게 쿼리, get, scan 이 존재
- insert 할때 Partition Key,Sort Key로 지정된 컬럼은 무조건 데이터를 넣어야함 (Non-Null)
- 트랜잭션 처리보다 데이터를 넣고 읽는 작업에 유용

## DynamoDB Secondary Index
- 두가지 종류가 있는데 Global Secondary Index(GSI), Local Secondary Index(LSI)가 있음.
- GSI (Global Secondary Index)
1. GSI는 Partition Key와 Sort Key키를 또 지정해줘야함 (테이블 생성시 a 컬럼에 sort key를 했다면 index 추가시 Partition Key가 될 수 도있음.)
2. 인덱스 크기는 제약이 없고 별도의 쓰기,읽기 용량이 할당된다. (요금 따로라는 말이여~)
3. 삭제 가능
4. 테이블 생성후 생성 가능
5. GSI 는 언제나 eventual consistent read 가 적용
6. GSI는 날짜 관련 컬럼으로 하는것이 좋다.
- LSI (Local Secondary Index)
7. 테이블과 동일한 Partition Key
8. 삭제 불가능
9. 테이블 생성시 생성 가능

## DynamoDB 비용 :moneybag:
- 쓰기는 가장 비싼 작업!
- 테이블 삭제는 무료
- TTL(컴퓨터나 네트워크에서 데이터의 유효 기간을 나타내기 위한 방법)을 활용한 삭제는 무료
- Eventual Consistent Read 50% 저렴


## 참고 자료
 - https://www.slideshare.net/awskorea/nosql-elasticahe-dynamodb-aws-aws-devday2018
 - https://www.dynamodbguide.com/key-concepts/
 - http://pyrasis.com/book/TheArtOfAmazonWebServices/Chapter14
