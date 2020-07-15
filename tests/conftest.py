import pytest
import os
import yaml
from tests.reference.full_output import full_output


# # I believe this was an easy way to test/actually generate real swagger docs
# @pytest.fixture
# def swagger():
#     dirname = os.path.dirname(__file__)
#     filename = os.path.join(dirname, 'swagger/dr.yaml')

#     with open(filename) as file:
#         dr_swagger = yaml.load(file, Loader=yaml.FullLoader)

#         # print(json.dumps(dr_swagger, indent=4))

#     return dr_swagger


@pytest.fixture
def expected_output():
    return full_output


@pytest.fixture
def credential_descriptor():
    credential_descriptor = {
        "api": {
            "resource": "credential",
            "methods": [
                {
                    "get": {"enabled": True, "secured": False, "grants": ["get:users"]},
                    "post": {"enabled": True, "secured": False, "grants": []},
                    "put": {"enabled": True, "secured": False, "grants": []},
                    "patch": {"enabled": True, "secured": False, "grants": []},
                    "delete": {"enabled": True, "secured": False, "grants": []},
                }
            ],
        },
        "datastore": {
            "tablename": "credential",
            "restricted_fields": [],
            "schema": {
                "fields": [
                    {
                        "name": "id",
                        "title": "Credential ID",
                        "type": "integer",
                        "description": "Credential's unique identifier",
                        "required": False,
                    },
                    {
                        "name": "credential_name",
                        "title": "Credential Name",
                        "type": "string",
                        "description": "Credential's Name",
                        "required": True,
                    },
                ],
                "primaryKey": "id",
            },
        },
    }
    return credential_descriptor


