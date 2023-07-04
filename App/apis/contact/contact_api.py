from App.utils import jwt_is_blacklist
from flask_restful import (
    Resource,
    reqparse,
    abort
)
from flask_jwt_extended import jwt_required



class UserContactResource(Resource):
    
    @jwt_required()
    @jwt_is_blacklist
    def get(self, contact_id : int, user_id : int):
        pass


    @jwt_required()
    @jwt_is_blacklist
    def put(self, contact_id : int, user_id : int):
        pass



class ContactResource(Resource):

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        
        

    @jwt_required()
    @jwt_is_blacklist
    def get(self, user_id):
        pass


    @jwt_required()
    @jwt_is_blacklist
    def post(self, user_id):
        pass


    @jwt_required()
    @jwt_is_blacklist
    def delete(self, user_id):
        pass



