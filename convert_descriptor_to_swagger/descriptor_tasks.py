from convert_descriptor_to_swagger.util import TABLESCHEMA_TO_SWAGGER_TYPES
from deepmerge import always_merger


def add_schemas_from_descriptor(name: str, descriptor: dict, swag: dict = {}) -> dict:
    lower_case_name = name.lower()
    sentence_case_name = name.capitalize()

    # construct each property from desc file
    generated_properties = generate_properties_from_desc(name, descriptor)

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


def generate_properties_from_desc(name: str, descriptor: dict) -> dict:
    sentence_case_name = name.capitalize()

    swag_output_properties = {}
    required_fields = []

    desc_properties = descriptor["datastore"]["schema"]["fields"]

    for desc_prop in desc_properties:
        swag_property = {}
        swag_property[f'{desc_prop["name"]}'] = {}
        prop_node = swag_property[f'{desc_prop["name"]}']

        swagger_type = TABLESCHEMA_TO_SWAGGER_TYPES[desc_prop["type"]]
        prop_node.update({"type": swagger_type})

        if desc_prop["type"] != "string":
            prop_node.update({"format": "int64"})

        prop_node.update(
            {"description": f'{desc_prop["title"]} - {desc_prop["description"]}'}
        )

        try:
            if desc_prop["constraints"].get("required") is True:
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

    paths = {
        "paths": {
            f"/{name}": {
                "get": {
                    "tags": [f"{lower_case_name}"],
                    "summary": "Get all items",
                    "parameters": [
                        {"$ref": "#/components/parameters/offsetParam"},
                        {"$ref": "#/components/parameters/limitParam"},
                    ],
                    "responses": {
                        "200": {
                            "description": "Success",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": f"#/components/schemas/All{sentence_case_name}"
                                    }
                                }
                            },
                        },
                        "401": {
                            "description": "Access denied",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/401"}
                                }
                            },
                        },
                        "500": {
                            "description": "Internal server error",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/500"}
                                }
                            },
                        },
                    },
                },
                "post": {
                    "tags": [f"{lower_case_name}"],
                    "summary": "Create a new item",
                    "requestBody": {
                        "$ref": f"#/components/requestBodies/{sentence_case_name}"
                    },
                    "responses": {
                        "201": {"$ref": "#/components/responses/Created"},
                        "401": {
                            "description": "Access denied",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/401"}
                                }
                            },
                        },
                        "500": {
                            "description": "Internal server error",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/500"}
                                }
                            },
                        },
                    },
                },
            },
            f"/{name}/query": {
                "post": {
                    "tags": [f"{lower_case_name}"],
                    "summary": "Query for items",
                    "requestBody": {
                        "$ref": f"#/components/requestBodies/{sentence_case_name}"
                    },
                    "responses": {
                        "200": {
                            "description": "Success",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": f"#/components/schemas/All{sentence_case_name}"
                                    }
                                }
                            },
                        },
                        "401": {
                            "description": "Access denied",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/401"}
                                }
                            },
                        },
                        "500": {
                            "description": "Internal server error",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/500"}
                                }
                            },
                        },
                    },
                }
            },
        }
    }

    swag = always_merger.merge(swag, paths)

    return swag


def add_plural_methods(name: str, swag: dict = {}) -> dict:
    sentence_case_name = name.capitalize()
    lower_case_name = name.lower()

    paths = {
        "paths": {
            f"/{name}/{{id}}": {
                "parameters": [{"$ref": "#/components/parameters/id"}],
                "get": {
                    "tags": [f"{lower_case_name}"],
                    "summary": "Get item by ID",
                    "responses": {
                        "200": {
                            "description": "Success",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": f"#/components/schemas/{sentence_case_name}"
                                    }
                                }
                            },
                        },
                        "401": {
                            "description": "Access denied",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/401"}
                                }
                            },
                        },
                        "500": {
                            "description": "Internal server error",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/500"}
                                }
                            },
                        },
                    },
                },
                "put": {
                    "tags": [f"{lower_case_name}"],
                    "summary": "Replace item by ID",
                    "requestBody": {
                        "$ref": f"#/components/requestBodies/{sentence_case_name}"
                    },
                    "responses": {
                        "201": {"$ref": "#/components/responses/Created"},
                        "401": {
                            "description": "Access denied",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/401"}
                                }
                            },
                        },
                        "500": {
                            "description": "Internal server error",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/500"}
                                }
                            },
                        },
                    },
                },
                "delete": {
                    "tags": [f"{lower_case_name}"],
                    "summary": "Delete item by ID",
                    "responses": {
                        "401": {
                            "description": "Access denied",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/401"}
                                }
                            },
                        },
                        "405": {
                            "description": "Unimplemented",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/405"}
                                }
                            },
                        },
                    },
                },
                "patch": {
                    "tags": [f"{lower_case_name}"],
                    "summary": "Update data by ID",
                    "requestBody": {
                        "$ref": f"#/components/requestBodies/{sentence_case_name}"
                    },
                    "responses": {
                        "201": {"$ref": "#/components/responses/Created"},
                        "401": {
                            "description": "Access denied",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/401"}
                                }
                            },
                        },
                        "500": {
                            "description": "Internal server error",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/500"}
                                }
                            },
                        },
                    },
                },
            }
        }
    }

    swag = always_merger.merge(swag, paths)

    return swag
