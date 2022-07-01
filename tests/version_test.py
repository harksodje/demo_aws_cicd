import pytest


@pytest.fixture
def project_name():
    return 'Demo CI/CD'


def test_version(project_name):
    assert project_name == 'Demo CI/CD'
    assert isinstance(project_name, str)
