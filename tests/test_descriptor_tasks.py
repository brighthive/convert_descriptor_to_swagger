from convert_descriptor_to_swagger.descriptor_tasks import (
    add_schemas_from_descriptor,
    add_request_bodies_from_descriptor,
    add_responses_from_descriptor,
    add_tags_from_descriptors,
    add_singular_methods,
    add_plural_methods,
    generate_properties_from_desc,
)
from tests.reference.full_output import (
    component_schemas_people,
    component_responses_people,
    component_request_bodies_people,
    tags_people,
    tags_team,
    paths_people_singular,
    paths_people_by_id,
)
from copy import deepcopy
from deepmerge import always_merger

# TODO update
# should generate list of required items
# should generate no list of required items if none are required
# should select correct type


# Helper func tests
def test_generate_properties_from_desc_with_required():
    required_descriptor = {
        "datastore": {
            "tablename": "test",
            "restricted_fields": [],
            "schema": {
                "fields": [
                    {
                        "name": "id",
                        "title": "Test ID",
                        "type": "integer",
                        "description": "Test's unique identifier",
                        "constraints": {},
                    },
                    {
                        "name": "name",
                        "title": "Test Name",
                        "type": "string",
                        "description": "Test's Name",
                        "constraints": {"required": True},
                    },
                ],
                "primaryKey": "id",
            },
        }
    }

    expected_output = {
        "Test": {
            "required": ["name"],
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "format": "int64",
                    "description": "Test ID - Test's unique identifier",
                },
                "name": {"type": "string", "description": "Test Name - Test's Name"},
            },
        }
    }

    output = generate_properties_from_desc("test", required_descriptor)
    assert output == expected_output


def test_generate_properties_from_desc_without_required():
    not_required_descriptor = {
        "datastore": {
            "tablename": "test",
            "restricted_fields": [],
            "schema": {
                "fields": [
                    {
                        "name": "id",
                        "title": "Test ID",
                        "type": "integer",
                        "description": "Test's unique identifier",
                        "constraints": {},
                    },
                    {
                        "name": "name",
                        "title": "Test Name",
                        "type": "string",
                        "description": "Test's Name",
                    },
                ],
                "primaryKey": "id",
            },
        }
    }

    expected_output = {
        "Test": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "format": "int64",
                    "description": "Test ID - Test's unique identifier",
                },
                "name": {"type": "string", "description": "Test Name - Test's Name"},
            },
        }
    }

    output = generate_properties_from_desc("test", not_required_descriptor)
    assert output == expected_output


# Process tests
def test_add_schemas_from_descriptor(people_descriptor):
    swag = add_schemas_from_descriptor("people", people_descriptor)
    assert swag == component_schemas_people


def test_add_responses_from_descriptor():
    swag = add_responses_from_descriptor("people", {})
    assert swag == component_responses_people


# TODO should handle required?
def test_add_request_bodies_from_descriptor():
    swag = add_request_bodies_from_descriptor("people", {})
    assert swag == component_request_bodies_people


def test_add_tags_from_descriptor():
    swag = add_tags_from_descriptors("people", {})
    assert swag == tags_people

    # Add teams to tags and ensure people is preserved
    swag = add_tags_from_descriptors("team", swag)
    tags_people_copy = deepcopy(tags_people)
    people_and_team_tags = always_merger.merge(tags_people_copy, tags_team)

    assert swag == people_and_team_tags


# TODO what is this?
# def test_add_tags_from_descriptor_with_items():
#     expected_output = {
#         "tags": [
#             {"name": "test1"},
#             {
#                 "name": "test",
#                 "description": "...",
#                 "externalDocs": {
#                     "description": "Find out more",
#                     "url": "http://swagger.io",
#                 },
#             },
#         ]
#     }

#     swag = add_tags_from_descriptors("test", {"tags": [{"name": "test1"}]})
#     assert swag == expected_output


def test_add_singular_methods():
    swag = add_singular_methods("people", {})
    assert swag == paths_people_singular


def test_add_plural_methods():
    swag = add_plural_methods("people", {})
    assert swag == paths_people_by_id
