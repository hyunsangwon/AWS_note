# AWS memo :pencil2:

AWS 서비스를 핵심만 간략하게 정리용도 입니다.

## VPC(Virtual Private Cloud)
- 논리적으로 격리된 사용자 전용 네트워크 구역
- AWS에서는 default VPC를 제공

## 서브넷
- VPC를 논리적으로 분리한 서브네트워크로 AWS 환경 내의 네트워크 최소 단위
- IGW (AWS 라우터)를 기준으로 Public 서브넷과 Private 서브넷으로 나뉨

## EC2
- AWS상의 가상 서버

## AMI(Amazon Machine Image)
- 즉시 사용이 가능한 상태의 OS 및 패키지 조합
- AWS 이외의 환경에서는 사용할 수 없기 때문에 온프레미스 환경에서는 사용할 수 없음
- AMI 가상화 타입으로 완전가상화인 HVM과 반가상화인 PV가 있고 HVM 성능이 더 좋다

## 보안그룹
