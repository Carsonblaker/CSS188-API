from flask import Flask
from flask_restful import Api, Resource, reqparse


class Hello(Resource):
    def get(self):
        return {"message": "Hello World!"}


class Square(Resource):
    def get(self, num):
        return {'Shape': __class__.__name__, 'Area': num * num}


class Echo(Resource):
    def get(self):
        # Use RequestParser to parse the arguments from the request.
        # Don't reinvent the wheel! We could write a parser ourselves,
        # but let's use one that was already made for us!
        parser = reqparse.RequestParser()
        parser.add_argument('arg1', type=str, location='args')
        parser.add_argument('arg2', type=str, location='args')

        arguments = parser.parse_args()
        # Return the arguments as JSON
        return arguments


def init_api(app: Flask) -> None:
    """Initialize the API for the given Flask app"""
    api = Api(app)
    api.add_resource(Hello, "/")
    api.add_resource(Square, "/square/<int:num>")
    api.add_resource(Echo, "/echo")


def create_app() -> Flask:
    """Create and configure the Flask app"""
    app = Flask(__name__)
    init_api(app)
    return app


def run_app(debug: bool = True) -> None:
    create_app().run(debug=debug)


if __name__ == "__main__":
    run_app()