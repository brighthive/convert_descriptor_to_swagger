{
    "openapi": "3.0.0",
    "info": {
        "description": "Example Data Resource API swagger file.  You can find\nout more about Swagger at\n[http://swagger.io](http://swagger.io) or on\n[irc.freenode.net, #swagger](http://swagger.io/irc/).\n",
        "version": "1.0.0",
        "title": "Swagger Data Resource",
        "termsOfService": "http://swagger.io/terms/",
        "contact": {
            "email": "engineering@brighthive.io"
        },
        "license": {
            "name": "Apache 2.0",
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
        }
    },
    "servers": [
        {
            "description": "SwaggerHub API Auto Mocking",
            "url": "https://virtserver.swaggerhub.com/loganripplinger/test_dr_swagger/1.0.0"
        }
    ],
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
                        "$ref": "#/components/parameters/offsetParam"
                    },
                    {
                        "$ref": "#/components/parameters/limitParam"
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
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/requestBodies/Credential"
                            }
                        }
                    }
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
            "get": {
                "tags": [
                    "credentials"
                ],
                "summary": "Get one item",
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
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/requestBodies/Credential"
                            }
                        }
                    }
                },
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
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/requestBodies/Credential"
                            }
                        }
                    }
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
                "responses": {
                    "200": {
                        "description": "ok"
                    }
                }
            }
        }
    },
    "components": {
        "parameters": {
            "offsetParam": {
                "in": "query",
                "name": "offset",
                "required": False,
                "schema": {
                    "type": "integer"
                },
                "description": "the offset"
            },
            "limitParam": {
                "in": "query",
                "name": "limit",
                "required": False,
                "schema": {
                    "type": "integer"
                },
                "description": "the limit"
            }
        },
        "schemas": {
            "Credential": {
                "description": "...",
                "type": "object",
                "required": [
                    "name"
                ],
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64",
                        "description": "...",
                        "example": 1
                    },
                    "name": {
                        "type": "string",
                        "description": "...",
                        "example": "Credential 1"
                    }
                }
            },
            "AllCredentials": {
                "description": "...",
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
                }
            },
            "Links": {
                "description": "...",
                "type": "object",
                "properties": {
                    "rel": {
                        "type": "string",
                        "enum": [
                            "self",
                            "first",
                            "prev",
                            "next",
                            "last"
                        ],
                        "description": "...",
                        "example": "first"
                    },
                    "href": {
                        "type": "string",
                        "example": "/credentials?offset=0&limit=20",
                        "description": "..."
                    }
                }
            },
            "Created": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Successfully added new resource.",
                        "description": "..."
                    },
                    "id": {
                        "type": "integer",
                        "format": "int64",
                        "description": "...",
                        "example": 1
                    }
                }
            }
        },
        "requestBodies": {
            "Credential": {
                "description": "Pet object that needs to be added to the store",
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/Credential"
                        }
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
        }
    }
}
