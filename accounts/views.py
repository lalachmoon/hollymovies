from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import AdminRequestMessageForm
from accounts.models import AdminRequestMessage


@login_required
def permissions_request_form(request):
    if request.method == 'POST':
        form = AdminRequestMessageForm(request.POST)
        if form.is_valid():
            admin_request = form.save(commit=False)
            admin_request.user = request.user
            admin_request.save()
            return redirect('/')
    else:
        form = AdminRequestMessageForm()

    return render(request, 'permissions_request_form.html', {'form': form})


class SubmittableLoginView(LoginView):
    template_name = 'login.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = '/'


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['first_name'] = self.request.user.first_name
        context['last_name'] = self.request.user.last_name
        user = self.request.user
        context['user'] = user
        context['user_messages'] = AdminRequestMessage.objects.filter(user=user)  # Mesajele utilizatorului curent
        context['biography'] = getattr(self.request.user.profile, 'biography', None)  # Safe lookup
        return context
