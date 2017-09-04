__author__ = 'weiyue'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username:',max_length=100)
    password = forms.CharField(label='password:',widget=forms.PasswordInput())

class CommentForm(forms.Form):
    #id = forms.AutoField(label='commentid')
    content = forms.CharField(label='content',max_length = 100)
    dessert_name = forms.CharField(label = "dessert_name",max_length = 100)
    dessert_shop_name = forms.CharField(label = "shop_name",max_length = 100)

class RegistForm(forms.Form):
    #account = forms.IntegerField(label='account')
    username = forms.CharField(label='username:',max_length=100)
    password = forms.CharField(label='password:',widget=forms.PasswordInput())

class ShopForm(forms.Form):
    #shopid = forms.IntegerField(label='shopid')
    name = forms.CharField(label='name',max_length = 100)
    phonenumber = forms.CharField(label='phonenumber',max_length =12)


