URL_ROOT='http://www.vako.ga'

import base64

# def get_user(req, resp):
#     for i in resp:
#         for y in i['members']:
#             try:
#                 z=y.split('/')
#                 if z[5]=='5':
#                     print(i)
#             except:
#                 continue
#     return resp[0] .encode('cp1251').decode('utf-8')
def head_auth(name,password):
    auth = name + ":" + password
    auth = base64.b64encode(auth.encode())
    auth = str(auth, 'utf-8')
    head = {"Authorization": 'Basic ' + auth}
    return head