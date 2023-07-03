from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow


DB : SQLAlchemy = SQLAlchemy()
JWT : JWTManager = JWTManager()
BCRYPT : Bcrypt = Bcrypt()
MALLOW : Marshmallow = Marshmallow()


def create_contact_app(environment) -> Flask:

    contact_app : Flask = Flask(__name__)   
    contact_app.config.from_object(environment)

    API : Api = Api(contact_app)
    DB.init_app(contact_app)
    BCRYPT.init_app(contact_app)
    MALLOW.init_app(contact_app)
    JWT.init_app(contact_app)
    CORS(contact_app)


    from App.apis.contact import (
        ContactResource,
        UserContactResource
    )
    from App.apis.auth import (
        SignInResource,
        SignOutResource,
        SignUpResource,
        RefreshSignOutResource,
        RefreshTokenResource
    )


    API.add_resource(ContactResource, "/api/contact/")
    API.add_resource(UserContactResource, "/api/contact/<int:contact_id>")

    API.add_resource(SignInResource, "/api/auth/signin")
    API.add_resource(SignUpResource, "/api/auth/signup")
    API.add_resource(SignOutResource, "/api/auth/signout")
    API.add_resource(RefreshTokenResource, "/api/auth/refresh")
    API.add_resource(RefreshSignOutResource, "/api/auth/refresh/signout")


    with contact_app.app_context():
        DB.create_all()
    

    return contact_app