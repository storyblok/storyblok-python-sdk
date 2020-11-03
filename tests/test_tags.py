import pytest
import storyblok

public_token  = "KOesmZuJLW2Yy7QJcMuFPQtt"

@pytest.fixture
def tags():
    client = storyblok.Client()
    return client.tags()

def test_tags_list(tags):
    response = tags.list(public_token)

    assert response.code == 200
    assert 'tags' in response.body.keys()
    assert type(response.body['tags']) is list

    first_tag = response.body['tags'][0]
    assert 'name'           in first_tag.keys()
    assert 'taggings_count' in first_tag.keys()
