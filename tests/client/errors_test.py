import pytest
import lokalise


@pytest.mark.vcr
def test_not_found(client):
    with pytest.raises(lokalise.errors.NotFound) as excinfo:
        client.project("123/invalid/")

    assert excinfo.value.args[1] == 404


@pytest.mark.vcr
def test_unknown_error(client):
    with pytest.raises(lokalise.errors.ClientError) as excinfo:
        client.project("very/invalid/path")

    assert excinfo.value.args[1] == 407


@pytest.mark.vcr
def test_invalid_client():
    invalid_client = lokalise.Client("invalid")
    with pytest.raises(lokalise.errors.BadRequest) as excinfo:
        invalid_client.projects()

    assert excinfo.value.args[1] == 400
