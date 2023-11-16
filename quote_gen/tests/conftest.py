import pytest
from app import app

@pytest.fixture()
def setup():
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(setup):
    return setup.test_client()


@pytest.fixture()
def runner(setup):
    return setup.test_cli_runner()