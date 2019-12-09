def add_schemas_from_descriptor(name: str, desc: dict, swag: dict = {}) -> dict:
    lower_case_name = name.lower()
    sentence_case_name = name.capitalize()
    
    if 'components' not in swag:
        swag['components'] = {}
    
    if 'schemas' not in swag['components']:
        swag['components']['schemas'] = {}

    # construct each property from desc file
    generated_properties = generate_properties_from_desc(name, desc)

    # construct from descriptor file
    swag['components']['schemas'].update(generated_properties)
    swag['components']['schemas'].update({
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


def generate_properties_from_desc(name: str, desc: dict) -> dict:
    # lower_case_name = name.lower()
    sentence_case_name = name.capitalize()

    swag_output_properties = {}
    required_fields = []
    
    desc_properties = desc['datastore']['schema']['fields']
    
    for desc_prop in desc_properties:
        swag_property = {}
        swag_property[f'{desc_prop["name"]}'] = {}
        thing = swag_property[f'{desc_prop["name"]}']
        
        if desc_prop['type'] == 'string':
            thing.update({'type': 'string'})
        else:
            thing.update({'type': 'integer'})

        if desc_prop['type'] != 'string':
            thing.update({'format': 'int64'})
        
        thing.update({'description': f'{desc_prop["title"]} - {desc_prop["description"]}'})

        if desc_prop.get('required') == True:
            required_fields.append(desc_prop['name'])

        swag_output_properties.update(swag_property)

    output_schema = {
        f"{sentence_case_name}": {
            "required": required_fields,
            "type": "object",
            "properties": swag_output_properties,
            "description": "..."
        },
    }
    return output_schema


def add_request_bodies_from_descriptor(name: str, swag: dict = {}) -> dict:
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

def add_tags_from_descriptors(name: str, swag: dict = {}) -> dict:
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

def add_singular_methods(name: str, swag: dict = {}) -> dict:
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
                    "$ref": f"#/components/responses/All{sentence_case_name}s"
                }
            }
        },
        "post": {
            "tags": [
                f"{lower_case_name}s"
            ],
            "summary": "Create an item",
            "requestBody": {
                "$ref": f"#/components/requestBodies/{sentence_case_name}"
            },
            "responses": {
                "201": {
                    "$ref": "#/components/responses/Created"
                }
            }
        }
    })

    return swag

def add_plural_methods(name: str, swag: dict = {}) -> dict:
    sentence_case_name = name.capitalize()
    lower_case_name = name.lower()

    if 'paths' not in swag:
        swag['paths'] = {}

    if f'{name}' not in swag['paths']:
        swag['paths'][f'/{name}s/{{id}}'] = {}

    swag['paths'][f'/{name}s/{{id}}'].update({
        "get": {
            "tags": [
                f"{lower_case_name}s"
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
                f"{lower_case_name}s"
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
                "$ref": f"#/components/requestBodies/{sentence_case_name}"
            },
            "responses": {
                "200": {
                    "description": "ok"
                }
            }
        },
        "delete": {
            "tags": [
                f"{lower_case_name}s"
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
                f"{lower_case_name}s"
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
                "$ref": f"#/components/requestBodies/{sentence_case_name}"
            },
            "responses": {
                "200": {
                    "description": "ok"
                }
            }
        }
    })

    return swag