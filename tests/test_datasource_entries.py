import pytest
import storyblok

public_token  = "KOesmZuJLW2Yy7QJcMuFPQtt"

@pytest.fixture
def datasource_entries():
    client = storyblok.Client()
    return client.datasource_entries()

def test_datasource_entries_list(datasource_entries):
    response = datasource_entries.list(public_token)

    assert response.code == 200
    assert 'datasource_entries' in response.body.keys()
    assert type(response.body['datasource_entries']) is list

    first_datasource_entry = response.body['datasource_entries'][0]
    assert 'id'              in first_datasource_entry.keys()
    assert 'name'            in first_datasource_entry.keys()
    assert 'value'           in first_datasource_entry.keys()
    assert 'dimension_value' in first_datasource_entry.keys()
