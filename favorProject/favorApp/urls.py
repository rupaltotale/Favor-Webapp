"""favorApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.show_services),
    # path('add-pending-user/', views.add_pending_user),
    path('landing/', views.landing, name="landing"),
    path('add-favor/', views.add_favor, name='add-favor'),
    path('user/', views.show_profile_page, name="show_profile_page"),
    path('edit/<int:pk>', views.edit_favor, name='edit_favor'),
    path('delete/<int:pk>', views.delete_favor, name='delete_favor'),
]