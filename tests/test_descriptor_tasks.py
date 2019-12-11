from convert_descriptor_to_swagger.descriptor_tasks import (
    add_schemas_from_descriptor,
    add_request_bodies_from_descriptor,
    add_responses_from_descriptor,
    add_tags_from_descriptors,
    add_singular_methods,
    add_plural_methods,
    generate_properties_from_desc
    )
from expects import expect, be_an, raise_error, have_property, equal, be_empty


def test_add_schemas_from_descriptor():
    expected_output = {
        "components": {
            "schemas": {
                "Test": {
                    "required": [
                        "test_name"
                    ],
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "format": "int64",
                            "description": "Test ID - Test's unique identifier",
                            # "example": 1
                        },
                        "test_name": {
                            "type": "string",
                            "description": "Test Name - Test's Name"
                            # "example": "Test 1"
                        }
                    },
                    "description": "..."
                },
                "AllTests": {
                    "type": "object",
                    "properties": {
                        "tests": {
                            "type": "array",
                            "items": {
                                "$ref": "#/components/schemas/Test"
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
            }
        }
    }

    descriptor = {
        "api": {
            "resource": "tests",
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
            "tablename": "tests",
            "restricted_fields": [],
            "schema": {
            "fields": [
                {
                "name": "id",
                "title": "Test ID",
                "type": "integer",
                "description": "Test's unique identifier",
                "required": False
                },
                {
                "name": "test_name",
                "title": "Test Name",
                "type": "string",
                "description": "Test's Name",
                "required": True
                }
            ],
            "primaryKey": "id"
            }
        }
    }

    swag = add_schemas_from_descriptor('test', descriptor)

    expect(swag).to(equal(expected_output))


def test_add_request_bodies_from_descriptor():
    expected_output = {
        'components': {
            "requestBodies": {
                "Test": {
                    "description": "Pet object that needs to be added to the store",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Test"
                            }
                        }
                    },
                    "required": True
                }
            }
        }
    }

    swag = add_request_bodies_from_descriptor('test', {})

    expect(swag).to(equal(expected_output))


def test_add_responses_from_descriptor():
    expected_output = {
        'components': {
            "responses": {
                "AllTests": {
                    "description": "...",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/AllTests"
                            }
                        }
                    }
                }
            }
        }
    }

    swag = add_responses_from_descriptor('test', {})

    expect(swag).to(equal(expected_output))


def test_add_tags_from_descriptor():
    expected_output = {
        "tags": [
            {
                "name": "tests",
                "description": "...",
                "externalDocs": {
                    "description": "Find out more",
                    "url": "http://swagger.io"
                }
            }
        ]
    }

    swag = add_tags_from_descriptors('test', {})

    expect(swag).to(equal(expected_output))


def test_add_tags_from_descriptor_with_items():
    expected_output = {
        "tags": [
            {
                "name": "test1"
            },
            {
                "name": "tests",
                "description": "...",
                "externalDocs": {
                    "description": "Find out more",
                    "url": "http://swagger.io"
                }
            }
        ]
    }

    swag = add_tags_from_descriptors('test', {
        "tags": [
            {
                "name": "test1"
            }
        ]
        })

    expect(swag).to(equal(expected_output))


def test_add_singular_methods():
    expected_output = {
        "paths": {
            "/credentials": {
                "get": {
                    "tags": [
                        "credentials"
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
                            "$ref": "#/components/responses/AllCredentials"
                        }
                    }
                },
                "post": {
                    "tags": [
                        "credentials"
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
            }
        }
    }

    swag = add_singular_methods('credential', {})

    expect(swag).to(equal(expected_output))


def test_add_plural_methods():
    expected_output = {
        "paths": {
            "/credentials/{id}": {
                "get": {
                    "tags": [
                        "credentials"
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
                        "credentials"
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
                        "credentials"
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
                        "credentials"
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
            }
        }
    }

    swag = add_plural_methods('credential', {})

    expect(swag).to(equal(expected_output))


def test_generate_properties_from_desc():
    descriptor = {
        "datastore": {
            "tablename": "tests",
            "restricted_fields": [],
            "schema": {
                "fields": [
                    {
                    "name": "id",
                    "title": "Test ID",
                    "type": "integer",
                    "description": "Test's unique identifier",
                    "required": False
                    },
                    {
                    "name": "test_name",
                    "title": "Test Name",
                    "type": "string",
                    "description": "Test's Name",
                    "required": True
                    }
                ],
                "primaryKey": "id"
            }
        }
    }

    expected_output = {
        'Test': {
            "required": [
                "test_name"
            ],
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "format": "int64",
                    "description": "Test ID - Test's unique identifier",
                    # "example": 1
                },
                "test_name": {
                    "type": "string",
                    "description": "Test Name - Test's Name",
                    # "example": f"{sentence_case_name} 1"
                }
            },
            "description": "..."
        }
    }

    output = generate_properties_from_desc('test', descriptor)

    expect(output).to(equal(expected_output))
