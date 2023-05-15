import random

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from niculacarplake.settings import EMAIL_HOST_USER
from userextend.forms import UserForm


# Create your views here.
class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    # success_url = reverse_lazy('homepage') #DACA FOLOSESC def form_valid(self, form) NU am nevoie de success_url

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            new_user.username = f'{new_user.first_name.lower()}{new_user.last_name.lower()}_{random.randrange(100000, 999999, 6)}'
            new_user.save()


            details ={
                'fullname': f'{new_user.first_name} {new_user.last_name}',
                'username': new_user.username
            }
            subject = 'Felicitari! Ai un cont nou in aplicatie'
            message = get_template('mail.html').render(details)
            mail = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [new_user.email]
            )
            mail.content_subtype = 'html'
            mail.send()



        return redirect('login')

urls.py
from django.urls import path

from userextend import views

urlpatterns = [
    path('create-user/', views.UserCreateView.as_view(), name='create_user'),
from django.shortcuts import render

# Create your views here.
