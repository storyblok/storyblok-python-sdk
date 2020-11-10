import pytest
import storyblok
import os

user_token = os.getenv('USER_TOKEN')

@pytest.fixture
def client():
    return storyblok.Client()

def test_get(client):
    response = client.get('/spaces/91322/tags/',auth_token=user_token)

    assert response.code == 200
    assert 'tags' in response.body.keys()
    assert type(response.body['tags']) is list

    first_tag = response.body['tags'][0]
    assert 'name'           in first_tag.keys()
    assert 'taggings_count' in first_tag.keys()

def test_post(client):
    story_params = { "story": { "name": "my awesome new story" } }

    response = client.post('/spaces/91322/stories/', auth_token=user_token, params=story_params)
    assert response.code == 201
    story = response.body['story']
    assert 'name'           in story.keys()
    assert story['name'] == story_params['story']['name']

def test_put(client):
    story_params = { "story": { "name": "my awesome new story name" } }

    response = client.put('/spaces/91322/stories/26392879', auth_token=user_token, params=story_params)
    assert response.code == 200
    story = response.body['story']
    assert 'name'           in story.keys()
    assert story['name'] == story_params['story']['name']

def test_delete(client):
    # creates a story to be deleted by the test
    story_params = { "story": { "name": "my awesome new story" } }
    story_create_response = client.post('/spaces/91322/stories/', auth_token=user_token, params=story_params)

    story_id = story_create_response.body['story']['id']
    response = client.delete('/spaces/91322/stories/'+ str(story_id), auth_token=user_token)
    assert response.code == 200
    story = response.body['story']
    assert 'name'           in story.keys()
    assert story['name'] == story_params['story']['name']
