from flask import Flask, jsonify
from flask_restful import Api, Resource


class Hello(Resource):
    def get(self):
        return {"message": "Hello World!"}

class Square(Resource):
    def get(self, num):
        return jsonify({'Shape': __class__.__name__,
'Area': num*num})


def init_api(app: Flask) -> None:
    """Initialize the API for the given Flask app"""
    api = Api(app)
    api.add_resource(Hello, "/")
    api.add_resource(Square, "/square/<int:num>")



def create_app() -> Flask:
    """Create and configure the Flask app"""
    app = Flask(__name__)
    init_api(app)
    return app


def run_app(debug: bool = True) -> None:
    create_app().run(debug=debug)


if __name__ == "__main__":
    run_app()