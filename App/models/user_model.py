from App import DB, MALLOW
from marshmallow import fields


class UserModel(DB.Model):
    pass



class UserSchema(MALLOW.Schema):
    
    class Meta:
        model : UserModel = UserModel
        fields : tuple = ()



user_schema : UserSchema = UserSchema()