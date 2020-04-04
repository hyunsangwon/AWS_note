Serverless note
=======

## 기술 스택 (S3 +Lambda + node.js 8 v)

## Introduction
 -  S3 용량큰 이미지 PUT시 람다를 활용한 resize 활용법

## Getting started
    1. S3 CREATE 
    2. S3 버킷 정책 수정
    3. 람다 생성 node.js **8버전** 으로 해야함!
    4. 로컬에서 npm install util async gm
    5. zip파일로 압축후 AWS람다에 배포
    6. 생성한 s3 트리거로 추가
    7. IAM 들어가서 S3 권한 생성후 람다에서 실행 역할 수정!
    8. 이미지 등록후 테스트 