from App.utils import jwt_is_blacklist
from App.models import (
    UserModel, 
    user_schema, 
    TokenModel
)
from App.utils import isValidEmail
from App import DB, BCRYPT
from flask_restful import (
    Resource,
    reqparse,
    abort
)
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    jwt_required,
    get_jwt_identity
)


class SignInResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("password", type=str, required=True)
        
    def post(self):
        
        data = self.parser.parse_args()

        user : UserModel = UserModel.query.filter_by(email = data["email"]).first()
        if not user:
            abort(404, message="User does not exists")

        if not BCRYPT.check_password_hash(user.password, data["password"]):
            abort(401, message="Incorrect password")

        access_token = create_access_token(identity=user.email)
        refresh_token = create_refresh_token(identity=user.email)

        schema = user_schema.dump(user)

        return {
            "message" : "Authorized access",
            "access_token" : access_token,
            "refresh_token" : refresh_token,
            "user" : schema
        }, 200


class SignUpResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("name", type=str, required=True)
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("password", type=str, required=True)
        self.parser.add_argument("phone_no", type=str, required=True)
        self.parser.add_argument("telephone_no", type=str, required=True)

    def post(self):
        
        data = self.parser.parse_args()

        user : UserModel = UserModel.query.filter_by(
            name = data["name"], email = data["email"]
        ).first()
        
        if user:
            abort(400, message="User already exists")
            
        if len(data["name"]) < 3:
            abort(400, message="name must at least be 3 characters long")
        
        if not isValidEmail(data["email"]):
            abort(400, message="Invalid email address")
        
        if len(data["password"]) < 6:
            abort(400, message="Password must at least be 6 characters long")

        data["password"] = BCRYPT.generate_password_hash(data["password"])
        user = UserModel.fromObject(data)

        DB.session.add(user)
        DB.session.commit()

        access_token = create_access_token(identity=user.email)
        refresh_token = create_refresh_token(identity=user.email)

        schema = user_schema.dump(user)

        return {
            "message" : "Authorized access",
            "access_token" : access_token,
            "refresh_token" : refresh_token,
            "user" : schema
        }, 200
    

class SignOutResource(Resource):

    @jwt_required(optional=True)
    @jwt_is_blacklist
    def post(self):
        token : TokenModel = TokenModel(get_jwt()["jti"])

        DB.session.add(token)
        DB.session.commit()

        return {"message" : "Logged out successfully"}, 200
        

class RefreshTokenResource(Resource):

    @jwt_required(refresh=True)
    @jwt_is_blacklist
    def post(self):

        access_token = get_jwt_identity()
        new_token = create_access_token(identity=access_token)

        return {"access_token" : new_token}, 200


class RefreshSignOutResource(Resource):

    @jwt_required(refresh=True)
    @jwt_is_blacklist
    def post(self):
        token : TokenModel = TokenModel(get_jwt()["jti"])

        DB.session.add(token)
        DB.session.commit()

        return {"message" : "Logged out successfully"}, 200
        
