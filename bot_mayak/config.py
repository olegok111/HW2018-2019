AUTH = False
TOKEN = '662581590:AAEF-Ii3kQSlgN6ke81xD_t6t_-9_SwwhY8'
PROXY = 'https://208.88.233.1:54149'
USERNAME = ''
PASSWORD = ''
if not AUTH:
    REQUEST_KWARGS = {'proxy_url': PROXY}
else:
    REQUEST_KWARGS = {'proxy_url': PROXY,
                      'urllib3_proxy_kwargs': {'username': USERNAME,
                                                'password': PASSWORD
                                               }
                      }
