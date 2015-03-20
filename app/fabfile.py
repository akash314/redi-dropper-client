# The 'fabfile.py' is used by Fabric and must reside in the application root directory.

from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from contextlib import contextmanager


@task
def install_requirements():
    """
    Install required Python packages using pip and requirements.txt
    """
    local('pip install -r requirements.txt')


@task
def reset_db():
    """
    Drop all tables, Create empty tables, and populate tables
    """
    local('PYTHONPATH=. python redidropper/startup/db_manager.py')


@task
def test():
    """
    Run the automated test suite using py.test
    """
    local('py.test --tb=short -s tests/')


@task
def test_cov():
    """
    Run the automated test suite using py.test
    """
    local('py.test --tb=short -s  --cov redidropper  --cov-config tests/.coveragerc  --cov-report term-missing  tests/')


@task
def run():
    """
    Start the web application using a development WSGI webserver provided by Flask
    """
    local('python run.py')


@task
def deploy():
    """
    Deploy web application to Heroku.
    Requires: heroku git:remote -a PROJECTNAME
    """
    local('git push heroku master')


@contextmanager
def virtualenv(venv_name):
    with prefix('source ~/.virtualenvs/'+venv_name+'/bin/activate'):
        yield
