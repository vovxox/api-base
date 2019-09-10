import config
import logging.config
from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

application = Flask(__name__, instance_relative_config=True)

# logging.config.fileConfig("logging.conf")
# logger = logging.getLogger("wslog")
# application = Flask(__name__, instance_relative_config=True)


def configure_app(flask_app):
    flask_app.config.from_object(config)
    flask_app.config.from_pyfile("config.py", silent=True)


def configure_swagger(flask_app):
    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={"app_name": "Seans-Python-Flask-REST-Boilerplate"}
    )
    flask_app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


def initialize_app(flask_app):
    configure_app(flask_app)
    configure_swagger(flask_app)

    # api =  API.add_namespace(
    #     Api(application),
    #     description="MetaboLights RESTful WebService",
    #     apiVersion=application.config.get("API_VERSION"),
    #     basePath=application.config.get("WS_APP_BASE_LINK"),
    #     api_spec_url=application.config.get("API_DOC"),
    #     # resourcePath=res_path,
    # )

    # API = flask_app.add_namespace(
    #     # ,
    #     description="MetaboLights RESTful WebService",
    #     apiVersion=application.config.get("API_VERSION"),
    #     basePath=application.config.get("WS_APP_BASE_LINK"),
    #     api_spec_url=application.config.get("API_DOC"),
    #     # resourcePath=res_path,
    # )

    # API.add_resource(Jira, "/project/<string:project>")
    # API.add_resource(Jira, "/issue/<string:issue>")


def main():
    print("Initialising application")
    initialize_app(application)
    print(
        "Starting server %s v%s",
        application.config.get("WS_APP_NAME"),
        application.config.get("WS_APP_VERSION"),
    )
    # application.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG, ssl_context=context)
    print("Starting application")
    application.run(
        host="0.0.0.0",
        port=application.config.get("PORT"),
        debug=application.config.get("DEBUG"),
    )
    print(
        "Finished server %s v%s",
        application.config.get("WS_APP_NAME"),
        application.config.get("WS_APP_VERSION"),
    )


if __name__ == "__main__":
    main()
