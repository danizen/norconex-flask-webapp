from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)


def register_blueprints(app):
    # Importing inside function prevents circular imports
    from .views import crawls
    app.register_blueprint(crawls, url_prefix='/crawls')


register_blueprints(app)


if __name__ == '__main__':
    app.run()

