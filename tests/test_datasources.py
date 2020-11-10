import pytest
import storyblok

public_token  = "KOesmZuJLW2Yy7QJcMuFPQtt"

@pytest.fixture
def datasources():
    client = storyblok.Client()
    return client.datasources()

def test_datasource_list(datasources):
    response = datasources.list(public_token)
    assert response.code == 200
    assert 'datasources' in response.body.keys()
    assert type(response.body['datasources']) is list

    first_datasource = response.body['datasources'][0]
    assert 'id'           in first_datasource.keys()
    assert 'name'         in first_datasource.keys()
    assert 'slug'         in first_datasource.keys()
    assert 'dimensions'   in first_datasource.keys()


def test_datasource_single(datasources):
    response = datasources.single(public_token, '23537')
    assert response.code == 200
    assert 'datasource' in response.body.keys()

    datasource = response.body['datasource']
    assert 'id'           in datasource.keys()
    assert 'name'         in datasource.keys()
    assert 'slug'         in datasource.keys()
    assert 'dimensions'   in datasource.keys()
