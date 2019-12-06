

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


def add_request_body_from_descriptor(name: str, swag: dict) -> dict:
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