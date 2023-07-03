from App import DB, MALLOW
from marshmallow import fields


class ContactModel(DB.Model):
    pass



class ContactSchema(MALLOW.Schema):
    
    class Meta:
        model : ContactModel = ContactModel
        fields : tuple = ()


contact_schema : ContactSchema = ContactSchema()
contacts_schema : ContactSchema = ContactSchema(many=True)