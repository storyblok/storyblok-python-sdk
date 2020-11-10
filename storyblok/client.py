from .http_client import HttpClient
from .api.sb_auth import sb_set_auth

# Assign all the api classes
from .api.spaces import Spaces
from .api.stories import Stories
from .api.tags import Tags
from .api.links import Links
from .api.datasource_entries import DatasourceEntries
from .api.datasources import Datasources

class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def spaces(self):
        """Returns your current space name, published version and domain
        """
        return Spaces(self)

    def stories(self):
        """Returns stories api instance
        """
        return Stories(self)

    def tags(self):
        """Returns tags api instance
        """
        return Tags(self)

    def links(self):
        """Returns links api instance
        """
        return Links(self)

    def datasources(self):
        """Returns Datasources api instance
        """
        return Datasources(self)

    def datasource_entries(self):
        """Returns DatasourceEntries api instance
        """
        return DatasourceEntries(self)

    def get(self, path, token='', auth_token='', params={}, options={}):
      """ Makes a custom GET request
      """
      sb_auth = sb_set_auth(token=token, auth_token=auth_token, params=params, options=options)

      res = self.http_client.get(path, sb_auth['params'], sb_auth['options'])
      return res

    def post(self, path, token='', auth_token='', params={}, options={}):
      """ Makes a custom POST request
      """

      sb_auth = sb_set_auth(token=token, auth_token=auth_token, params=params, options=options)

      res = self.http_client.post(path, sb_auth['params'], sb_auth['options'])
      return res

    def put(self, path, token='', auth_token='', params={}, options={}):
      """ Makes a custom PUT request
      """

      sb_auth = sb_set_auth(token=token, auth_token=auth_token, params=params, options=options)

      res = self.http_client.put(path, sb_auth['params'], sb_auth['options'])
      return res

    def delete(self, path, token='', auth_token='', params={}, options={}):
      """ Makes a custom DELETE request
      """

      sb_auth = sb_set_auth(token=token, auth_token=auth_token, params=params, options=options)

      res = self.http_client.delete(path, sb_auth['params'], sb_auth['options'])
      return res
