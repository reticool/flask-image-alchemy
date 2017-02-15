from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_image_alchemy.storages import S3Storage
from flask_image_alchemy.fields import StdImageField


admin = Admin()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # config
    app.config['SECRET_KEY'] = '123456790'
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql+psycopg2://localhost:5432/test'

    # init extensions
    admin.init_app(app)
    db.init_app(app)

    return app

# create app
app = create_app()


# define main route
@app.route('/')
def index():
    return 'Hello World'


# define models
class ExampleModel(db.Model):
    image = db.Column(
        StdImageField(
            storage=S3Storage(),
            variations={
                'thumbnail': {"width": 100, "height": 100, "crop": True}
            }
        )
    )

def build_db():
    db.drop_all()
    db.create_all()


build_db()
app.run(debug=True)