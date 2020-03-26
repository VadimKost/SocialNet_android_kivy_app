# encoding=utf8
from kivy.storage.jsonstore import JsonStore
import base64

from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp

store = JsonStore('hello.json')

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





class Login(Screen):
    def sucsses(self,req, resp):
        name = req.req_headers['name']
        password = req.req_headers['password']
        store.put('user', name=name, password=password)
        self.manager.current='2'
    def on_kv_post(self, base_widget):
        if store.exists('user'):
            self.manager.current='2'
    req_name = StringProperty()
    req_password=StringProperty()
    def log(self):
        auth = self.req_name + ":" + self.req_password
        auth = base64.b64encode(auth.encode())
        auth = str(auth, 'utf-8')
        head = {"Authorization": 'Basic ' + auth}
        head['name']=self.req_name
        head['password']=self.req_password
        data = UrlRequest('http://www.vako.ga/api/user/', self.sucsses, req_headers=head)

        print(data.req_headers)


class Account(Screen):
    pass


class Manager(ScreenManager):
    pass


class MyApp(MDApp):
    def build(self):
        return Manager()


MyApp().run()
