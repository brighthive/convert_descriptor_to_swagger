from convert_descriptor_to_swagger.descriptor_tasks import (
    add_schemas_from_descriptor,
    add_request_bodies_from_descriptor,
    add_responses_from_descriptor,
    add_tags_from_descriptors
    )
from expects import expect, be_an, raise_error, have_property, equal, be_empty


def test_add_schemas_from_descriptor():
    expected_output = {
        "components": {
            "schemas": {
                "Test": {
                    "required": [
                        "name"
                    ],
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "...",
                            "format": "int64",
                            "example": 1
                        },
                        "name": {
                            "type": "string",
                            "description": "...",
                            "example": "Test 1"
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

    swag = add_schemas_from_descriptor('test', {})

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
                "name": "Test",
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
                "name": "test"
            },
            {
                "name": "Test",
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
                "name": "test"
            }
        ]
        })

    expect(swag).to(equal(expected_output))