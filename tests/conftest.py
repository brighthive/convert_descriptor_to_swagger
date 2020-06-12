import pytest
import os
import yaml


# I believe this was an easy way to test/actually generate real swagger docs
@pytest.fixture
def swagger():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'swagger/dr.yaml')

    with open(filename) as file:
        dr_swagger = yaml.load(file, Loader=yaml.FullLoader)

        # print(json.dumps(dr_swagger, indent=4))
    
    return dr_swagger


@pytest.fixture
def expected_output():
    expected_output = {
        "openapi": "3.0.0",
        "info": {
            "title": "Swagger Data Resource",
            "description": "Autogenerated Data Resource API swagger file.  You can find\nout more about Swagger at\n[http://swagger.io](http://swagger.io) or on\n[irc.freenode.net, #swagger](http://swagger.io/irc/).\n",
            "termsOfService": "http://swagger.io/terms/",
            "contact": {
                "email": "engineering@brighthive.io"
            },
            "license": {
                "name": "Apache 2.0",
                "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
            },
            "version": "1.0.0"
        },
        "servers": [
            {
                "description": "Local server.",
                "url": "http://localhost:8000"
            }
        ],
        "components": {
            "parameters": {
                "offsetParam": {
                    "name": "offset",
                    "in": "query",
                    "description": "the offset",
                    "required": False,
                    "style": "form",
                    "explode": True,
                    "schema": {
                        "type": "integer"
                    }
                },
                "limitParam": {
                    "name": "limit",
                    "in": "query",
                    "description": "the limit",
                    "required": False,
                    "style": "form",
                    "explode": True,
                    "schema": {
                        "type": "integer"
                    }
                }
            },
            "schemas": {
                "Links": {
                    "type": "object",
                    "properties": {
                        "rel": {
                            "type": "string",
                            "description": "...",
                            "example": "first",
                            "enum": [
                                "self",
                                "first",
                                "prev",
                                "next",
                                "last"
                            ]
                        },
                        "href": {
                            "type": "string",
                            "description": "...",
                            "example": "/credential?offset=0&limit=20"
                        }
                    },
                    "description": "..."
                },
                "Created": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "...",
                            "example": "Successfully added new resource."
                        },
                        "id": {
                            "type": "integer",
                            "description": "...",
                            "format": "int64",
                            "example": 1
                        }
                    }
                },
                "Credential": {
                    "required": [
                        "credential_name"
                    ],
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "format": "int64",
                            "description": "Credential ID - Credential's unique identifier"
                        },
                        "credential_name": {
                            "type": "string",
                            "description": "Credential Name - Credential's Name"
                        }
                    },
                    "description": "..."
                },
                "AllCredential": {
                    "type": "object",
                    "properties": {
                        "credential": {
                            "type": "array",
                            "items": {
                                "$ref": "#/components/schemas/Credential"
                            }
                        },
                        "links": {
                            "type": "array",
                            "items": {
                                "$ref": "#/components/schemas/Links"
                            }
                        }
                    },
                    "description": "..."
                }
            },
            "responses": {
                "Created": {
                    "description": "...",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Created"
                            }
                        }
                    }
                },
                "AllCredential": {
                    "description": "...",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/AllCredential"
                            }
                        }
                    }
                }
            },
            "requestBodies": {
                "Credential": {
                    "description": "Pet object that needs to be added to the store",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Credential"
                            }
                        }
                    },
                    "required": True
                }
            }
        },
        "tags": [
            {
                "name": "credential",
                "description": "...",
                "externalDocs": {
                    "description": "Find out more",
                    "url": "http://swagger.io"
                }
            }
        ],
        "paths": {
            "/credential": {
                "get": {
                    "tags": [
                        "credential"
                    ],
                    "summary": "Get all items",
                    "parameters": [
                        {
                            "$ref": "#/components/parameters/offsetParam"
                        },
                        {
                            "$ref": "#/components/parameters/limitParam"
                        }
                    ],
                    "responses": {
                        "200": {
                            "$ref": "#/components/responses/AllCredential"
                        }
                    }
                },
                "post": {
                    "tags": [
                        "credential"
                    ],
                    "summary": "Create an item",
                    "requestBody": {
                        "$ref": "#/components/requestBodies/Credential"
                    },
                    "responses": {
                        "201": {
                            "$ref": "#/components/responses/Created"
                        }
                    }
                }
            },
            "/credential/{id}": {
                "get": {
                    "tags": [
                        "credential"
                    ],
                    "summary": "Get one item",
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "description": "User ID",
                            "required": True,
                            "style": "simple",
                            "explode": False,
                            "schema": {
                                "type": "integer",
                                "format": "int64"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "ok"
                        }
                    }
                },
                "put": {
                    "tags": [
                        "credential"
                    ],
                    "summary": "Put one item",
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "description": "User ID",
                            "required": True,
                            "style": "simple",
                            "explode": False,
                            "schema": {
                                "type": "integer",
                                "format": "int64"
                            }
                        }
                    ],
                    "requestBody": {
                        "$ref": "#/components/requestBodies/Credential"
                    },
                    "responses": {
                        "200": {
                            "description": "ok"
                        }
                    }
                },
                "delete": {
                    "tags": [
                        "credential"
                    ],
                    "summary": "Get one item",
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "description": "User ID",
                            "required": True,
                            "style": "simple",
                            "explode": False,
                            "schema": {
                                "type": "integer",
                                "format": "int64"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "ok"
                        }
                    }
                },
                "patch": {
                    "tags": [
                        "credential"
                    ],
                    "summary": "Get one item",
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "description": "User ID",
                            "required": True,
                            "style": "simple",
                            "explode": False,
                            "schema": {
                                "type": "integer",
                                "format": "int64"
                            }
                        }
                    ],
                    "requestBody": {
                        "$ref": "#/components/requestBodies/Credential"
                    },
                    "responses": {
                        "200": {
                            "description": "ok"
                        }
                    }
                }
            },
            "/credential/query": {
                "post": {
                    "tags": [
                        "credential"
                    ],
                    "summary": "Query for items.",
                    "requestBody": {
                        "$ref": "#/components/requestBodies/Credential"
                    },
                    "responses": {
                        "201": {
                            "$ref": "#/components/responses/Created"
                        }
                    }
                }
            }
        }
    }
    return expected_output


