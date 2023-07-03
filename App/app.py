from flask import Flask


def create_contact_app(environment) -> Flask:

    contact_app : Flask = Flask(__name__)   
    contact_app.config.from_object(environment)

    

    return contact_app