@pytest.fixture
def program_descriptor():
    program_descriptor = {
        "api": {
            "resource": "program",
            "methods": [
                {
                    "get": {"enabled": True, "secured": False, "grants": ["get:users"]},
                    "post": {
                        "enabled": True,
                        "secured": False,
                        "grants": ["get:users"],
                    },
                    "put": {"enabled": True, "secured": True, "grants": ["get:users"]},
                    "patch": {
                        "enabled": True,
                        "secured": True,
                        "grants": ["get:users"],
                    },
                    "delete": {
                        "enabled": True,
                        "secured": True,
                        "grants": ["get:users"],
                    },
                    "custom": [
                        {
                            "resource": "/program/credential",
                            "methods": [
                                {
                                    "get": {
                                        "enabled": True,
                                        "secured": False,
                                        "grants": ["get:users"],
                                    },
                                    "put": {
                                        "enabled": True,
                                        "secured": False,
                                        "grants": [],
                                    },
                                    "patch": {
                                        "enabled": True,
                                        "secured": False,
                                        "grants": [],
                                    },
                                    "delete": {
                                        "enabled": True,
                                        "secured": False,
                                        "grants": [],
                                    },
                                }
                            ],
                        }
                    ],
                }
            ],
        },
        "datastore": {
            "tablename": "program",
            "restricted_fields": [],
            "schema": {
                "fields": [
                    {
                        "name": "id",
                        "title": "Program ID",
                        "type": "integer",
                        "description": "Program's unique identifier",
                        "required": False,
                    },
                    {
                        "name": "program_name",
                        "title": "Program Name",
                        "type": "string",
                        "description": "Program's name.",
                        "required": True,
                    },
                    {
                        "name": "program_code",
                        "title": "Program Code",
                        "type": "integer",
                        "description": "Program's Code",
                        "required": True,
                    },
                    {
                        "name": "program_description",
                        "title": "Program Description",
                        "type": "string",
                        "description": "Program's Description",
                        "required": True,
                    },
                    {
                        "name": "program_status",
                        "title": "Program Status",
                        "type": "string",
                        "description": "Program's Status",
                        "required": True,
                    },
                    {
                        "name": "program_fees",
                        "title": "Program Fees",
                        "type": "number",
                        "description": "Program's tuition fees",
                        "required": True,
                    },
                    {
                        "name": "eligibility_criteria",
                        "title": "Eligibility Criteria",
                        "type": "string",
                        "description": "Program's eligibility criteria",
                        "required": True,
                    },
                    {
                        "name": "program_url",
                        "title": "Program URL",
                        "type": "string",
                        "format": "uri",
                        "description": "Program's webpage url",
                        "required": True,
                    },
                    {
                        "name": "program_contact_phone",
                        "title": "Program Contact Phone",
                        "type": "string",
                        "description": "Program's contact telephone",
                        "required": False,
                    },
                    {
                        "name": "program_contact_email",
                        "title": "Program Contact Email",
                        "type": "string",
                        "format": "email",
                        "description": "Program's contact email address",
                        "required": False,
                    },
                    {
                        "name": "languages",
                        "title": "Languages",
                        "type": "string",
                        "description": "Languages the program is offered in",
                        "required": False,
                    },
                    {
                        "name": "current_intake_capacity",
                        "title": "Current Intake Capacity",
                        "type": "integer",
                        "description": "Current intake capacity of the program",
                        "required": False,
                    },
                    {
                        "name": "program_offering_model",
                        "title": "Program Offering Model",
                        "type": "integer",
                        "description": "The program's current offering model",
                        "required": False,
                    },
                    {
                        "name": "program_length_hours",
                        "title": "Program Length (Hours)",
                        "type": "number",
                        "description": "Length of the program (in hours)",
                        "required": False,
                    },
                    {
                        "name": "program_length_weeks",
                        "title": "Program Length (Weeks)",
                        "type": "number",
                        "description": "Length of the program (in weeks)",
                        "required": False,
                    },
                    {
                        "name": "program_soc",
                        "title": "Program SOC",
                        "type": "integer",
                        "description": "Program SOC",
                        "required": False,
                    },
                    {
                        "name": "funding_sources",
                        "title": "Funding Source",
                        "type": "string",
                        "description": "The program's funding source",
                        "required": False,
                    },
                    {
                        "name": "on_etpl",
                        "title": "On ETPL",
                        "type": "integer",
                        "description": "Whether or not the student is on ETPL",
                        "required": False,
                    },
                    {
                        "name": "cost_of_books_and_supplies",
                        "title": "Cost of Books and Supplies",
                        "type": "number",
                        "description": "Cost of Books and Supplies",
                        "required": False,
                    },
                    {
                        "name": "provider_id",
                        "title": "Provider ID",
                        "type": "integer",
                        "description": "Foreign key for provider",
                        "required": False,
                    },
                    {
                        "name": "location_id",
                        "title": "Provider ID",
                        "type": "integer",
                        "description": "Foreign key for provider",
                        "required": False,
                    },
                    {
                        "name": "credential_earned",
                        "title": "Provider ID",
                        "type": "integer",
                        "description": "Foreign key for provider",
                        "required": False,
                    },
                    {
                        "name": "potential_outcome_id",
                        "title": "Provider ID",
                        "type": "integer",
                        "description": "Foreign key for provider",
                        "required": False,
                    },
                    {
                        "name": "prerequisite_id",
                        "title": "Provider ID",
                        "type": "integer",
                        "description": "Foreign key for provider",
                        "required": False,
                    },
                ],
                "primaryKey": "id",
                "foreignKeys": [
                    {
                        "fields": ["provider_id"],
                        "reference": {"resource": "providers", "fields": ["id"]},
                    },
                    {
                        "fields": ["location_id"],
                        "reference": {"resource": "locations", "fields": ["id"]},
                    },
                    {
                        "fields": ["credential_earned"],
                        "reference": {"resource": "credential", "fields": ["id"]},
                    },
                    {
                        "fields": ["potential_outcome_id"],
                        "reference": {
                            "resource": "program_potential_outcomes",
                            "fields": ["id"],
                        },
                    },
                    {
                        "fields": ["prerequisite_id"],
                        "reference": {
                            "resource": "program_prerequisites",
                            "fields": ["id"],
                        },
                    },
                ],
            },
        },
    }
    return program_descriptor
