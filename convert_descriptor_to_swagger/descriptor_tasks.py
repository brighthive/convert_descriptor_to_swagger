

def add_schemas_from_descriptor(name: str, swag: dict) -> dict:
    lower_case_name = name.lower()
    sentence_case_name = name.capitalize()
    
    if 'components' not in swag:
        swag['components'] = {}
    
    if 'schemas' not in swag['components']:
        swag['components']['schemas'] = {}

    swag['components']['schemas'].update({
        f"{sentence_case_name}": {
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
                    "example": f"{sentence_case_name} 1"
                }
            },
            "description": "..."
        },
        f"All{sentence_case_name}s": {
            "type": "object",
            "properties": {
                f"{lower_case_name}s": {
                    "type": "array",
                    "items": {
                        "$ref": f"#/components/schemas/{sentence_case_name}"
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
    })

    return swag


def add_request_bodies_from_descriptor(name: str, swag: dict) -> dict:
    sentence_case_name = name.capitalize()
    
    if 'components' not in swag:
        swag['components'] = {}
    
    if 'requestBodies' not in swag['components']:
        swag['components']['requestBodies'] = {}

    swag['components']['requestBodies'].update({
        f"{sentence_case_name}": {
            "description": "Pet object that needs to be added to the store",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": f"#/components/schemas/{sentence_case_name}"
                    }
                }
            },
            "required": True
                }
    })
    
    return swag

def add_responses_from_descriptor(name: str, swag:dict) -> dict:
    sentence_case_name = name.capitalize()
    
    if 'components' not in swag:
        swag['components'] = {}
    
    if 'responses' not in swag['components']:
        swag['components']['responses'] = {}
    
    swag['components']['responses'].update({
        f"All{sentence_case_name}s": {
            "description": "...",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": f"#/components/schemas/All{sentence_case_name}s"
                    }
                }
            }
        }
    })
    
    return swag

def add_tags_from_descriptors(name: str, swag: dict) -> dict:
    sentence_case_name = name.capitalize()

    if 'tags' not in swag:
        swag['tags'] = []

    tags = swag['tags']

    tags.append(
        {
            "name": f"{sentence_case_name}",
            "description": "...",
            "externalDocs": {
                "description": "Find out more",
                "url": "http://swagger.io"
            }
        }
    )

    swag['tags'] = tags

    return swag

def add_singular_methods(name: str, swag: dict) -> dict:
    sentence_case_name = name.capitalize()
    lower_case_name = name.lower()

    if 'paths' not in swag:
        swag['paths'] = {}

    if f'{name}' not in swag['paths']:
        swag['paths'][f'/{name}s'] = {}

    swag['paths'][f'/{name}s'].update({
        "get": {
            "tags": [
                f"{lower_case_name}s"
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
                                "$ref": f"#/components/responses/All{sentence_case_name}s"
                            }
                        }
                    }
                }
            }
        },
        "post": {
            "tags": [
                f"{lower_case_name}s"
            ],
            "summary": "Create an item",
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": f"#/components/requestBodies/{sentence_case_name}"
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
    })

    return swag
