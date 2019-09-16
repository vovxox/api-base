from flask import request
from flask.ext.restful import Resource, Api, marshal_with, fields, abort
from flask_restful_swagger import swagger
from jira import JIRA
from .models import DummyResult
from .models import HelloResult
from .models import IssueResult

from .errors import JsonRequiredError
from .errors import JsonInvalidError

options = {"server": "https://testhomelol.atlassian.net"}


class DummyEndpoint(Resource):
    @swagger.operation(responseClass=DummyResult.__name__, nickname="dummy")
    @marshal_with(DummyResult.resource_fields)
    def get(self):
        """Return a DummyResult object

        Lightweight response to let us confirm that the server is on-line"""
        return DummyResult()


class GetIssueEndpoint(Resource):
    @swagger.operation(responseClass=IssueResult.__name__, nickname="issue")
    @marshal_with(IssueResult.resource_fields)
    def get(self, issue_id):
        """Return a DummyResult object
        
        Lightweight response to let us confirm that the server is on-line"""
        jira = JIRA(
            server="https://testhomelol.atlassian.net",
            options={"verify": False},
            basic_auth=("vovxox1@gmail.com", ""),
        )
        # print(jira.issue("TEST-1").fields.reporter.displayName)
        return IssueResult(name=jira.issue("TEST-1").fields.reporter.displayName)


class HelloEndpoint(Resource):
    @swagger.operation(
        responseClass=HelloResult.__name__,
        nickname="hello",
        responseMessages=[
            {"code": 400, "message": "Input required"},
            {"code": 500, "message": "JSON format not valid"},
        ],
        parameters=[
            {
                "name": "name",
                "description": "JSON-encoded name",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "body",
            }
        ],
    )
    @marshal_with(HelloResult.resource_fields)
    def post(self):
        """Return a HelloResult object"""
        reqs = request.get_json()
        if not reqs:
            raise JsonRequiredError()
        try:
            reqs["name"]
            return HelloResult(name=reqs["name"])
        except KeyError:
            raise JsonInvalidError()
