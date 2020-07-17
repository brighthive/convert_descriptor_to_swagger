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




# NAME OF APP
One sentence explanation of the tool.

## Motivation (Why did we build this?)
Why did BrightHive build this?

## Demo (or Features)
What does this tool do? Include screenshots and/or GIFs.

Alternatively, this section may enumerate the features of the app. Use bullet points.

## How to use [NAME OF APP]
[OPTIONAL] This section describes how to use the app, e.g., how to install it via `pip`, how to configure it, how to execute useful functions, etc. This section is necessary for libraries and scripts, but may not be useful for web APIs. 

## How to develop [NAME OF APP]
**Alternatively, you can call this section "Getting Started" – the preferred header if you omit "How to use."** 

This section should provide instructions for running the app locally: requirements, docker, virtualenv management, etc. Future BrightHive developers need this section, in particular! But this section can also be beneficial to off-the-street open source developers. For this reason, please include the following text somewhere:

> We welcome code contributions, suggestions, and reports! Please report bugs and make suggestions using Github issues. The BrightHive team will triage and prioritize your issue as soon as possible.

## Testing
How do I run tests? (And what libraries did we use to write said tests?)

## Contributions

BrightHive welcomes and appreciates your contributions! Contribute by doing one (or more) of the following:

1. **Report a bug** <br>
Did you encounter a bug? Please open [a descriptive issue on Github](<link-to-repo-issues>). We will respond as soon as we can.

2. **Request a feature** <br>
You can request a feature by opening [an issue on Github](<link-to-repo-issues>), and if it seems viable, BrightHive will allocate development time to implement it.  

3. **Create a pull request** <br>
Check out a branch, push your commits to Github, and open a pull request. (N.b., you can either fork or clone the repo.) Add a detailed description of your changes, and finally, request a review from someone on the BrightHive team (see below). 

> Read more about the open-source community [here](https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source), and learn more about creating a pull request [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github).

## Team
Names and titles of core contributors (including people who did not push code to Github). Use bullets, for example:

```
* Regina Compton (Software Engineer)
* Logan Ripplinger (Software Engineer)
* Sarah Henry (User Experience Researcher and Strategist)
```

## License
Include a link to the LICENSE.md file in your repo. 
