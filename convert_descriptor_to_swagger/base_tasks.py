def add_metadata(title="Swagger Data Resource") -> dict:
    swag = {}
    swag['openapi'] = "3.0.0"
    swag['info'] =  {
        "title": title,
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

    return swag


def add_parameters(swag: dict) -> dict:
    if 'components' not in swag:
        swag['components'] = {}
    
    if 'parameters' not in swag:
        swag['components']['parameters'] = {}

    swag['components']['parameters'].update({
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
    })

    return swag


def add_base_schemas(swag: dict) -> dict:
    if 'components' not in swag:
        swag['components'] = {}
    
    if 'schemas' not in swag['components']:
        swag['components']['schemas'] = {}

    swag['components']['schemas'].update({
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
    })

    return swag

def add_base_responses(swag: dict) -> dict:
    if 'components' not in swag:
        swag['components'] = {}
    
    if 'responses' not in swag['components']:
        swag['components']['responses'] = {}

    swag['components']['responses'].update({
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
    })
    return swag