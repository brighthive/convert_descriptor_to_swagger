from deepmerge import always_merger
from convert_descriptor_to_swagger.reference.full_output import (
    metadata,
    servers,
    component_parameters_base,
    component_schemas_base,
    component_responses_base,
)


def add_metadata(swag: dict = {}) -> dict:
    always_merger.merge(swag, metadata)
    return swag


def add_servers(swag: dict = {}) -> dict:
    always_merger.merge(swag, servers)
    return swag


def add_parameters(swag: dict = {}) -> dict:
    always_merger.merge(swag, component_parameters_base)
    return swag


def add_base_schemas(swag: dict = {}) -> dict:
    always_merger.merge(swag, component_schemas_base)
    return swag


def add_base_responses(swag: dict = {}) -> dict:
    always_merger.merge(swag, component_responses_base)
    return swag
