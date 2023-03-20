from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView

from .models import News


# Create your views here.

class MainView(TemplateView):
    template_name = 'news_main.html'

    def get(self, request):
        if request.user.is_authenticated:
            news = News.objects.filter(author=request.user)
            ctx = {'news': news}
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/news/'
    template_name = 'login.html'

    def form_vali(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginView, self).form_valid()

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid()


class Logout(View):
    def get(self, request):
        logout(request)
