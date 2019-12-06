from convert_descriptor_to_swagger.descriptor_tasks import add_schemas_from_descriptor
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
