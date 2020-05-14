from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView, FormView
from profiles.forms import RegisterForm


class SiteLoginView(LoginView):
    template_name = 'login.html'


class SiteRegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'],
            password=data['password1'],
            email=data['email'],
        )
        url = f"{reverse('register_ok')}?username={new_user.username}"
        return redirect(url)


class SiteRegisterOkView(TemplateView):
    template_name = 'register_ok.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context


class EditProfilesView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class SiteLogoutView(LogoutView):
    template_name = 'logout.html'