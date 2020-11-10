import pytest
import storyblok

def test_spaces_me():
    client = storyblok.Client()
    spaces = client.spaces()
    response = spaces.me("KOesmZuJLW2Yy7QJcMuFPQtt")
    assert response.code == 200
    assert 'space'          in response.body.keys()
    assert 'id'             in response.body['space'].keys()
    assert 'name'           in response.body['space'].keys()
    assert 'domain'         in response.body['space'].keys()
    assert 'domain'         in response.body['space'].keys()
    assert 'version'        in response.body['space'].keys()
    assert 'language_codes' in response.body['space'].keys()
