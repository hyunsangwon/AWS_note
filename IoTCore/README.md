## AWS IoT Core ?

-   AWS IoT Core는 서버를 프로비저닝하거나 관리할 필요 없이 IoT 디바이스를 AWS 클라우드에 연결할 수 있게 해 줌.

### 특징

-   최고 최대 128KB(킬로바이트) 크기의 메시지를 송신 및 수신할 수 있음.

### 토픽

-   publishing Client와 Subscribing Client간의 메세지를 주고받는 메시지 통로
-   토픽 필터
    필터 # (하위 토픽 구독)
    ex) sensor/#  
     sensor/temp  
     sensor/temp/room1  
    필터 + (연관된 토픽 구독)
    ex) sensor/+/room1  
     sensor/temp/room1  
     sensor/moisture/room1

### 규칙

-   규칙?
    규칙은 웹으로 비유하자면 API 서버이다.  
    디바이스는 규칙에서 정의한 주소로 데이터를 보낸다.  
    Lambda,DynamoDB 등 다른 서비스에 연결할 수 있다.  
    쿼리문이 존재하고 DB SQL문하고 유사하다.

-   규칙 쿼리 문법
    '''
    SELECT <Attribute> FROM <Topic Filter> WHERE <Condition>
    '''
-   규칙 쿼리 문법 예시 (온도가 30도 이상인 데이터만 수신)
    '''
    SELECT
    CAST(topic(2) AS DECIMAL) AS device_id,
    temperature AS reported_temperature,
    30 AS max_temperature
    FROM 'device/+/data' WHERE temperature > 30
    '''
    topic(number) 함수는 from절에서 정의한 토픽 필터 인덱스 값 호출  
    where 조건으로 온도가 30도인 데이터만 받게 필터 가능  
    ex) device/50/data 이라는 토픽이 있다면 topic(1)은 data가 나옴.

### 보안

-   AWS IoT 와 상호 작용하려면 연결된 각 디바이스 또는 클라이언트에는 자격 증명이 있어야 함. (즉, 디바이스 안에 Key가 있어야 함.)
-   AWS IoT 에서 송수신하는 모든 트래픽은 TLS (전송 계층 보안) 를 통해 안전하게 전송.
-   AWS 클라우드 보안 메커니즘은 AWS IoT와 기타 AWS 서비스 간에 이동하는 데이터를 보호.

#### 요금

-   최소 요금, 의무 서비스 사용량 없음.
-   연결 시간과 메시징 으로 요금을 부과.
-   연결 요금
    0.096 USD(연결 100만 분당)  
     ex) 연중무휴 24시간 연결 시 1년에 디바이스당 0.050 USD를 지불.(연결 1개 _ 0.096 USD/연결 1,000,000분 _ 525,600분/년)

-   메세징
    메시지 100만 개당 1.20 USD  
    메시지가 40억 개를 넘으면 100만 개당 0.96  
    메시지 50억 개 초과 100만 개당 0.84  
    메시지는 5KB 단위로 측정 ex) 8KB 메시지는 메시지 2개로 측정
