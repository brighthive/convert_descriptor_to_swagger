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
    paths_team_singular,
    paths_team_by_id,
)


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
    assert swag == paths_team_singular


def test_add_plural_methods():
    swag = add_plural_methods("people", {})
    assert swag == paths_team_by_id


# TODO update
# def test_generate_properties_from_desc():
#     descriptor = {
#         "datastore": {
#             "tablename": "test",
#             "restricted_fields": [],
#             "schema": {
#                 "fields": [
#                     {
#                         "name": "id",
#                         "title": "Test ID",
#                         "type": "integer",
#                         "description": "Test's unique identifier",
#                         "required": False,
#                     },
#                     {
#                         "name": "test_name",
#                         "title": "Test Name",
#                         "type": "string",
#                         "description": "Test's Name",
#                         "required": True,
#                     },
#                 ],
#                 "primaryKey": "id",
#             },
#         }
#     }

#     expected_output = {
#         "Test": {
#             "required": ["test_name"],
#             "type": "object",
#             "properties": {
#                 "id": {
#                     "type": "integer",
#                     "format": "int64",
#                     "description": "Test ID - Test's unique identifier",
#                     # "example": 1
#                 },
#                 "test_name": {
#                     "type": "string",
#                     "description": "Test Name - Test's Name",
#                     # "example": f"{sentence_case_name} 1"
#                 },
#             },
#             "description": "...",
#         }
#     }

#     output = generate_properties_from_desc("test", descriptor)
#     assert output == expected_output
