## AWS SSM(AWS Systems Manager) ?

-   AWS에서 인프라를 보고 제어하기 위해 사용할 수 있는 AWS 서비스.

### 이점

-   Bastion Host (터널링 전용 서버)가 필요없음.
-   Key Pair가 필요 없음.
-   Private Subnet에 있는 EC2 터널링 없이 바로 접속 가능.
    session-manager-plugin

### 특징

-   SSH 명령으로 Server에 접속하는 대신, SSM서비스의 start-session 명령으로
    AWS Systems Manager에 연결.
-   SSM은 HTTPS 프로토콜 사용.
-   인증은 AWS Credentials를 사용 (IAM User).

### 로컬 환경 구성

1. awscli 설치

```
pip3 install awscli
```

2. AWS Session Manger Plugin 설치

-   Windows Session Manager Plugin 설치

https://s3.amazonaws.com/session-manager-downloads/plugin/latest/windows/SessionManagerPluginSetup.exe

-   MacOS Session Manager Plugin 설치

curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/mac/sessionmanager-bundle.zip" -o "sessionmanager-bundle.zip"

unzip sessionmanager-bundle.zip

sudo ./sessionmanager-bundle/install -i /usr/local/sessionmanagerplugin -b /usr/local/bin/session-manager-plugin

3. session-manager-plugin 설치 확인

```
> session-manager-plugin
아래와 같은 문장이 나오면 설치 성공.
The Session Manager plugin was installed successfully. Use the AWS CLI to start a session.
```

4. SSM으로 EC2 연결

```
aws ssm start-session --target <EC2 인스턴스 ID> --profile <profile 이름>
```

5. 세션 종료

```
aws ssm terminate-session --session-id <session-id>
```

### 서버 환경 구성

1. 콘솔로 로그인하여 EC2연결 후 아래 명령어 입력

```
# 우분투 Ubuntu Server 20.04, 18.04, 16.04 LTS (64 bit)
1. sudo apt install snapd
2. sudo snap install amazon-ssm-agent --classic
3. sudo systemctl start snap.amazon-ssm-agent.amazon-ssm-agent.service
```

2. EC2에 권한 추가 (SSMStartSession, AmazonSSMFullAccess)

3. SSMStartSession Json 편집

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SessionManagerStartSession",
            "Effect": "Allow",
            "Action": "ssm:StartSession",
            "Resource": [
                "arn:aws:ec2:*:*:instance/*",
                "arn:aws:ssm:*:*:document/AWS-StartSSHSession"
            ]
        },
        {
            "Sid": "SessionManagerTerminateSession",
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession",
                "ssm:ResumeSession"
            ],
            "Resource": "arn:aws:ssm:*:*:session/${aws:username}-*"
        }
    ]
}
```

### 참고문헌

[1] Session Manager Plugin 설치
https://docs.aws.amazon.com/ko_kr/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html
[2] 시작 명령어
https://docs.aws.amazon.com/ko_kr/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html
[3] SSH 연결
https://docs.aws.amazon.com/ko_kr/systems-manager/latest/userguide/session-manager-getting-started-enable-ssh-connections.html
[4] SSH 연결
https://medium.com/@dnorth98/hello-aws-session-manager-farewell-ssh-7fdfa4134696
[5] profile 수정
https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-configure-profiles.html
[6] 작동방식
https://docs.aws.amazon.com/ko_kr/systems-manager/latest/userguide/how-it-works.html
[7] 우분투 SSM 설치
https://docs.aws.amazon.com/ko_kr/systems-manager/latest/userguide/agent-install-ubuntu.html
