from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm


class SignupView(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'auth_/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'auth_/signup.html', {'form': form})