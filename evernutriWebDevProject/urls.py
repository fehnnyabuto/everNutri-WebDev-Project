"""
URL configuration for evernutriWebDevProject project.

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
from . import views as my_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', my_views.home, name='home-url'),
    path('blog/', my_views.blog, name='blog-url'),
    path('about/', my_views.about, name='about-url'),
    path('contact/', my_views.contact, name='contact-url'),
    path('auth/', include('auth.urls')),
    path('products/', include('products.urls')),
])
               # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
