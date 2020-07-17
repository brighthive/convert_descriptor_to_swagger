from convert_descriptor_to_swagger import convert_descriptor_to_swagger
from openapi_spec_validator import validate_spec
from convert_descriptor_to_swagger.reference.full_output import (
    people_output,
    full_output,
)
from copy import deepcopy


def test_expected_output_is_valid():
    output = deepcopy(full_output)
    errors = validate_spec(output)
    assert errors is None


def test_full_people_output_is_valid_and_expected(people_descriptor):
    swagger = convert_descriptor_to_swagger([people_descriptor])
    assert swagger == people_output

    output = deepcopy(swagger)
    errors = validate_spec(output)
    assert errors is None


def test_full_mn_output_is_valid_and_expected(people_descriptor, team_descriptor):
    descriptors = [people_descriptor, team_descriptor]
    swagger = convert_descriptor_to_swagger(descriptors, [["people", "team"]])

    assert swagger == full_output

    output = deepcopy(swagger)
    errors = validate_spec(output)
    assert errors is None
