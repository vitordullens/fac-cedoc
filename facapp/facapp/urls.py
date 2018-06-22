"""facapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

import cedoc.views as cedocViews
import accounts.views as accountsViews
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', authViews.login, name='login'),
    path('logout', authViews.logout, name='logout'),
    path('password_reset', authViews.password_reset, name='password_reset'),
    path('signup/', accountsViews.SignUp, name='url_signup'),

    path('', cedocViews.index, name='url_index'),
    path('option', cedocViews.option, name='url_option'),
    path('<str:btn>/new_entry/', cedocViews.new_entry, name='url_new_entry'),
    path('delete/<int:pk>', cedocViews.delete, name='url_delete'),
    path('contributors/<int:pk>', cedocViews.contribs, name='url_contribs'),
    path('index/<int:pk>', cedocViews.idx, name='url_idx'),
    path('certificates/<int:pk>', cedocViews.certificates, name='url_certificates'),


    path('edit/<int:pk>', cedocViews.edit, name='url_edit')
]
