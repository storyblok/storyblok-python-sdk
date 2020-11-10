class Spaces(object):

    """Returns your current space name, published version and domain
    """

    def __init__(self, client):
        self.client = client

    def me(self, token, options={}):
        """This endpoint is mostly useful for client side apps. The response contains space.version which you can use to call the story api and get the most recent published version. (https://www.storyblok.com/docs/Delivery-Api/spaces)

        '/cdn/spaces/me' GET

        Args:
            token: Public token for published or private token for draft version
        """
        response = self.client.get('/cdn/spaces/me', token=token, options=options)

        return response

