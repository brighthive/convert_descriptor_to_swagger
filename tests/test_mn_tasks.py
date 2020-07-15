from convert_descriptor_to_swagger.mn_tasks import (
    add_mn_schemas,
    add_mn_responses,
    add_mn_request_bodies,
    add_mn_paths,
)
from tests.reference.full_output import (
    component_schemas_mn,
    component_responses_mn,
    component_request_bodies_mn,
    paths_people_team_mn,
)

# from copy import deepcopy
# from deepmerge import always_merger
import pytest


@pytest.mark.xfail
def test_add_mn_schemas():
    swag = add_mn_schemas(["people", "team"], {})
    assert swag == component_schemas_mn


@pytest.mark.xfail
def test_add_mn_responses():
    swag = add_mn_schemas(["people", "team"], {})
    assert swag == component_responses_mn


@pytest.mark.xfail
def test_add_mn_request_bodies():
    swag = add_mn_request_bodies(["people", "team"], {})
    assert swag == component_request_bodies_mn


@pytest.mark.xfail
def test_add_mn_paths():
    swag = add_mn_paths(["people", "team"], {})
    assert swag == paths_people_team_mn