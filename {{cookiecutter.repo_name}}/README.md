# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Installation

You need at least Python 3.8 or higher.

Create a [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) first and then install dependencies with pip:

```bash
pip install -r requirements.txt
```

## Execute

You can execute the `{{cookiecutter.script_name }}.py` like the following:

```bash
python {{cookiecutter.script_name }}.py
```

## Development

### Setup environment

Install the development environment.

```bash
pip install -Ur dev-requirements.txt
```

### Setup pre-commit

pre-commit hooks is an additional option to check linting and formatting of code independent of an editor before you commit your changes with git.

```bash
pre-commit install
```
