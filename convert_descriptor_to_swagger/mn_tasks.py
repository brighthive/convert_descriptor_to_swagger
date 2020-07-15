# from copy import deepcopy
from deepmerge import always_merger
from tests.reference.full_output import (
    component_schemas_mn,
    component_responses_mn,
    component_request_bodies_mn,
    paths_people_team_mn,
)


def add_mn_schemas(swag: dict = {}) -> dict:
    swag = always_merger.merge(swag, component_schemas_mn)
    return swag


def add_mn_responses(swag: dict = {}) -> dict:
    swag = always_merger.merge(swag, component_responses_mn)
    return swag


def add_mn_request_bodies(relationship: list, swag: dict = {}) -> dict:
    return swag


def add_mn_paths(relationship: list, swag: dict = {}) -> dict:
    return swag
