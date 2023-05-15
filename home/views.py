from django.shortcuts import render

from django.views.generic import TemplateView



class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'


class MembriTemplateView:
    @classmethod
    def as_view(cls):
        pass
