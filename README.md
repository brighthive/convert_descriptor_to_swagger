# What is this

[BrightHive](https://brighthive.io/) [Data Resources](https://github.com/brighthive/data-resource-generator) are set up using modified frictionless table schema descriptor files. [What is table schema?](https://frictionlessdata.io/specs/table-schema/).

This package will convert your set of descriptor files into a Open API 3.0 (swagger) spec. [What is Swagger?](https://swagger.io/docs/specification/about/)

This allows developers to generate and create clients easily that can easily interact with BrightHive Data Resources.

## How to use

- Install the released version package from Github into your project with pip.

- Import the function `convert_descriptor_to_swagger`.

- Pass a list of descriptor files to it.

- Optionally pass an array of relationships. This will generate the many to many relationships.

- The function will return a swagger spec that can be used to build clients for your Data Resources.

### Many to many

The `convert_descriptor_to_swagger` function can optionally take a `relationships` list. It expects a list of relationship lists. This should look like the following:

`[["people", "team"], ["student", "classroom"]]`

The items within the "relationship list" should match the names of tables found in the descriptor file.

This will add both `/parent/{id}/child/` and `/child/{id}/parent` routes to your swagger file.

## Developers

### Run tests

Use `pipenv run pytest tests` to run the tests.
