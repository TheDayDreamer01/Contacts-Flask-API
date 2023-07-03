from App import create_contact_app
from Config import (
    TestingEnvironment,
    DevelopmentEnvironment,
    ProductionEnvironment
)


ENVIRONMENT : str = "DEVELOPMENT"
config = DevelopmentEnvironment()


match (ENVIRONMENT):
    case "PRODUCTION":
        config = ProductionEnvironment()
    case "TESTING":
        config = TestingEnvironment()
    case _:
        config = DevelopmentEnvironment()


contact_app = create_contact_app(config)

if __name__ == "__main__":
    contact_app.run(debug=True)