# 이미지 제작 웹 프로젝트

사용자가 입력하는 폼에 따라 알맞는 이미지를 제작해서 반환하는 웹 서비스
CAPTCHA용 이미지, 인스타그램 게시글 썸네일, 명함 등의 이미지 타입을 제공한다.

## Setup Instruction

### 1) 의존성 설치

```bash
python3 -m pip install -r requirements.txt
```

### 2) 서버 실행

```bash
python3 run.py
```

기본 실행 주소: `http://127.0.0.1:5000`  
Swagger 문서 주소: `http://127.0.0.1:5000/apidocs/`

## API 테스트

### CAPTCHA 이미지 생성

```bash
curl -X POST http://127.0.0.1:5000/captcha
```

### 인스타그램 썸네일 생성

```bash
curl -X POST http://127.0.0.1:5000/instagram \
  -H "Content-Type: application/json" \
  -d '{"background_color":"#F5D142","text":"HELLO"}'
```

### 명함 이미지 생성

```bash
curl -X POST http://127.0.0.1:5000/bizcard \
  -H "Content-Type: application/json" \
  -d '{"background_color":"#E8F0FE","name":"MOJAN KIM","phone":"010-1234-5678","email":"mojan@example.com"}'
```

## 실행 결과 예시

### CAPTCHA

![CAPTCHA Sample](images/captcha_9c83941654ec4f1c80eba17e4ca3d40f.png)

### Instagram Thumbnail

![Instagram Sample](images/instagram_1bb9697975aa4953ab0057f538e3c28d.png)

### Business Card

![Bizcard Sample](images/bizcard_03de210986984b4582f8ed57dc860ac1.png)
