from convert_descriptor_to_swagger.util import TABLESCHEMA_TO_SWAGGER_TYPES
from deepmerge import always_merger


def add_schemas_from_descriptor(name: str, desc: dict, swag: dict = {}) -> dict:
    lower_case_name = name.lower()
    sentence_case_name = name.capitalize()

    # construct each property from desc file
    generated_properties = generate_properties_from_desc(name, desc)

    # construct from descriptor file
    schemas = {
        "components": {
            "schemas": {
                **generated_properties,
                f"All{sentence_case_name}": {
                    "type": "object",
                    "properties": {
                        f"{lower_case_name}": {
                            "type": "array",
                            "items": {
                                "$ref": f"#/components/schemas/{sentence_case_name}"
                            },
                        },
                        "links": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/Links"},
                        },
                    },
                },
            }
        }
    }

    swag = always_merger.merge(swag, schemas)
    return swag


def generate_properties_from_desc(name: str, desc: dict) -> dict:
    sentence_case_name = name.capitalize()

    swag_output_properties = {}
    required_fields = []

    desc_properties = desc["datastore"]["schema"]["fields"]

    for desc_prop in desc_properties:
        swag_property = {}
        swag_property[f'{desc_prop["name"]}'] = {}
        thing = swag_property[f'{desc_prop["name"]}']

        swagger_type = TABLESCHEMA_TO_SWAGGER_TYPES[desc_prop["type"]]
        thing.update({"type": swagger_type})

        if desc_prop["type"] != "string":
            thing.update({"format": "int64"})

        thing.update(
            {"description": f'{desc_prop["title"]} - {desc_prop["description"]}'}
        )

        try:
            if desc_prop["constraints"].get("required") == True:
                required_fields.append(desc_prop["name"])
        except KeyError:
            pass

        swag_output_properties.update(swag_property)

    output_schema = {
        f"{sentence_case_name}": {
            "type": "object",
            "properties": swag_output_properties,
        }
    }

    if required_fields:
        output_schema[sentence_case_name].update({"required": required_fields})

    return output_schema


def add_request_bodies_from_descriptor(name: str, swag: dict = {}) -> dict:
    sentence_case_name = name.capitalize()

    request_bodies = {
        "components": {
            "requestBodies": {
                f"{sentence_case_name}": {
                    "description": "Object to be added",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": f"#/components/schemas/{sentence_case_name}"
                            }
                        }
                    },
                    "required": True,
                }
            }
        }
    }

    always_merger.merge(swag, request_bodies)
    return swag


def add_responses_from_descriptor(name: str, swag: dict) -> dict:
    sentence_case_name = name.capitalize()

    responses = {
        "components": {
            "responses": {
                f"All{sentence_case_name}": {
                    "description": "List of objects",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": f"#/components/schemas/All{sentence_case_name}"
                            }
                        }
                    },
                }
            }
        }
    }

    swag = always_merger.merge(swag, responses)

    return swag


def add_tags_from_descriptors(name: str, swag: dict = {}) -> dict:
    lower_case_name = name.lower()

    tags = {
        "tags": [
            {
                "name": f"{lower_case_name}",
                "description": "Data Resource",
                "externalDocs": {
                    "description": "More info",
                    "url": "http://example.com",
                },
            }
        ]
    }

    always_merger.merge(swag, tags)

    return swag


def add_singular_methods(name: str, swag: dict = {}) -> dict:
    sentence_case_name = name.capitalize()
    lower_case_name = name.lower()

    if "paths" not in swag:
        swag["paths"] = {}

    if f"{name}" not in swag["paths"]:
        swag["paths"][f"/{name}"] = {}

    swag["paths"][f"/{name}"].update(
        {
            "get": {
                "tags": [f"{lower_case_name}"],
                "summary": "Get all items",
                "parameters": [
                    {"$ref": "#/components/parameters/offsetParam"},
                    {"$ref": "#/components/parameters/limitParam"},
                ],
                "responses": {
                    "200": {"$ref": f"#/components/responses/All{sentence_case_name}"}
                },
            },
            "post": {
                "tags": [f"{lower_case_name}"],
                "summary": "Create an item",
                "requestBody": {
                    "$ref": f"#/components/requestBodies/{sentence_case_name}"
                },
                "responses": {"201": {"$ref": "#/components/responses/Created"}},
            },
        }
    )

    if f"{name}" not in swag["paths"]:
        swag["paths"][f"/{name}/query"] = {}

    swag["paths"][f"/{name}/query"].update(
        {
            "post": {
                "tags": [f"{lower_case_name}"],
                "summary": "Query for items.",
                "requestBody": {
                    "$ref": f"#/components/requestBodies/{sentence_case_name}"
                },
                "responses": {"201": {"$ref": "#/components/responses/Created"}},
            }
        }
    )

    return swag


def add_plural_methods(name: str, swag: dict = {}) -> dict:
    sentence_case_name = name.capitalize()
    lower_case_name = name.lower()

    if "paths" not in swag:
        swag["paths"] = {}

    if f"{name}" not in swag["paths"]:
        swag["paths"][f"/{name}/{{id}}"] = {}

    swag["paths"][f"/{name}/{{id}}"].update(
        {
            "get": {
                "tags": [f"{lower_case_name}"],
                "summary": "Get one item",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "description": "User ID",
                        "required": True,
                        "style": "simple",
                        "explode": False,
                        "schema": {"type": "integer", "format": "int64"},
                    }
                ],
                "responses": {"200": {"description": "ok"}},
            },
            "put": {
                "tags": [f"{lower_case_name}"],
                "summary": "Put one item",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "description": "User ID",
                        "required": True,
                        "style": "simple",
                        "explode": False,
                        "schema": {"type": "integer", "format": "int64"},
                    }
                ],
                "requestBody": {
                    "$ref": f"#/components/requestBodies/{sentence_case_name}"
                },
                "responses": {"200": {"description": "ok"}},
            },
            "delete": {
                "tags": [f"{lower_case_name}"],
                "summary": "Get one item",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "description": "User ID",
                        "required": True,
                        "style": "simple",
                        "explode": False,
                        "schema": {"type": "integer", "format": "int64"},
                    }
                ],
                "responses": {"200": {"description": "ok"}},
            },
            "patch": {
                "tags": [f"{lower_case_name}"],
                "summary": "Get one item",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "description": "User ID",
                        "required": True,
                        "style": "simple",
                        "explode": False,
                        "schema": {"type": "integer", "format": "int64"},
                    }
                ],
                "requestBody": {
                    "$ref": f"#/components/requestBodies/{sentence_case_name}"
                },
                "responses": {"200": {"description": "ok"}},
            },
        }
    )

    return swag
