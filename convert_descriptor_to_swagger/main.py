from convert_descriptor_to_swagger.base_tasks import (
    add_metadata,
    add_parameters,
    add_base_schemas,
    add_base_responses)
from convert_descriptor_to_swagger.descriptor_tasks import (
    add_schemas_from_descriptor,
    add_request_bodies_from_descriptor,
    add_responses_from_descriptor,
    add_tags_from_descriptors,
    add_singular_methods,
    add_plural_methods
    )


def convert_descriptor_to_swagger(descriptor: dict) -> dict:
    # First pass -- only need to add these items once
    swag = add_metadata()
    swag = add_parameters(swag)
    swag = add_base_schemas(swag)
    swag = add_base_responses(swag)

    # These items are added for each descriptor -- should take a list to iterate on
    swag = process_descriptor(descriptor, swag)

    return swag


def process_descriptor(descriptor: dict, swag: dict) -> dict:
    # get resource name
    assert descriptor['datastore']['tablename'] == descriptor['api']['resource'], "Expected datastore.tablename to equal api.resource"
    _name = descriptor['datastore']['tablename']

    assert _name[-1].lower() == 's', f"Expected {_name} to be plural and end in an 's'."
    singular_name = _name[0:-1] # Remove the s

    # add all of the components ---
    # add schemas
    swag = add_schemas_from_descriptor(singular_name, swag)

    # add requestBody
    swag = add_request_bodies_from_descriptor(singular_name, swag)

    # add responses
    swag = add_responses_from_descriptor(singular_name, swag)

    # add tags
    swag = add_tags_from_descriptors(singular_name, swag)

    # add the paths
    swag = add_singular_methods(singular_name, swag)
    swag = add_plural_methods(singular_name, swag)
    
    return swag
