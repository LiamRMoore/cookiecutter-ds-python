{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------
    .
    ├── bin/                                  <- Executable scripts directory
{%- if cookiecutter.use_aws_ec2_instance.lower() == "y" -%}
    │   ├── connect_to_aws                    <- Connect to AWS EC2 instance
    │   ├── connect_to_notebook               <- Open a connection to jupyter notebook port on EC2 instance
    │   └── update_ssh_config                  <- Update your ssh config file with current instance IP
{% endif %}
    │
    ├── config.yml                             <- configuration file for global project variables
    │
    ├── {{ cookiecutter.python_module_name }} <- The python package, **install with 'pip install -e .'**
    │   ├── config.py                          <- Makes config.yml variables accessible in {{ cookiecutter.python_module_name }}.config namespace
    │   └── models/                           <- store ML models
    │
    ├── data                                  <- Data dump
    │   ├── intermediate                      <- Intermediate data e.g. serialised arrays
    │   ├── processed                         <- Data ready-for-training/inference
    │   ├── raw                               <- Raw data - should be immutable
    │   └── volumes                           <- Mirrored drives
    │
    ├── docker-compose.yml          <- Start-up configuration for docker container
    │
    ├── Dockerfile                   <- Instructions for building docker image
    │
    ├── envs                        <- conda virtual environment definition files
    │   ├── {{cookiecutter.python_module_name}}_cpu_env.yml
    │   └── {{cookiecutter.python_module_name}}_gpu_env.yml
    │
    ├── figures                      <- Figures saved by scripts or notebooks.
    │
    ├── LICENSE
    │
    ├── Makefile                     <- Makefile with commands like `make environment`
    │
    ├── notebooks/                  <- Jupyter notebooks
    │
    ├── output/                     <- Manipulated data, logs, etc.
    │
    ├── README.md                   <- The top-level README for developers using this project.
    │
    ├── setup.py
    │
    ├── tests                       <- Unit tests.
    │
    └── tox.ini                     <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</p>


Set up
------------

Install the virtual environment with conda and activate it:

```bash
$ conda env create -f environment.yml
$ conda activate example-project
```

Install `{{ cookiecutter.python_module_name }}` in the virtual environment:

```bash
$ pip install --editable .
```
