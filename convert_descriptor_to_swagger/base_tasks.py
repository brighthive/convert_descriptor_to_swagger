from deepmerge import always_merger
from convert_descriptor_to_swagger.reference.full_output import (
    metadata,
    servers,
    component_parameters_base,
    component_schemas_base,
    component_responses_base,
)
from copy import deepcopy


def add_metadata(swag: dict = {}) -> dict:
    new = deepcopy(swag)
    always_merger.merge(new, metadata)
    return new


def add_servers(swag: dict = {}) -> dict:
    new = deepcopy(swag)
    always_merger.merge(new, servers)
    return new


def add_parameters(swag: dict = {}) -> dict:
    new = deepcopy(swag)
    always_merger.merge(new, component_parameters_base)
    return new


def add_base_schemas(swag: dict = {}) -> dict:
    new = deepcopy(swag)
    always_merger.merge(new, component_schemas_base)
    return new


def add_base_responses(swag: dict = {}) -> dict:
    new = deepcopy(swag)
    always_merger.merge(new, component_responses_base)
    return new
