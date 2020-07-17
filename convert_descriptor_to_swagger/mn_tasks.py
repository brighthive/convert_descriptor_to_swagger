from deepmerge import always_merger
from convert_descriptor_to_swagger.reference.full_output import (
    component_schemas_mn,
    component_responses_mn,
    component_request_bodies_mn,
)


def add_mn_schemas(swag: dict = {}) -> dict:
    swag = always_merger.merge(swag, component_schemas_mn)
    return swag


def add_mn_responses(swag: dict = {}) -> dict:
    swag = always_merger.merge(swag, component_responses_mn)
    return swag


def add_mn_request_bodies(swag: dict = {}) -> dict:
    swag = always_merger.merge(swag, component_request_bodies_mn)
    return swag


def add_mn_paths(relationship: list, swag: dict = {}) -> dict:
    parent = relationship[0]
    child = relationship[1]

    paths_mn = {
        "paths": {
            f"/{parent}/{{id}}/{child}": {
                "parameters": [{"$ref": "#/components/parameters/id"}],
                "get": {
                    "tags": [f"{parent}"],
                    "summary": "Get many-to-many relationship",
                    "responses": {
                        "200": {"$ref": "#/components/responses/Relations"},
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
                    "tags": [f"{parent}"],
                    "summary": "Replace many-to-many relationship",
                    "requestBody": {"$ref": "#/components/requestBodies/Relations"},
                    "responses": {
                        "200": {"$ref": "#/components/responses/Relations"},
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
                "patch": {
                    "tags": [f"{parent}"],
                    "summary": "Update many-to-many relationship",
                    "requestBody": {"$ref": "#/components/requestBodies/Relations"},
                    "responses": {
                        "200": {"$ref": "#/components/responses/Relations"},
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
            f"/{child}/{{id}}/{parent}": {
                "parameters": [{"$ref": "#/components/parameters/id"}],
                "get": {
                    "tags": [f"{child}"],
                    "summary": "Get many-to-many relationship",
                    "responses": {
                        "200": {"$ref": "#/components/responses/Relations"},
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
                    "tags": [f"{child}"],
                    "summary": "Replace many-to-many relationship",
                    "requestBody": {"$ref": "#/components/requestBodies/Relations"},
                    "responses": {
                        "200": {"$ref": "#/components/responses/Relations"},
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
                "patch": {
                    "tags": [f"{child}"],
                    "summary": "Update many-to-many relationship",
                    "requestBody": {"$ref": "#/components/requestBodies/Relations"},
                    "responses": {
                        "200": {"$ref": "#/components/responses/Relations"},
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
        }
    }

    swag = always_merger.merge(swag, paths_mn)
    return swag
