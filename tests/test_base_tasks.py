from convert_descriptor_to_swagger.base_tasks import (
    add_metadata,
    add_parameters,
    add_base_schemas,
    add_base_responses,
    add_servers,
)
from convert_descriptor_to_swagger.reference.full_output import (
    metadata,
    servers,
    component_parameters_base,
    component_schemas_base,
    component_responses_base,
)


def test_add_metadata():
    swag = add_metadata()
    assert swag == metadata


def test_add_servers():
    swag = add_servers({})
    assert swag == servers


def test_add_parameters():
    swag = add_parameters({})
    assert swag == component_parameters_base


def test_add_base_schemas():
    swag = add_base_schemas({})
    assert swag == component_schemas_base


def test_add_base_responses():
    swag = add_base_responses({})
    assert swag == component_responses_base
