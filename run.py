from app import app
from flasgger import Swagger


if __name__ == "__main__":
    Swagger(app)
    app.run()
