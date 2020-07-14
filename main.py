# encoding=utf8

from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty, ObjectProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp

from mything import URL_ROOT, head_auth

store = JsonStore('hello.json')

class Login(Screen):
    req_name = StringProperty()
    req_password=StringProperty()
    def sucsses(self,req, resp):
        name = self.req_name
        password = self.req_password
        store.put('user', name=name, password=password)
        self.manager.current='2'
    def on_kv_post(self, base_widget):
        if store.exists('user'):
            self.manager.current='2'
    def log(self):
        data = UrlRequest(URL_ROOT+'/api/user/', self.sucsses, req_headers=head_auth(self.req_name,self.req_password))


class Content():
    pass


class Account(Screen):
    image=ObjectProperty()
    username=ObjectProperty()
    address=ObjectProperty
    phone=ObjectProperty()
    about_me=ObjectProperty()
    def success(self,req,resp):
        print(resp)
        self.data=resp
        self.image.source=URL_ROOT+resp['img']
        self.username.text=self.data['user']['username']
        self.address.text = self.data['adress']
        self.phone.text = self.data['phone']
        self.about_me.text=self.data['AboutMe']

    def on_pre_enter(self, *args):
        user=store.get('user')
        req = UrlRequest(URL_ROOT+'/api/currentuser/', self.success, req_headers=head_auth(user['name'],user['password']))
class Manager(ScreenManager):
    pass



class MyApp(MDApp):
    def build(self):
        return Manager()


MyApp().run()
