#! /usr/bin/env python2.7
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)