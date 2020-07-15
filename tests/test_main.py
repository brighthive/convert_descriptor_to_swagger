from convert_descriptor_to_swagger import convert_descriptor_to_swagger
from deepdiff import DeepDiff
from expects import expect, be_an, raise_error, have_property, equal, be_empty
from openapi_spec_validator import validate_spec
import json
import pytest
from tests.reference.full_output import people_output, full_output


def test_expected_output_is_valid():
    errors = validate_spec(full_output)
    assert errors == None


# E2E
@pytest.mark.xfail
def test_full_people_output(people_descriptor):
    swagger = convert_descriptor_to_swagger([people_descriptor])
    errors = validate_spec(swagger)

    assert errors == None
    assert swagger == people_output


@pytest.mark.xfail
def test_full_mn_output(people_descriptor, team_descriptor):
    descriptors = [people_descriptor, team_descriptor]
    swagger = convert_descriptor_to_swagger(descriptors, relations=["people", "team"])
    errors = validate_spec(swagger)

    assert errors == None
    assert swagger == full_output
