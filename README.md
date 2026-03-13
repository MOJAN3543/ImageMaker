# 이미지 제작 웹 프로젝트

사용자가 입력하는 폼에 따라 알맞는 이미지를 제작해서 반환하는 웹 서비스
CAPTCHA용 이미지, 인스타그램 게시글 썸네일, 명함 등의 이미지 타입을 제공한다.

## Test

- CAPTCHA 이미지

```bash
curl -X POST http://127.0.0.1:5000/captcha
```

- 인스타그램 썸네일

```bash
curl -X POST http://127.0.0.1:5000/instagram \
  -H "Content-Type: application/json" \
  -d '{"background_color":"#F5D142","text":"Text"}'
```

- 명함

```bash
curl -X POST http://127.0.0.1:5000/bizcard \
  -H "Content-Type: application/json" \
  -d '{"background_color":"#E8F0FE","name":"Jane Doe","phone":"010-1234-5678","email":"janedoe@example.com"}'
```
