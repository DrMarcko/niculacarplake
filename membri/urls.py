from django.urls import path

from home import views


urlpatterns = [
    path('', views.MembriTemplateView.as_view(), name='membri'),

]