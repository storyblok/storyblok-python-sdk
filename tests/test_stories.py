import pytest
import storyblok

public_token  = "KOesmZuJLW2Yy7QJcMuFPQtt"
preview_token = "Nb8l74hQYP1hrrIA0lE7Lwtt"

@pytest.fixture
def stories():
    client = storyblok.Client()
    return client.stories()

def test_stories_list_published(stories):
    response = stories.list(public_token)

    assert response.code == 200
    assert 'stories' in response.body.keys()
    assert type(response.body['stories']) is list

    first_story = response.body['stories'][0]
    assert 'id'           in first_story.keys()
    assert 'name'         in first_story.keys()
    assert 'created_at'   in first_story.keys()
    assert 'published_at' in first_story.keys()
    assert 'uuid'         in first_story.keys()
    assert 'content'      in first_story.keys()
    assert 'slug'         in first_story.keys()
    assert 'full_slug'    in first_story.keys()
    assert 'tag_list'     in first_story.keys()

def test_stories_list_draft(stories):
    response = stories.list(preview_token, { "version": "draft"})

    assert response.code == 200
    assert 'stories' in response.body.keys()
    assert type(response.body['stories']) is list

    first_story = response.body['stories'][0]
    assert 'id'           in first_story.keys()
    assert 'name'         in first_story.keys()
    assert 'created_at'   in first_story.keys()
    assert 'published_at' in first_story.keys()
    assert 'uuid'         in first_story.keys()
    assert 'content'      in first_story.keys()
    assert 'slug'         in first_story.keys()
    assert 'full_slug'    in first_story.keys()
    assert 'tag_list'     in first_story.keys()

def test_stories_list_simple_querying(stories):
    response = stories.list(public_token, { "with_tag": "tag_from_my_second_folder"})

    assert response.code == 200
    assert 'stories' in response.body.keys()
    assert type(response.body['stories']) is list
    for story in response.body['stories']:
      assert story['tag_list'][0] == "tag_from_my_second_folder"

def test_stories_list_with_multi_params_querying(stories):
    response = stories.list(preview_token, { "is_startpage": "false", "with_tag": "tag_from_my_second_folder"})

    assert response.code == 200
    assert 'stories' in response.body.keys()
    assert type(response.body['stories']) is list
    for story in response.body['stories']:
      assert story['tag_list'][0] == "tag_from_my_second_folder"
      assert story['is_startpage'] == False

def test_stories_single_published(stories):
  response = stories.single(public_token, '18733502')
  response_body = response.body
  assert response.code == 200
  assert 'id'           in response_body['story'].keys()
  assert 'name'         in response_body['story'].keys()
  assert 'created_at'   in response_body['story'].keys()
  assert 'published_at' in response_body['story'].keys()
  assert 'uuid'         in response_body['story'].keys()
  assert 'content'      in response_body['story'].keys()
  assert 'slug'         in response_body['story'].keys()
  assert 'full_slug'    in response_body['story'].keys()
  assert 'tag_list'     in response_body['story'].keys()
  assert 'release_id'   in response_body['story'].keys()
  assert 'lang'         in response_body['story'].keys()

def test_stories_single_draft(stories):
  response = stories.single(preview_token, '18409847', {'version': 'draft'})
  response_body = response.body
  assert response.code == 200
  assert 'id'           in response_body['story'].keys()
  assert 'name'         in response_body['story'].keys()
  assert 'created_at'   in response_body['story'].keys()
  assert 'published_at' in response_body['story'].keys()
  assert 'uuid'         in response_body['story'].keys()
  assert 'content'      in response_body['story'].keys()
  assert 'slug'         in response_body['story'].keys()
  assert 'full_slug'    in response_body['story'].keys()
  assert 'tag_list'     in response_body['story'].keys()
  assert 'release_id'   in response_body['story'].keys()
  assert 'lang'         in response_body['story'].keys()
