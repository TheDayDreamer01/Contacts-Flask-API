from App import DB, MALLOW
from marshmallow import fields


class ContactModel(DB.Model):
    __tablename__ = "contact"
    id = DB.Column(DB.Integer, primary_key = True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey("user.id") ) 

    first_name = DB.Column(DB.String(40))    
    last_name = DB.Column(DB.String(40))    
    email = DB.Column(DB.String(150), unique=True)
    phone_no = DB.Column(DB.String(20), unique=True)
    telephone_no = DB.Column(DB.String(20), unique=True)

    work_address = DB.Column(DB.Text)
    home_address = DB.Column(DB.Text)

    date = DB.Column(DB.Date, default=DB.func.current_date())
    

    def __init__(self, first_name : str, last_name :str, email : str,
                phone_no : str, telephone_no : str, work_address : str, home_address : str):
        self.first_name = first_name 
        self.last_name = last_name 
        self.email = email 
        self.phone_no = phone_no 
        self.telephone_no = telephone_no 
        self.work_address = work_address
        self.home_address = home_address


    def __repr__(self) -> str:
        return "<Contact %r>"%(self.first_name + " " + self.last_name)
    

    def toObject(self) -> dict:
        return {
            "id" : self.id,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email" : self.email,
            "phone_no" : self.phone_no,
            "telephone_no" : self.telephone_no,
            "home_address" : self.home_address,
            "work_address" : self.work_address
        }
    
    @staticmethod
    def fromObject(data : dict) -> "ContactModel":
        return ContactModel(
            first_name = data["first_name"],
            last_name = data["last_name"],
            email = data["email"],
            phone_no = data["phone_no"],
            telephone_no = data["telephone_no"],
            work_address = data["work_address"],
            home_address = data["home_address"]
        )


class ContactSchema(MALLOW.Schema):
    
    class Meta:
        model : ContactModel = ContactModel
        fields : tuple = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_no",
            "telephone_no"
        )

    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    phone_no = fields.String()
    telephone_no = fields.String()


contact_schema : ContactSchema = ContactSchema()
contacts_schema : ContactSchema = ContactSchema(many=True)