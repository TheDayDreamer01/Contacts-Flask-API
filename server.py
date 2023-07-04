from App import create_contact_app
from Config import (
    TestingEnvironment,
    DevelopmentEnvironment,
    ProductionEnvironment
)


ENVIRONMENT : str = "DEVELOPMENT"
config = DevelopmentEnvironment()


match ENVIRONMENT.upper():
    case "PRODUCTION":
        config = ProductionEnvironment()
    case "TESTING":
        config = TestingEnvironment()
    case _:
        config = DevelopmentEnvironment()


contact_app = create_contact_app(config)

if __name__ == "__main__":
    
    match ENVIRONMENT.upper():
        case "PRODUCTION":
            contact_app.run()
    
        case _:
            contact_app.run(debug=True, host="0.0.0.0")