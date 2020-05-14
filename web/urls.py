"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from profiles import views as profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', profile_views.SiteLoginView.as_view(), name='login'),
    path('register/', profile_views.SiteRegisterView.as_view(), name='register'),
    path('register/ok/', profile_views.SiteRegisterOkView.as_view(), name='register_ok'),
    path('logout/', profile_views.SiteLogoutView.as_view(), name='logout'),
    path('profile/', profile_views.EditProfilesView.as_view(), name='profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)