@pytest.fixture
def credential_descriptor():
    credential_descriptor = {
        "api": {
            "resource": "credential",
            "methods": [
            {
                "get": {
                "enabled": True,
                "secured": False,
                "grants": ["get:users"]
                },
                "post": {
                "enabled": True,
                "secured": False,
                "grants": []
                },
                "put": {
                "enabled": True,
                "secured": False,
                "grants": []
                },
                "patch": {
                "enabled": True,
                "secured": False,
                "grants": []
                },
                "delete": {
                "enabled": True,
                "secured": False,
                "grants": []
                }
            }
            ]
        },
        "datastore": {
            "tablename": "credential",
            "restricted_fields": [],
            "schema": {
            "fields": [
                {
                "name": "id",
                "title": "Credential ID",
                "type": "integer",
                "description": "Credential's unique identifier",
                "required": False
                },
                {
                "name": "credential_name",
                "title": "Credential Name",
                "type": "string",
                "description": "Credential's Name",
                "required": True
                }
            ],
            "primaryKey": "id"
            }
        }
    }
    return credential_descriptor


@pytest.fixture
def program_descriptor():
    program_descriptor = {
        "api": {
            "resource": "program",
            "methods": [
            {
                "get": {
                "enabled": True,
                "secured": False,
                "grants": ["get:users"]
                },
                "post": {
                "enabled": True,
                "secured": False,
                "grants": ["get:users"]
                },
                "put": {
                "enabled": True,
                "secured": True,
                "grants": ["get:users"]
                },
                "patch": {
                "enabled": True,
                "secured": True,
                "grants": ["get:users"]
                },
                "delete": {
                "enabled": True,
                "secured": True,
                "grants": ["get:users"]
                },
                "custom": [
                {
                    "resource": "/program/credential",
                    "methods": [
                    {
                        "get": {
                        "enabled": True,
                        "secured": False,
                        "grants": ["get:users"]
                        },
                        "put": {
                        "enabled": True,
                        "secured": False,
                        "grants": []
                        },
                        "patch": {
                        "enabled": True,
                        "secured": False,
                        "grants": []
                        },
                        "delete": {
                        "enabled": True,
                        "secured": False,
                        "grants": []
                        }
                    }
                    ]
                }
                ]
            }
            ]
        },
        "datastore": {
            "tablename": "program",
            "restricted_fields": [],
            "schema": {
            "fields": [
                {
                "name": "id",
                "title": "Program ID",
                "type": "integer",
                "description": "Program's unique identifier",
                "required": False
                },
                {
                "name": "program_name",
                "title": "Program Name",
                "type": "string",
                "description": "Program's name.",
                "required": True
                },
                {
                "name": "program_code",
                "title": "Program Code",
                "type": "integer",
                "description": "Program's Code",
                "required": True
                },
                {
                "name": "program_description",
                "title": "Program Description",
                "type": "string",
                "description": "Program's Description",
                "required": True
                },
                {
                "name": "program_status",
                "title": "Program Status",
                "type": "string",
                "description": "Program's Status",
                "required": True
                },
                {
                "name": "program_fees",
                "title": "Program Fees",
                "type": "number",
                "description": "Program's tuition fees",
                "required": True
                },
                {
                "name": "eligibility_criteria",
                "title": "Eligibility Criteria",
                "type": "string",
                "description": "Program's eligibility criteria",
                "required": True
                },
                {
                "name": "program_url",
                "title": "Program URL",
                "type": "string",
                "format": "uri",
                "description": "Program's webpage url",
                "required": True
                },
                {
                "name": "program_contact_phone",
                "title": "Program Contact Phone",
                "type": "string",
                "description": "Program's contact telephone",
                "required": False
                },
                {
                "name": "program_contact_email",
                "title": "Program Contact Email",
                "type": "string",
                "format": "email",
                "description": "Program's contact email address",
                "required": False
                },
                {
                "name": "languages",
                "title": "Languages",
                "type": "string",
                "description": "Languages the program is offered in",
                "required": False
                },
                {
                "name": "current_intake_capacity",
                "title": "Current Intake Capacity",
                "type": "integer",
                "description": "Current intake capacity of the program",
                "required": False
                },
                {
                "name": "program_offering_model",
                "title": "Program Offering Model",
                "type": "integer",
                "description": "The program's current offering model",
                "required": False
                },
                {
                "name": "program_length_hours",
                "title": "Program Length (Hours)",
                "type": "number",
                "description": "Length of the program (in hours)",
                "required": False
                },
                {
                "name": "program_length_weeks",
                "title": "Program Length (Weeks)",
                "type": "number",
                "description": "Length of the program (in weeks)",
                "required": False
                },
                {
                "name": "program_soc",
                "title": "Program SOC",
                "type": "integer",
                "description": "Program SOC",
                "required": False
                },
                {
                "name": "funding_sources",
                "title": "Funding Source",
                "type": "string",
                "description": "The program's funding source",
                "required": False
                },
                {
                "name": "on_etpl",
                "title": "On ETPL",
                "type": "integer",
                "description": "Whether or not the student is on ETPL",
                "required": False
                },
                {
                "name": "cost_of_books_and_supplies",
                "title": "Cost of Books and Supplies",
                "type": "number",
                "description": "Cost of Books and Supplies",
                "required": False
                },
                {
                "name": "provider_id",
                "title": "Provider ID",
                "type": "integer",
                "description": "Foreign key for provider",
                "required": False
                },
                {
                "name": "location_id",
                "title": "Provider ID",
                "type": "integer",
                "description": "Foreign key for provider",
                "required": False
                },
                {
                "name": "credential_earned",
                "title": "Provider ID",
                "type": "integer",
                "description": "Foreign key for provider",
                "required": False
                },
                {
                "name": "potential_outcome_id",
                "title": "Provider ID",
                "type": "integer",
                "description": "Foreign key for provider",
                "required": False
                },
                {
                "name": "prerequisite_id",
                "title": "Provider ID",
                "type": "integer",
                "description": "Foreign key for provider",
                "required": False
                }
            ],
            "primaryKey": "id",
            "foreignKeys": [
                {
                "fields": ["provider_id"],
                "reference": {
                    "resource": "providers",
                    "fields": ["id"]
                }
                },
                {
                "fields": ["location_id"],
                "reference": {
                    "resource": "locations",
                    "fields": ["id"]
                }
                },
                {
                "fields": ["credential_earned"],
                "reference": {
                    "resource": "credential",
                    "fields": ["id"]
                }
                },
                {
                "fields": ["potential_outcome_id"],
                "reference": {
                    "resource": "program_potential_outcomes",
                    "fields": ["id"]
                }
                },
                {
                "fields": ["prerequisite_id"],
                "reference": {
                    "resource": "program_prerequisites",
                    "fields": ["id"]
                }
                }
            ]
            }
        }
    }
    return program_descriptor
