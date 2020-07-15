from convert_descriptor_to_swagger import convert_descriptor_to_swagger
from deepdiff import DeepDiff
from expects import expect, be_an, raise_error, have_property, equal, be_empty
from openapi_spec_validator import validate_spec
import json


# def test_produces_valid_swagger(program_descriptor, credential_descriptor):
#     descriptors = [program_descriptor, credential_descriptor]

#     swagger = convert_descriptor_to_swagger(descriptors, relations=['program','credential'])
#     # print(json.dumps(swagger, indent=4))

#     output = validate_spec(swagger)
#     expect(output).to(equal(None))
