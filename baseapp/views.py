# -*- coding: utf-8 -*-
""" baseapp's views """

from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from baseapp.forms import LoginForm, LogoutForm
from baseapp.mixins import LoginRequiredMixin


class Home(FormView):
    """ shows the homepage """
    template_name = 'baseapp/home.html'
    form_class = LoginForm
    success_url = '/profile/'

    def form_valid(self, form):
        """  """
        c_d = form.cleaned_data
        user = form.save()
        login(self.request, user)
        return super(Home, self).form_valid(form)


class LogoutView(FormView):
    """  """
    form_class = LogoutForm

    def form_valid(self, form):
        """  """
        logout(self.request)
        return redirect('home')


class ProfileView(LoginRequiredMixin, TemplateView):
    """ shows the user profile """
    template_name = 'baseapp/profile.html'

    def get_context_data(self, **kwargs):
        """  """
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['form'] = LogoutForm()
        return context
