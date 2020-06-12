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
                "AllTest": {
                    "type": "object",
                    "properties": {
                        "test": {
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
            "resource": "test",
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
            "tablename": "test",
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

    # expect(swag).to(equal(expected_output))
    assert swag == expected_output


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

    assert swag == expected_output


def test_add_responses_from_descriptor():
    expected_output = {
        'components': {
            "responses": {
                "AllTest": {
                    "description": "...",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/AllTest"
                            }
                        }
                    }
                }
            }
        }
    }

    swag = add_responses_from_descriptor('test', {})

    assert swag == expected_output


def test_add_tags_from_descriptor():
    expected_output = {
        "tags": [
            {
                "name": "test",
                "description": "...",
                "externalDocs": {
                    "description": "Find out more",
                    "url": "http://swagger.io"
                }
            }
        ]
    }

    swag = add_tags_from_descriptors('test', {})

    assert swag == expected_output


def test_add_tags_from_descriptor_with_items():
    expected_output = {
        "tags": [
            {
                "name": "test1"
            },
            {
                "name": "test",
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

    assert swag == expected_output


add_single_expected_output = {
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

def test_add_singular_methods():
    swag = add_singular_methods('credential', {})

    assert swag == add_single_expected_output


def test_add_plural_methods():
    expected_output = {
        "paths": {
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
            }
        }
    }

    swag = add_plural_methods('credential', {})

    assert swag == expected_output


def test_generate_properties_from_desc():
    descriptor = {
        "datastore": {
            "tablename": "test",
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

    assert output == expected_output
