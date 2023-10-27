# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Installation

You need at least Python 3.8 or higher.

Create a [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) first and then install dependencies with pip:

```bash
pip install -r requirements.txt
```

## Configuration

For configuration environment variables are used. Take a look at the file `.env-sample` to see what environment variables can be set.

You can set those variables either in your system directly. Optionally based on `.env-sample` you can also create a file `.env` and adjust it
accordingly.

## Execute

You can execute the `{{cookiecutter.script_name }}.py` like the following:

```bash
python {{cookiecutter.script_name }}.py
```

To get a list of all available options run the following:

```bash
python {{cookiecutter.script_name }}.py --help
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
