from convert_descriptor_to_swagger import convert_descriptor_to_swagger
from tests.descriptors.credentials import credentials_descriptor
from tests.descriptors.programs import programs_descriptor
import yaml
from expects import expect, be_an, raise_error, have_property, equal, be_empty
import os
import json


def load_swagger():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'swagger/dr.yaml')

    with open(filename) as file:
        dr_swagger = yaml.load(file, Loader=yaml.FullLoader)

        print(json.dumps(dr_swagger, indent=4))
    
    return dr_swagger


def test_load_desc():
    swagger = load_swagger()

    output = convert_descriptor_to_swagger(credentials_descriptor)

    expect(output).to(equal(swagger))
