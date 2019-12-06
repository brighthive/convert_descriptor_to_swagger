from expects import expect, be_an, raise_error, have_property, equal, be_empty


def add_schemas_from_descriptor():
    expected_output = {
        "components": {
            "schemas": {
                "Credential": {
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
                            "example": "Credential 1"
                        }
                    },
                    "description": "..."
                },
                "AllCredentials": {
                    "type": "object",
                    "properties": {
                        "credentials": {
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
            }
        }
    }

    swag = add_schemas_from_descriptor({})

    expect(swag).to(equal(expected_output))
