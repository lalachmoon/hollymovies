from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import SubmittableLoginView, SubmittablePasswordChangeView, SignUpView, ProfileView
from accounts.views import permissions_request_form


app_name = 'accounts'

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('permissions-request-form/', permissions_request_form, name='permissions_request_form'),
]
