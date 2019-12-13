credentials_descriptor = {
    "api": {
        "resource": "credentials",
        "methods": [
        {
            "get": {
            "enabled": True,
            "secured": False,
            "grants": ["get:users"]
            },
            "post": {
            "enabled": True,
            "secured": False,
            "grants": []
            },
            "put": {
            "enabled": True,
            "secured": False,
            "grants": []
            },
            "patch": {
            "enabled": True,
            "secured": False,
            "grants": []
            },
            "delete": {
            "enabled": True,
            "secured": False,
            "grants": []
            }
        }
        ]
    },
    "datastore": {
        "tablename": "credentials",
        "restricted_fields": [],
        "schema": {
        "fields": [
            {
            "name": "id",
            "title": "Credential ID",
            "type": "integer",
            "description": "Credential's unique identifier",
            "required": False
            },
            {
            "name": "credential_name",
            "title": "Credential Name",
            "type": "string",
            "description": "Credential's Name",
            "required": True
            }
        ],
        "primaryKey": "id"
        }
    }
}
