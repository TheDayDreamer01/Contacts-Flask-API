from App.utils import jwt_is_blacklist, auth_required
from App.models import (
    ContactModel, 
    contacts_schema, 
    contact_schema
)
from App import DB

from flask_jwt_extended import jwt_required
from flask_restful import (
    Resource,
    reqparse,
    abort
)



class UserContactResource(Resource):
    
    @jwt_required()
    @jwt_is_blacklist
    @auth_required
    def get(self, contact_id : int, user_id : int):
        contact : ContactModel = ContactModel.query.filter_by(
            id = contact_id, user_id = user_id).first()
        
        if not contact : 
            return {}, 200
        
        schema = contact_schema.dump(contact)
        return schema, 200  
        


    @jwt_required()
    @jwt_is_blacklist
    @auth_required
    def put(self, contact_id : int, user_id : int):
        pass

    
    @jwt_required()
    @jwt_is_blacklist
    @auth_required
    def delete(self, user_id : int):
        pass



class ContactResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("first_name", type=str, required=True)
        self.parser.add_argument("last_name", type=str, required=True)
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("phone_no", type=str, required=True)
        self.parser.add_argument("telephone_no", type=str, required=True)
        self.parser.add_argument("work_address", type=str, required=True)
        self.parser.add_argument("home_address", type=str, required=True)
        
    @jwt_required()
    @jwt_is_blacklist
    @auth_required
    def get(self, user_id : int):
        contact : ContactModel = ContactModel.query.filter_by(user_id = user_id).all()
        if not contact : 
            return {}, 200
        
        schema = contacts_schema.dump(contact)
        return schema, 200  
    

    @jwt_required()
    @jwt_is_blacklist
    @auth_required
    def post(self, user_id : int):
        
        data = self.parser.parse_args()

        contact : ContactModel = ContactModel.query.filter_by(
            user_id = user_id, phone_no = data["phone_no"], 
            telephone_no = data["telephone_no"]
        ).first()

        if contact:
            abort(401, message="Contact already exists")

        if not data["first_name"] or not data["last_name"]:
            abort(400, message="Name field must not be empty ")

        if not data["telephone_no"] or not data["phone_no"]:
            abort(400, message="Must setup at least one contact #")

        contact = ContactModel.fromObject(data)
        contact.user_id = user_id

        DB.session.add(contact)
        DB.session.commit()
        
        schema = contact_schema.dump(contact)
        return schema, 200
        
    


