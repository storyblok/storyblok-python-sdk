class Datasources(object):

    """Returns Datasources api instance
    """

    def __init__(self, client):
        self.client = client

    def list(self, token, options={}):
        """Returns a list of Datasources (https://www.storyblok.com/docs/api/content-delivery#core-resources/datasources/datasources)

        '/cdn/datasources/' GET

        Args:
            token: Public token
        """
        response = self.client.get('/cdn/datasources/', token=token, options=options)

        return response

    def single(self, token, id, options={}):
        """Returns a single Datasource (https://www.storyblok.com/docs/api/content-delivery#core-resources/datasources/datasources)

        '/cdn/datasources/:id' GET

        Args:
            token: Public token
        """
        response = self.client.get('/cdn/datasources/' + id, token=token, options=options)

        return response
