## AWS SAM(Serverless Application Model) ?

### SAM를 실행하는 환경에서 필요한 설치 목록

-   Python 설치

-   SAM 설치

```
 //--user 옵션을 추가하면  root 권한이 없어도 패키지 설치가 가능.
 pip install --user aws-sam-cli
```

-   Docker 설치  
    OS Window일 경우 WSL2가 설치되어야함.
    (https://www.44bits.io/ko/post/wsl2-install-and-basic-usage)
-   AWS CLI 설치

### SAM 설치

```
sam init --runtime <your python version> --name <project name>
ex) sam init --runtime python3.8 --name sangwon-sam-app
```

### SAM 핵심 파일

![](sam-dir.png)

-   event.json : 람다 함수 파라미터로 넘길 인자값이 존재.
-   template.yaml : 람다의 환경을 설정할 수 있는 파일. ( 람다 실행시간, 람다 환경변수,Layer 등)

### SAM Build

```
sam build --template <your_yaml_file_name> --use-container
```

### SAM Run

```
# 이벤트 사용
sam local invoke <your_function_name> --event <your_event_path>
# 이벤트 사용없이
sam local invoke <your_function_name> --no-event
```

### SAM Deploy

```
aws lambda update-function-code --function-name <your_function_name> --zip-file fileb://function.zip --profile <your_profile_name>
```

### 참고 문헌

-   https://docs.aws.amazon.com/ko_kr/serverless-application-model/latest/developerguide/what-is-sam.html

-   https://docs.aws.amazon.com/ko_kr/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html
