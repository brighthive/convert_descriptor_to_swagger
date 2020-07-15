import pytest
import os
import yaml
from tests.reference.full_output import full_output


# # I believe this was an easy way to test/actually generate real swagger docs
# @pytest.fixture
# def swagger():
#     dirname = os.path.dirname(__file__)
#     filename = os.path.join(dirname, 'swagger/dr.yaml')

#     with open(filename) as file:
#         dr_swagger = yaml.load(file, Loader=yaml.FullLoader)

#         # print(json.dumps(dr_swagger, indent=4))

#     return dr_swagger


@pytest.fixture
def expected_output():
    return full_output


@pytest.fixture
def people_descriptor():
    people_descriptor = {
        "api": {
            "resource": "people",
            "methods": [
                {
                    "get": {"enabled": True, "secured": False, "grants": ["get:users"]},
                    "post": {"enabled": True, "secured": False, "grants": []},
                    "put": {"enabled": True, "secured": False, "grants": []},
                    "patch": {"enabled": True, "secured": False, "grants": []},
                    "delete": {"enabled": True, "secured": False, "grants": []},
                }
            ],
        },
        "datastore": {
            "tablename": "people",
            "restricted_fields": [],
            "schema": {
                "fields": [
                    {
                        "name": "id",
                        "title": "Person ID",
                        "type": "integer",
                        "description": "A unique identifer for person.",
                        "constraints": {},
                    },
                    {
                        "name": "name",
                        "title": "Person's name",
                        "type": "string",
                        "description": "The name that a Person goes by. This is left intentionally generic.",
                        "constraints": {},
                    },
                ],
                "primaryKey": "id",
            },
        },
    }
    return people_descriptor


# TODO need to handle foreign keys?
@pytest.fixture
def team_descriptor():
    team_descriptor = {
        "api": {
            "resource": "team",
            "methods": [
                {
                    "get": {"enabled": True, "secured": False, "grants": ["get:users"]},
                    "post": {
                        "enabled": True,
                        "secured": False,
                        "grants": ["get:users"],
                    },
                    "put": {"enabled": True, "secured": True, "grants": ["get:users"]},
                    "patch": {
                        "enabled": True,
                        "secured": True,
                        "grants": ["get:users"],
                    },
                    "delete": {
                        "enabled": True,
                        "secured": True,
                        "grants": ["get:users"],
                    },
                    "custom": [
                        {
                            "resource": "/people/team",
                            "methods": [
                                {
                                    "get": {
                                        "enabled": True,
                                        "secured": False,
                                        "grants": ["get:users"],
                                    },
                                    "put": {
                                        "enabled": True,
                                        "secured": False,
                                        "grants": [],
                                    },
                                    "patch": {
                                        "enabled": True,
                                        "secured": False,
                                        "grants": [],
                                    },
                                    "delete": {
                                        "enabled": True,
                                        "secured": False,
                                        "grants": [],
                                    },
                                }
                            ],
                        }
                    ],
                }
            ],
        },
        "datastore": {
            "tablename": "team",
            "restricted_fields": [],
            "schema": {
                "fields": [
                    {
                        "name": "id",
                        "title": "Team ID",
                        "type": "integer",
                        "description": "A unique identifer for team.",
                        "constraints": {},
                    },
                    {
                        "name": "name",
                        "title": "Team Name",
                        "type": "string",
                        "description": "The name that a Team goes by.",
                        "constraints": {},
                    },
                ],
                "primaryKey": "id",
                "foreignKeys": [
                    {
                        "fields": ["provider_id"],
                        "reference": {"resource": "providers", "fields": ["id"]},
                    },
                    {
                        "fields": ["location_id"],
                        "reference": {"resource": "locations", "fields": ["id"]},
                    },
                    {
                        "fields": ["credential_earned"],
                        "reference": {"resource": "credential", "fields": ["id"]},
                    },
                    {
                        "fields": ["potential_outcome_id"],
                        "reference": {
                            "resource": "program_potential_outcomes",
                            "fields": ["id"],
                        },
                    },
                    {
                        "fields": ["prerequisite_id"],
                        "reference": {
                            "resource": "program_prerequisites",
                            "fields": ["id"],
                        },
                    },
                ],
            },
        },
    }
    return program_descriptor
