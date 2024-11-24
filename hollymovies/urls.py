"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from viewer import urls as viewer_urls
from viewer.views import index
from accounts import urls as accounts_urls

from django.conf import settings
from django.conf.urls.static import static

# Functia include() include path-uri din alte apps
# care au un fisier urls.py in interiorul lor
urlpatterns = [
    # Url-ul pentru pagina de login
    # path('accounts/login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('', index),
    path('movies/', include(viewer_urls)),
    path('accounts/', include(accounts_urls , namespace='accounts'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ^ adauga urls extra pentru fiecare fisier din folderul static/