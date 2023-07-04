from App import DB, MALLOW
from marshmallow import fields


class UserModel(DB.Model):
    __tablename__ = "user"
    id = DB.Column(DB.Integer, primary_key=True)
    contact = DB.relationship("ContactModel")

    name = DB.Column(DB.String(100), nullable=False)
    email = DB.Column(DB.String(150), nullable=False, unique=True)
    password = DB.Column(DB.String(150), nullable=False)
    phone_no = DB.Column(DB.String(20))
    telephone_no = DB.Column(DB.String(20))
    no_of_contact = DB.Column(DB.Integer, default=0)


    def __init__(self, name : str, email : str, password : str, phone_no : str, telephone_no : str):
        self.name = name
        self.email = email
        self.password = password
        self.phone_no = phone_no
        self.telephone_no = telephone_no


    def __repr__(self) -> str:
        return "<User %r>"%self.name
    

    def toObject(self) -> dict:
        return {
            "id" : self.id,
            "name" : self.name,
            "email" : self.email,   
            "phone_no" : self.phone_no,
            "telephone_no" : self.telephone_no,
            "no_of_contact" : self.no_of_contact
        }
    
    @staticmethod
    def fromObject(object) -> "UserModel":
        return UserModel(
            name = object["name"],
            email = object["email"],
            password = object["password"],
            phone_no = object["phone_no"],
            telephone_no = object["telephone_no"]
        )
    
    
class UserSchema(MALLOW.Schema):
    
    class Meta:
        model : UserModel = UserModel
        fields : tuple = (
            "id", 
            "name", 
            "email", 
            "phone_no", 
            "telephone_no", 
            "no_of_contact"
        )

    id = fields.Integer()
    name = fields.String()
    email = fields.Email()
    phone_no = fields.String()
    telephone_no = fields.String()
    no_of_contact = fields.Integer()



user_schema : UserSchema = UserSchema()