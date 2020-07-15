from convert_descriptor_to_swagger import convert_descriptor_to_swagger
from openapi_spec_validator import validate_spec
import pytest
from tests.reference.full_output import people_output, full_output


def test_expected_output_is_valid():
    errors = validate_spec(full_output)
    assert errors == None


# E2E
def test_full_people_output(people_descriptor):
    swagger = convert_descriptor_to_swagger([people_descriptor])
    assert swagger == people_output

    errors = validate_spec(swagger)
    assert errors == None


@pytest.mark.xfail
def test_full_mn_output(people_descriptor, team_descriptor):
    descriptors = [people_descriptor, team_descriptor]
    swagger = convert_descriptor_to_swagger(descriptors, relations=["people", "team"])
    assert swagger == full_output

    errors = validate_spec(swagger)
    assert errors == None
