def sb_set_auth(token='', auth_token='', params={}, options={}):
      if(token):
        params['token'] = token
      else:
        options['headers'] = {'Authorization': auth_token }

      return { 'params': params, 'options': options }
