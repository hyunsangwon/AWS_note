## SMMS_V2_Outer_Move_Event_Check 람다 목적
- 패킷 아이디가 2, 3번(이동감지)인 패킷을 처리 하는 람다입니다.

## 빌드 전 체크해야하는 항목
- AWS credentials 파일에 ACCESS KEY, SECRET KET가 유효한지 체크  
- SAM 명령어가 설치되었는지 확인  
- GIT PULL 명령어로 최신화  
## Build
```bash
sam build --template SMMS_V2_Outer_Move_Event_Check_TEST.yaml --use-container
```
## Compile
```bash
# 이벤트 사용
sam local invoke --template SMMS_V2_Outer_Move_Event_Check_TEST.yaml --event events/event.json
# 이벤트 사용없이
sam local invoke --template SMMS_V2_Outer_Move_Event_Check_TEST.yaml --no-event
```
## Deploy
```bash
aws lambda update-function-code --function-name SMMS_V2_Outer_Move_Event_Check_TEST --zip-file fileb://function.zip --profile SMMS_V2
```
## Error 대처
- 에러내용 : UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position ***: illegal multibyte sequence  
- 대처법 : event.json 파일 인코딩 형식을 ANSI로 변경