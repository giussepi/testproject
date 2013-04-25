# -*- coding: utf-8 -*-
""" baseapp's form """

from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    """  """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'span2', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'span2', 'placeholder': 'Password'}))

    def clean(self):
        """ verifies the use credentials """
        c_d = super(LoginForm, self).clean()
        user = authenticate(username=c_d['username'], password=c_d['password'])
        if user is not None and user.is_active:
            self.user = user
            pass
        else:
            raise forms.ValidationError('Invalid cretendials')
        return c_d

    def save(self):
        return self.user


class LogoutForm(forms.Form):
    """  """
    pass
