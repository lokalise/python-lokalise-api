import pytest

@pytest.mark.vcr
def test_all_projects(client):
    p = client.projects()
    print(p.items[0].project_id)
    print(p.total_count)
    assert True == True
