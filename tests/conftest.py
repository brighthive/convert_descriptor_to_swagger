import pytest
import os
import yaml


@pytest.fixture
def swagger():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'swagger/dr.yaml')

    with open(filename) as file:
        dr_swagger = yaml.load(file, Loader=yaml.FullLoader)

        # print(json.dumps(dr_swagger, indent=4))
    
    return dr_swagger