### HTTP API, REST API 
    HTTP API를 사용하면 REST API보다 지연 시간이 짧고 비용이 저렴한 RESTful API를 생성할 수 있음.
    둘 차이점은 HTTP API는 OIDC 및 OAuth 2.0 인증을 지원하는지 차이.
    
### API Gateway Lambda 프록시 통합
    Lambda 프록시 통합을 사용하면 클라이언트가 백엔드에서 단일 Lambda 함수를 호출할 수 있다.

### Lambda <-> API Gateway
- '열기'는 API 주소만 있으면 누구나 호출 가능 (public)
- AmazonAPIGatewayInvokeFullAccess (권한 필요)