# What is this?
[BrightHive Data Resources](https://github.com/brighthive/data-resource-api) are set up using modified frictionless table schema descriptor files. [What is table schema?](https://frictionlessdata.io/specs/table-schema/).

This package will convert your descriptor files into a swagger spec. [What is Swagger?](https://swagger.io/docs/specification/about/)

This allows developers to generate and create clients easily that can easily interact with Data Resource APIs.

# How to use
Install the package into your project with pip.

Import the function `convert_descriptor_to_swagger`.

Pass a list of descriptor files to it.

It will generate a swagger spec that can be used to build clients for your Data Resources.

# Developers
## Run tests
Use `pipenv run pytest tests` to run the tests.
