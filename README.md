# storyblok-python-sdk

Storyblok API library client for python

__This library is generated by [alpaca](https://github.com/pksunkara/alpaca)__

## Installation

Make sure you have [pip](https://pypi.python.org/pypi/pip) installed

```bash
$ pip install storyblok
```

#### Versions

Works with [ 2.6 / 2.7 / 3.2 / 3.3 ]

## Usage

```python
import storyblok

# Then we instantiate a client (as shown below)
```

### Build a client

##### Without any authentication

```python
client = storyblok.Client()

# If you need to send options
client = storyblok.Client({}, client_options)
```

### Client Options

The following options are available while instantiating a client:

 * __base__: Base url for the api
 * __api_version__: Default version of the api (to be used in url)
 * __user_agent__: Default user-agent for all requests
 * __headers__: Default headers for all requests
 * __request_type__: Default format of the request body

### Response information

__All the callbacks provided to an api call will recieve the response as shown below__

```python
response = client.klass('args').method('args', method_options)

response.code
# >>> 200

response.headers
# >>> {'content-type': 'application/json; charset=utf-8'}
```

##### JSON response

When the response sent by server is __json__, it is decoded into a dict

```python
response.body
# >>> {"story": {"name":"story_name"}}
```

### Method Options

The following options are available while calling a method of an api:

 * __api_version__: Version of the api (to be used in url)
 * __headers__: Headers for the request
 * __query__: Query parameters for the url
 * __body__: Body of the request
 * __request_type__: Format of the request body

### Request body information

Set __request_type__ in options to modify the body accordingly

##### JSON request

When the value is set to __json__, JSON encode the body.

```python
body = {'story': {'name':"story_name"}}
# >>> '{"story": {"name":"story_name"}}'
```

### Spaces api

Returns your current space name, published version and domain

```python
spaces = client.spaces()
```

##### Get current space (GET /cdn/spaces/me)

This endpoint is mostly useful for client side apps. The response contains space.version which you can use to call the story api and get the most recent published version. (https://www.storyblok.com/docs/Delivery-Api/spaces)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

```python
response = spaces.me("your_access_token", options)
```

### Stories api

Returns stories api instance

```python
stories = client.stories()
```

##### Get a list of stories (GET /cdn/stories/)

Returns a list of Stories (https://www.storyblok.com/docs/Delivery-Api/get-a-story#get-a-list-of-stories)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

Getting a published stories list:

_simple example:_
```python
response = stories.list("your_access_token")
```
_advanced example:_
```python
response = stories.list("public_token", {"query": { "with_tag": "tag_from_my_second_folder"}})
```

Getting a draft stories list:

_simple example:_
```python
response = stories.list(preview_token, {"query": { "version": "draft"}})
```

##### Get a story by id (GET /cdn/stories/:story_id)

Returns a single story by id (https://www.storyblok.com/docs/Delivery-Api/get-a-story#get-a-story-by-id)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

Getting a published story:
```python
response = stories.single("your_access_token", "41252")
```

Getting a draft story:
```python
response = stories.single("your_access_token", "41252", { "query": {"version": "draft"}})
```

### Tags api

Returns tags api instance

```python
tags = client.tags()
```

##### Get a list of tags (GET /cdn/tags/)

Returns a list of tags (https://www.storyblok.com/docs/Delivery-Api/Tags)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

```python
response = tags.list("your_access_token", "de", options)
```

### Links api

Returns links api instance

```python
links = client.links()
```

##### Get a list of links (GET /cdn/links/)

Returns a list of links (https://www.storyblok.com/docs/Delivery-Api/Links)

The following arguments are required:

 * __token__: Public token for published or private token for draft version

```python
response = links.list("your_access_token", "draft", "de", options)
```

##### Get a link by id (GET /cdn/links/:id)

Returns a single link by id (https://www.storyblok.com/docs/Delivery-Api/Links#get-a-single-link)

The following arguments are required:

 * __token__: Public token for published or private token for draft version
 * __id__: Uuid of the link

```python
response = links.single("your_access_token", "148ee49a-ad81-4aff-b3d5-a2b4b6739e65", options)
```

### Datasources api

Returns datasources api instance

```python
datasources = client.datasources()
```

##### Get a list of Datasources (GET /cdn/datasources/)

Returns a list of Datasources (https://www.storyblok.com/docs/api/content-delivery#core-resources/datasources/datasources)

The following arguments are required:

 * __token__: Public token

```python
response = datasources.list("your_access_token")
```

##### Get a single Datasource (GET /cdn/datasources/:id)

Returns a single Datasources (https://www.storyblok.com/docs/api/content-delivery#core-resources/datasources/datasources)

The following arguments are required:

 * __token__: Public token

```python
response = datasources.single("your_access_token", 'id')
```

### DatasourceEntries api

Returns datasource_entries api instance

```python
datasource_entries = client.datasource_entries()
```

##### Get a list of DatasourceEntries (GET /cdn/datasource_entries/)

Returns a list of DatasourceEntries (https://www.storyblok.com/docs/api/content-delivery#core-resources/datasource-entries/datasource-entries)

The following arguments are required:

 * __token__: Public token

```python
response = datasource_entries.list("your_access_token")
```

## Testing
Install the testing tool
```bash
pip install -U pytest==6.1.2
```

Inside of the directory project set the `PYTHONPATH` to help the test suite find the module
```bash
export PYTHONPATH=.
```

Run the test suite:
```bash
pytest
```

## Contributors
Here is a list of [Contributors](https://github.com/storyblok/storyblok-python-sdk/contributors)

## License
MIT

## Bug Reports
Report [here](https://github.com/storyblok/storyblok-python-sdk/issues).
