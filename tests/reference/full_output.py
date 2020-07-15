metadata = {
    "openapi": "3.0.0",
    "info": {
        "title": "BrightHive Data Resource generated OpenAPI Spec 3.0",
        "description": "Autogenerated Data Resource API OpenAPI Specification 3.0 (Swagger) file.\n\n[Learn more about BrightHive Data Resources.](https://github.com/brighthive/data-resource-generator)\n\n[Learn more about BrightHive!](https://brighthive.io)\n\nYou can find out more about Swagger at\n[http://swagger.io](http://swagger.io) or on\n[irc.freenode.net, #swagger](http://swagger.io/irc/).\n",
        "termsOfService": "http://swagger.io/terms/",
        "contact": {"email": "engineering@brighthive.io"},
        "license": {
            "name": "Apache 2.0",
            "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
        },
        "version": "0.0.0",
    },
}

servers = {
    "servers": [
        {"description": "Local server 1", "url": "http://0.0.0.0:8081"},
        {"description": "Local server 2", "url": "http://localhost:8000"},
    ]
}

component_parameters_base = {
    "components": {
        "parameters": {
            "offsetParam": {
                "name": "offset",
                "in": "query",
                "description": "Offset value",
                "required": False,
                "style": "form",
                "explode": True,
                "schema": {"type": "integer"},
            },
            "limitParam": {
                "name": "limit",
                "in": "query",
                "description": "Item limit value",
                "required": False,
                "style": "form",
                "explode": True,
                "schema": {"type": "integer"},
            },
            "id": {
                "name": "id",
                "in": "path",
                "description": "Item's primary key value",
                "required": True,
                "style": "simple",
                "explode": False,
                "schema": {"type": "integer", "format": "int64"},
            },
        }
    }
}

# Schemas
# TODO I think this needs to be added?
component_schemas_base = {
    "components": {
        "schemas": {
            "400": {
                "description": "Error",
                "allOf": [
                    {"$ref": "#/components/schemas/ErrorMessage"},
                    {
                        "type": "object",
                        "properties": {"message": {"example": "Error Message"}},
                    },
                ],
            },
            "401": {
                "description": "Access Denied",
                "allOf": [
                    {"$ref": "#/components/schemas/ErrorMessage"},
                    {
                        "type": "object",
                        "properties": {"message": {"example": "Access Denied"}},
                    },
                ],
            },
            "405": {
                "description": "Access Denied",
                "allOf": [
                    {"$ref": "#/components/schemas/ErrorMessage"},
                    {
                        "type": "object",
                        "properties": {"message": {"example": "Unimplemented delete"}},
                    },
                ],
            },
            "500": {
                "description": "An error occured in the server",
                "allOf": [
                    {"$ref": "#/components/schemas/ErrorMessage"},
                    {
                        "type": "object",
                        "properties": {"error": {"example": "Internal Server Error"}},
                    },
                ],
            },
            "Links": {
                "type": "object",
                "properties": {
                    "rel": {
                        "type": "string",
                        "description": "Pagination navigation page name",
                        "example": "first",
                        "enum": ["self", "first", "prev", "next", "last"],
                    },
                    "href": {
                        "type": "string",
                        "description": "URI for pagination.",
                        "example": "/credential?offset=0&limit=20",
                    },
                },
                "description": "Pagination navigation links",
            },
            "Created": {
                "type": "object",
                "description": "Successful creation message",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Status message",
                        "example": "Successfully added new resource.",
                    },
                    "id": {
                        "type": "integer",
                        "description": "Item's primary key value",
                        "format": "int64",
                        "example": 1,
                    },
                },
            },
            "ErrorMessage": {
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "A description of the error that occured",
                        "example": "Internal Server Error",
                    }
                }
            },
            "ErrorMessages": {
                "properties": {
                    "errors": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "example": "Required item is missing",
                        },
                    }
                }
            },
        }
    }
}

component_schemas_people = {
    "components": {
        "schemas": {
            "People": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64",
                        "description": "Person ID - A unique identifer for person.",
                    },
                    "name": {
                        "type": "string",
                        "description": "Person's name - The name that a Person goes by. This is left intentionally generic.",
                    },
                },
            },
            "AllPeople": {
                "type": "object",
                "properties": {
                    "people": {
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/People"},
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

component_schemas_team = {
    "components": {
        "schemas": {
            "Team": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64",
                        "description": "Team ID - A unique identifer for team.",
                    },
                    "name": {
                        "type": "string",
                        "description": "Team name - The name that a Team goes by.",
                    },
                },
            },
            "AllTeam": {
                "type": "object",
                "properties": {
                    "team": {
                        "type": "array",
                        "items": {"$ref": "#/components/schemas/Team"},
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

# TODO
component_schemas_mn = {
    "components": {
        "schemas": {
            "Relations": {
                "description": "List of primary keys found in many to many relationship",
                "type": "array",
                "example": [1, 2, 3],
                "items": {"type": "integer"},
            }
        }
    }
}

# Responses
# TODO ?
component_responses_base = {
    "components": {
        "responses": {
            "Created": {
                "description": "Successfully created an item message",
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/Created"}
                    }
                },
            }
        }
    }
}

component_responses_people = {
    "components": {
        "responses": {
            "AllPeople": {
                "description": "List of objects",
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/AllPeople"}
                    }
                },
            }
        }
    }
}

component_responses_team = {
    "components": {
        "responses": {
            "AllTeam": {
                "description": "List of objects",
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/AllTeam"}
                    }
                },
            }
        }
    }
}

