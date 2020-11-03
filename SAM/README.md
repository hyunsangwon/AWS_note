# AWS SAM :pencil2:

## What is SAM?
- AWS Serverless Application Model (AWS SAM)는 오픈 소스 프레임워크
- 서버리스 애플리케이션 은(는) Lambda 기능, 이벤트 소스 및 기타 리소스를 사용하여 작업을 수행
- 쉽게 설명하여 Lambda 디버깅, 관리가 가능함 

## SAM 사용방법 (python, sam, docker가 설치 되어 있어야 한다.)
- python 설치
- pip install --user aws-sam-cli (SAM 설치)
- docker 설치 (window 경우 WSL2 설치)  (https://www.docker.com/products/docker-desktop)
- docker window 설치 전 WSL2 설치 방법 (https://www.44bits.io/ko/post/wsl2-install-and-basic-usage)
- aws cli 설치
- aws configure 설정
## SAM 주요 명령어
1. SAM 구성
- sam init --runtime python3.8 --name my-sls-app
2. 일회성 호출 만들기  
 2-1. 이벤트 없이
 - sam local invoke "HelloWorldFunction" --no-event  
 2-2. 이벤트 넣어서
 - sam local invoke "HelloWorldFunction" -e events/event.json
3. 업로드할 파일 zip으로 압축
4. 람다 소스 배포
- aws lambda update-function-code --function-name my-function --zip-file fileb://app.zip
5. 코드가 수정 되었다면 빌드!
-  sam build

## Debug 방법 :wrench:  
1. pip install ptvsd (원격 디버깅 라이브러리 설치)  
2. requirements.txt 편집  
ptvsd==4.1.4  
4. build 디렉토리 생성 (hello_world 아래)  
3. pip install -r ./requirements.txt -t hello_world\build  
4. 메인 함수에 아래 코드 추가  
```
import ptvsd
ptvsd.enable_attach(address=('0.0.0.0', 5858), redirect_output=True)
ptvsd.wait_for_attach()
```
5. VS Code로 디버깅을 한다면 launch.json 작성(VS Code는모든 것을 실행하는 방법은 알고 있지 않기에.)  
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug with SAM CLI (Remote Debug)",
            "type": "python",
            "request": "attach",
            "port": 5858,
            "host":  "localhost",
            "pathMappings": [
                {
                "localRoot": "${workspaceFolder}/hello_world/build",
                "remoteRoot" : "/var/task"
                }
            ]
        }
    ]
}
```
6. sam local start-api -d 5858 (디버깅 시작)
