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


def convert_descriptor_to_swagger(descriptors: list, **kwags) -> dict:
    # First pass -- only need to add these items once
    swag = create_base_swag()

    # These items are added for each descriptor -- should take a list to iterate on
    for descriptor in descriptors:
        swag = process_descriptor(descriptor, swag)

    try:
        if kwargs["relationships"]:
            # Add base mn items
            swag = add_mn_schemas(swag)
            # Add mn responses
            swag = add_mn_responses(relationship, swag)

            for relationship in kwargs["relationships"]:
                swag = process_mn(relationship, swag)

    except NameError:
        pass

    return swag


def create_base_swag() -> dict:
    swag = add_metadata({})
    swag = add_servers(swag)
    swag = add_parameters(swag)
    swag = add_base_schemas(swag)
    swag = add_base_responses(swag)
    return swag


def process_descriptor(descriptor: dict, swag: dict = {}) -> dict:
    # get resource name
    # assert (
    #     descriptor["datastore"]["tablename"] == descriptor["api"]["resource"]
    # ), "Expected datastore.tablename to equal api.resource"
    table_name = descriptor["datastore"]["tablename"]

    # add all of the components ---
    # add schemas
    swag = add_schemas_from_descriptor(table_name, descriptor, swag)

    # add requestBody
    swag = add_request_bodies_from_descriptor(table_name, swag)

    # add responses
    swag = add_responses_from_descriptor(table_name, swag)

    # add tags
    swag = add_tags_from_descriptors(table_name, swag)

    # add the paths
    swag = add_singular_methods(table_name, swag)
    swag = add_plural_methods(table_name, swag)

    return swag


def process_mn(relationship: list, swag: dict = {}) -> dict:

    # Add mn request bodies
    # component_request_bodies_mn
    swag = add_mn_request_bodies(relationship, swag)

    # Add mn paths
    # paths_people_team_mn
    swag = add_mn_paths(relationship, swag)

    return swag
