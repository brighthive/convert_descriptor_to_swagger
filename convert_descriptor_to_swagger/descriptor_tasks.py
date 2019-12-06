


# def add_schemas_from_descriptor():
#     if 'components' not in swag:
#         swag['components'] = {}

#     if 'schema' not in swag['components']:
#         swag['components'].update({'schema': {}})

#     if 'components' not in swag:
#         swag['components'] = {}
    
#     if 'schemas' not in swag['components']:
#         swag['components']['schemas'] = {}

#     swag['components']['schemas'].update({
#         "Credential": {
#             "required": [
#                 "name"
#             ],
#             "type": "object",
#             "properties": {
#                 "id": {
#                     "type": "integer",
#                     "description": "...",
#                     "format": "int64",
#                     "example": 1
#                 },
#                 "name": {
#                     "type": "string",
#                     "description": "...",
#                     "example": "Credential 1"
#                 }
#             },
#             "description": "..."
#         },
#         "AllCredentials": {
#             "type": "object",
#             "properties": {
#                 "credentials": {
#                     "type": "array",
#                     "items": {
#                         "$ref": "#/components/schemas/Credential"
#                     }
#                 },
#                 "links": {
#                     "type": "array",
#                     "items": {
#                         "$ref": "#/components/schemas/Links"
#                     }
#                 }
#             },
#             "description": "..."
#         }
#     }