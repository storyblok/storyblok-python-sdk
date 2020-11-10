class Links(object):

    """Returns links api instance
    """

    def __init__(self, client):
        self.client = client

    def list(self, token, options={}):
        """Returns a list of links (https://www.storyblok.com/docs/Delivery-Api/Links)

        '/cdn/links/' GET

        Args:
            token: Public token for published or private token for draft version
        """

        response = self.client.get('/cdn/links/', token=token, options=options)

        return response

    def single(self, token, id, options={}):
        """Returns a single link by id (https://www.storyblok.com/docs/Delivery-Api/Links#get-a-single-link)

        '/cdn/links/:id' GET

        Args:
            token: Public token for published or private token for draft version
            id: Uuid of the link
        """

        response = self.client.get('/cdn/links/' + id, token=token, options=options)

        return response

