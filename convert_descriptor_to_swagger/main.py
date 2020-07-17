from convert_descriptor_to_swagger.base_tasks import (
    add_metadata,
    add_parameters,
    add_base_schemas,
    add_base_responses,
    add_servers,
)
from convert_descriptor_to_swagger.descriptor_tasks import (
    add_schemas_from_descriptor,
    add_request_bodies_from_descriptor,
    add_responses_from_descriptor,
    add_tags_from_descriptors,
    add_singular_methods,
    add_plural_methods,
)
from convert_descriptor_to_swagger.mn_tasks import (
    add_mn_schemas,
    add_mn_responses,
    add_mn_request_bodies,
    add_mn_paths,
)


def convert_descriptor_to_swagger(descriptors: list, relationships: list = []) -> dict:
    # First pass -- only need to add these items once
    swag = create_base_swag()

    # These items are added for each descriptor -- should take a list to iterate on
    for descriptor in descriptors:
        swag = process_descriptor(descriptor, swag)

    if relationships:
        if type(relationships[0]) is not list:
            relationships = list(relationships)

        swag = add_mn_schemas(swag)
        swag = add_mn_responses(swag)
        swag = add_mn_request_bodies(swag)

        for relationship in relationships:
            swag = add_mn_paths(relationship, swag)

    return swag


def create_base_swag() -> dict:
    swag = add_metadata({})
    swag = add_servers(swag)
    swag = add_parameters(swag)
    swag = add_base_schemas(swag)
    swag = add_base_responses(swag)
    return swag


def process_descriptor(descriptor: dict, swag: dict = {}) -> dict:
    # TODO add validation check on file

    # get resource name
    table_name = descriptor["datastore"]["tablename"]

    # add all of the components ---
    swag = add_schemas_from_descriptor(table_name, descriptor, swag)
    swag = add_request_bodies_from_descriptor(table_name, swag)
    swag = add_responses_from_descriptor(table_name, swag)
    swag = add_tags_from_descriptors(table_name, swag)
    swag = add_singular_methods(table_name, swag)
    swag = add_plural_methods(table_name, swag)

    return swag
