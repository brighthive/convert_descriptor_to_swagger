from convert_descriptor_to_swagger.base_tasks import add_metadata, add_parameters, add_base_schemas
from expects import expect, be_an, raise_error, have_property, equal, be_empty


def test_add_metadata():
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
        }
    }
    
    swag = add_metadata()

    expect(swag).to(equal(expected_output))


def test_add_parameters():
    expected_output = {
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
            }
        }
    }

    swag = add_parameters({})

    expect(swag).to(equal(expected_output))


def test_add_base_schemas():
    expected_output = {
        "components": {
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
                            "example": "/credentials?offset=0&limit=20"
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
                }
            }
        }
    }

    swag = add_base_schemas({})

    expect(swag).to(equal(expected_output))
