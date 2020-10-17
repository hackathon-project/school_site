from django.shortcuts import render
from django.http import Http404, HttpResponseForbidden, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.db import models
from django.contrib.auth.models import User

def test(request):
    return render(request, 'test_page.html')


def registration(request):
    return render(request, 'registration.html', {'form': UserCreationForm})


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = 'articles/'
    template_name = 'registration.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
    
    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

def validate_registration_form(request):
    form = UserCreationForm(request.GET)
    #return HttpResponse(form.is_valid())
    if form.is_valid:
        pass
    else:
        return super(RegisterFormView, self).form_invalid(form)

def add_user(request):
    f = UserCreationForm(request.POST)
    if f.is_valid():
        f.save()
    return HttpResponseRedirect(reverse('main:test'))