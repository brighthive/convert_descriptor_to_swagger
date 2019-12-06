from convert_descriptor_to_swagger.base_tasks import add_metadata, add_parameters, add_base_schemas
from convert_descriptor_to_swagger.descriptor_tasks import add_schemas_from_descriptor


def convert_descriptor_to_swagger(descriptor: dict) -> dict:
    # First pass -- only need to add these items once
    swag = add_metadata()
    swag = add_parameters(swag)
    swag = add_base_schemas(swag)


    # These items are added for each descriptor -- should take a list to iterate on
    swag = process_descriptor(descriptor, swag)

    return swag


def process_descriptor(descriptor: dict, swag: dict) -> dict:
    # get resource name
    assert descriptor['datastore']['tablename'] == descriptor['api']['resource'], "Expected datastore.tablename to equal api.resource"
    
    name = descriptor['datastore']['tablename']

    # add all of the components
    # add schemas
    swag = add_schemas_from_descriptor(name, swag)

    # add requestBody
    # add responses
    # add the paths
    # add tags
    return swag
