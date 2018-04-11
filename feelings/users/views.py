from django.shortcuts import render
from django.contrib.auth import logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .forms import LogoutForm

def dashboard(request):
    return render(request, 'users/dashboard.html')


class LogoutView(LoginRequiredMixin, FormView):
    form_class = LogoutForm
    template_name = 'registration/logout.html'

    def form_valid(self, form):
        logout(self.request)
        return HttpResponseRedirect(reverse('home'))