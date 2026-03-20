from app import app


def _json(response):
    return response.get_json(silent=True) or {}


def _assert_image_path_payload(response):
    payload = _json(response)
    assert response.status_code == 200
    assert "image_path" in payload
    assert payload["image_path"]


def test_instagram_success_skeleton():
    with app.test_client() as client:
        response = client.post(
            "/instagram",
            json={"background_color": "#F5D142", "text": "HELLO"},
        )
        _assert_image_path_payload(response)


def test_instagram_invalid_payload_skeleton():
    with app.test_client() as client:
        response = client.post(
            "/instagram",
            json={"background_color": "#F5D142", "text": ""},
        )
        assert response.status_code == 400


def test_captcha_success_skeleton():
    with app.test_client() as client:
        response = client.post("/captcha")
        _assert_image_path_payload(response)


def test_bizcard_success_skeleton():
    with app.test_client() as client:
        response = client.post(
            "/bizcard",
            json={
                "background_color": "#E8F0FE",
                "name": "MOJAN KIM",
                "phone": "010-1234-5678",
                "email": "mojan@example.com",
            },
        )
        _assert_image_path_payload(response)


def test_bizcard_invalid_payload_skeleton():
    with app.test_client() as client:
        response = client.post(
            "/bizcard",
            json={"background_color": "#E8F0FE", "name": "MOJAN KIM"},
        )
        assert response.status_code == 400

def test_instagram_empty_color():
    # 인스타그램 Post Payload에 color가 없어도 정상적으로 동작 하는지
    with app.test_client() as client:
        response = client.post("/instagram", json={"text": "HELLO"})
        _assert_image_path_payload(response)

def test_instagram_empty_text():
    # 인스타그램 Post Payload에 text가 없으면 동작하지 않는지(400)
    with app.test_client() as client:
        response = client.post("/instagram", json={"background_color": "#F5D142"})
        assert response.status_code == 400

def test_bizcard_empty_color():
    # 인스타그램 Post Payload에 color가 없어도 정상적으로 동작 하는지
    with app.test_client() as client:
        response = client.post(
            "/bizcard",
            json={
                "name": "MOJAN KIM",
                "phone": "010-1234-5678",
                "email": "mojan@example.com",
            },
        )
        _assert_image_path_payload(response)

def test_bizcard_empty_name():
    # 인스타그램 Post Payload에 name이 없으면 동작하지 않는지(400)
    with app.test_client() as client:
        response = client.post(
            "/bizcard",
            json={
                "background_color": "#E8F0FE",
                "phone": "010-1234-5678",
                "email": "mojan@example.com",
            },
        )
        assert response.status_code == 400

def test_bizcard_empty_phone():
    # 인스타그램 Post Payload에 phone이 없으면 동작하지 않는지(400)
    with app.test_client() as client:
        response = client.post(
            "/bizcard",
            json={
                "background_color": "#E8F0FE",
                "name": "MOJAN KIM",
                "email": "mojan@example.com",
            },
        )
        assert response.status_code == 400

def test_bizcard_empty_email():
    # 인스타그램 Post Payload에 email이 없으면 동작하지 않는지(400)
    with app.test_client() as client:
        response = client.post(
            "/bizcard",
            json={
                "background_color": "#E8F0FE",
                "name": "MOJAN KIM",
                "phone": "010-1234-5678",
            },
        )
        assert response.status_code == 400
