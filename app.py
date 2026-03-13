from flask import Flask

app = Flask(__name__)


@app.post("/instagram")
def instagram():
    return "", 204


@app.post("/captcha")
def captcha():
    return "", 204


@app.post("/bizcard")
def bizcard():
    return "", 204


if __name__ == "__main__":
    app.run()