component_responses_mn = {
    "components": {
        "responses": {
            "Relations": {
                "description": "A list of primary keys found in the many to many relationship",
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/Relations"}
                    }
                },
            }
        }
    }
}

# Request bodies
component_request_bodies_people = {
    "components": {
        "requestBodies": {
            "People": {
                "description": "Object to be added",
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/People"}
                    }
                },
                "required": True,
            }
        }
    }
}

component_request_bodies_team = {
    "components": {
        "requestBodies": {
            "Team": {
                "description": "Object to be added",
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/Team"}
                    }
                },
                "required": True,
            }
        }
    }
}

component_request_bodies_mn = {
    "components": {
        "requestBodies": {
            "Relations": {
                "description": "A list of primary key relationships.",
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/Relations"}
                    }
                },
            }
        }
    }
}


# Tags
tags_people = {
    "tags": [
        {
            "name": "people",
            "description": "Data Resource",
            "externalDocs": {"description": "More info", "url": "http://example.com"},
        }
    ]
}

tags_team = {
    "tags": [
        {
            "name": "team",
            "description": "Data Resource",
            "externalDocs": {"description": "More info", "url": "http://example.com"},
        }
    ]
}


# Paths
paths_people_singular = {
    "paths": {
        "/people": {
            "get": {
                "tags": ["people"],
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
                                "schema": {"$ref": "#/components/schemas/AllPeople"}
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
                "tags": ["people"],
                "summary": "Create a new item",
                "requestBody": {"$ref": "#/components/requestBodies/People"},
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
        "/people/query": {
            "post": {
                "tags": ["people"],
                "summary": "Query for items",
                "requestBody": {"$ref": "#/components/requestBodies/People"},
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/AllPeople"}
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

paths_people_by_id = {
    "paths": {
        "/people/{id}": {
            "parameters": [{"$ref": "#/components/parameters/id"}],
            "get": {
                "tags": ["people"],
                "summary": "Get item by ID",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/People"}
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
                "tags": ["people"],
                "summary": "Replace item by ID",
                "requestBody": {"$ref": "#/components/requestBodies/People"},
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
                "tags": ["people"],
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
                "tags": ["people"],
                "summary": "Update data by ID",
                "requestBody": {"$ref": "#/components/requestBodies/People"},
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


paths_team_singular = {
    "paths": {
        "/team": {
            "get": {
                "tags": ["team"],
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
                                "schema": {"$ref": "#/components/schemas/AllTeam"}
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
                "tags": ["team"],
                "summary": "Create a new item",
                "requestBody": {"$ref": "#/components/requestBodies/Team"},
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
        "/team/query": {
            "post": {
                "tags": ["team"],
                "summary": "Query for items",
                "requestBody": {"$ref": "#/components/requestBodies/Team"},
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/AllTeam"}
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


paths_team_by_id = {
    "paths": {
        "/team/{id}": {
            "parameters": [{"$ref": "#/components/parameters/id"}],
            "get": {
                "tags": ["team"],
                "summary": "Get item by ID",
                "responses": {
                    "200": {
                        "description": "Success",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Team"}
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
                "tags": ["team"],
                "summary": "Replace item by ID",
                "requestBody": {"$ref": "#/components/requestBodies/Team"},
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
                "tags": ["team"],
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
                "tags": ["team"],
                "summary": "Update data by ID",
                "requestBody": {"$ref": "#/components/requestBodies/Team"},
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


paths_people_team_mn = {
    "paths": {
        "/people/{id}/team": {
            "parameters": [{"$ref": "#/components/parameters/id"}],
            "get": {
                "tags": ["people"],
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
                "tags": ["people"],
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
                "tags": ["people"],
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
        "/team/{id}/people": {
            "parameters": [{"$ref": "#/components/parameters/id"}],
            "get": {
                "tags": ["team"],
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
                "tags": ["team"],
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
                "tags": ["team"],
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


from deepmerge import always_merger
from copy import deepcopy


def merger(items: list):
    base = {}

    for item in items:
        base = deepcopy(base)
        result = always_merger.merge(base, item)

    return base


full_output = merger(
    [
        metadata,
        servers,
        component_parameters_base,
        component_schemas_base,
        component_schemas_people,
        component_schemas_team,
        component_schemas_mn,
        component_responses_base,
        component_responses_people,
        component_responses_team,
        component_responses_mn,
        component_request_bodies_people,
        component_request_bodies_team,
        component_request_bodies_mn,
        tags_people,
        tags_team,
        paths_people_singular,
        paths_people_by_id,
        paths_team_singular,
        paths_team_by_id,
        paths_people_team_mn,
    ]
)
