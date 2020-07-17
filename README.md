# Convert_descriptor_to_swagger

This tool generates an Open API 3.0 (swagger) spec from BrightHive tableschema descriptor files!

## Motivation (Why did we build this?)

[BrightHive](https://brighthive.io/) [Data Resources](https://github.com/brighthive/data-resource-generator) are set up using modified frictionless table schema descriptor files. [What is table schema?](https://frictionlessdata.io/specs/table-schema/).

This package will convert your set of descriptor files into a Open API 3.0 (swagger) spec. [What is Swagger?](https://swagger.io/docs/specification/about/)

This allows developers to generate and create clients easily that can easily interact with BrightHive Data Resources.

## How to use convert_descriptor_to_swagger

- Install the released version package from Github into your project with pip.

- Import the function `convert_descriptor_to_swagger`.

- Pass a list of descriptor files to it.

- Optionally pass an array of relationships. This will generate the many to many relationships.

- The function will return a swagger spec that can be used to build clients for your Data Resources.

### Many to many feature

The `convert_descriptor_to_swagger` function can optionally take a `relationships` list. It expects a list of relationship lists. This should look like the following:

`[["people", "team"], ["student", "classroom"]]`

The items within the "relationship list" should match the names of tables found in the descriptor file.

This will add both `/parent/{id}/child/` and `/child/{id}/parent` routes to your swagger file.

## How to develop convert_descriptor_to_swagger

> We welcome code contributions, suggestions, and reports! Please report bugs and make suggestions using Github issues. The BrightHive team will triage and prioritize your issue as soon as possible.

1. Install pipenv
1. Install docker and docker-compose
1. Clone the repo
1. Install production and development packages

    ```bash
    pipenv install --dev
    ```

1. Install pre-commit hooks

    ```bash
    pipenv run pre-commit install
    ```

### Quick note about pre-commit hooks

In the event that you want to run pre-commit hooks over the entire application use the following,

```bash
pipenv run pre-commit run --all-files
```

## Testing

Use `pipenv run pytest tests` to run the tests.

## Contributions

BrightHive welcomes and appreciates your contributions! Contribute by doing one (or more) of the following:

1. **Report a bug**
Did you encounter a bug? Please open [a descriptive issue on Github](https://github.com/brighthive/convert_descriptor_to_swagger/issues). We will respond as soon as we can.

2. **Request a feature**
You can request a feature by opening [an issue on Github](https://github.com/brighthive/convert_descriptor_to_swagger/issues), and if it seems viable, BrightHive will allocate development time to implement it.

3. **Create a pull request**
Check out a branch, push your commits to Github, and open a pull request. (N.b., you can either fork or clone the repo.) Add a detailed description of your changes, and finally, request a review from someone on the BrightHive team (see below).

> Read more about the open-source community [here](https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source), and learn more about creating a pull request [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github).

## Team

Names and titles of core contributors (including people who did not push code to Github). Use bullets, for example:

```
* Logan Ripplinger (Software Engineer)
```

## License

[MIT](LICENSE)
