import pytest


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
                        "title": "Team name",
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
    return team_descriptor
