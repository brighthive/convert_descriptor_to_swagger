from convert_descriptor_to_swagger import convert_descriptor_to_swagger
from convert_descriptor_to_swagger.main import process_descriptor
from tests.descriptors.credentials import credentials_descriptor
from tests.descriptors.programs import programs_descriptor
from expects import expect, be_an, raise_error, have_property, equal, be_empty
import json


def _load_desc(swagger):
    # print(json.dumps(swagger, indent=4))
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
                },
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
                        "credentialss": {
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
            "requestBodies": {
                "Credentials": {
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
            },
            "responses": {
                "AllCredentials": {
                    "description": "...",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/AllCredentials"
                            }
                        }
                    }
                }
            }
        }
    }


    output = convert_descriptor_to_swagger(credentials_descriptor)
    # print(json.dumps(output, indent=4))

    expect(output).to(equal(expected_output))
    # Final test
    # expect(output).to(equal(swagger))


def _process_descriptor():
    expected_output = {
        "tags": [
            {
                "name": "Credential",
                "description": "...",
                "externalDocs": {
                    "description": "Find out more",
                    "url": "http://swagger.io"
                }
            },
            {
                "name": "Programs",
                "description": "..."
            }
        ],
        "paths": {
            "/credentials": {
                "get": {
                    "tags": [
                        "credentials"
                    ],
                    "summary": "Get all items",
                    "parameters": [
                        {
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
                        {
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
                    ],
                    "responses": {
                        "200": {
                            "description": "ok",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/responses/AllCredentials"
                                    }
                                }
                            }
                        }
                    }
                },
                "post": {
                    "tags": [
                        "credentials"
                    ],
                    "summary": "Create an item",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/requestBodies/Credential"
                                }
                            }
                        },
                        "required": True
                    },
                    "responses": {
                        "201": {
                            "description": "created",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/responses/Created"
                                    }
                                }
                            }
                        }
                    }
                }
            },
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
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/requestBodies/Credential"
                                }
                            }
                        },
                        "required": True
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
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/requestBodies/Credential"
                                }
                            }
                        },
                        "required": True
                    },
                    "responses": {
                        "200": {
                            "description": "ok"
                        }
                    }
                }
            }
        },
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
                },
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
            },
            "responses": {
                "AllCredentials": {
                    "description": "...",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/AllCredentials"
                            }
                        }
                    }
                },
                "Created": {
                    "description": "...",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Created"
                            }
                        }
                    }
                }
            },
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
        }
    }

    swag = process_descriptor({}, {})

    expect(swag).to(equal(expected_output))
