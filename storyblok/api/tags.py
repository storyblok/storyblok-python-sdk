class Tags(object):

    """Returns tags api instance
    """

    def __init__(self, client):
        self.client = client

    def list(self, token, options={}):
        """Returns a list of tags (https://www.storyblok.com/docs/Delivery-Api/Tags)

        '/cdn/tags/' GET

        Args:
            token: Public token for published or private token for draft version
        """
        response = self.client.get('/cdn/tags/', token=token, options=options)

        return response

