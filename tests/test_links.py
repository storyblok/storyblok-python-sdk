import pytest
import storyblok

public_token  = "KOesmZuJLW2Yy7QJcMuFPQtt"

@pytest.fixture
def links():
    client = storyblok.Client()
    return client.links()

def test_link_list(links):
    response = links.list(public_token)
    assert response.code == 200
    assert 'links' in response.body.keys()

    first_link = response.body['links']['7fa6ea24-896e-4ee9-8412-f9df7e37c7df']
    assert 'id'           in first_link.keys()
    assert 'name'         in first_link.keys()
    assert 'slug'         in first_link.keys()
    assert 'slug'         in first_link.keys()
    assert 'is_folder'    in first_link.keys()
    assert 'parent_id'    in first_link.keys()
    assert 'published'    in first_link.keys()
    assert 'position'     in first_link.keys()
    assert 'uuid'         in first_link.keys()
    assert 'is_startpage' in first_link.keys()
    assert 'real_path'    in first_link.keys()

def test_link_single(links):
    response = links.single(public_token, 'b28c8822-5854-4013-8e38-0dda6e058916')
    assert response.code == 200
    assert 'link' in response.body.keys()

    link = response.body['link']
    assert 'id'           in link.keys()
    assert 'name'         in link.keys()
    assert 'slug'         in link.keys()
    assert 'is_folder'    in link.keys()
    assert 'parent_id'    in link.keys()
    assert 'published'    in link.keys()
    assert 'position'     in link.keys()
    assert 'uuid'         in link.keys()
    assert 'is_startpage' in link.keys()
