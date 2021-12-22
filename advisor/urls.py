"""booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from bookadvisor import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='home'),
    path('advisor/',views.createadvisor,name='createadvisor'),
    path('user/register/',views.register,name='register'),
    path('user/login/',views.login_view,name='login_view'),
    path('user/logout/',views.logout_view,name='logout'),
    path('user/userid/advisor/',views.bookadvisor,name='bookadvisor'),
    path('user/userid/advisor/<int:id>/',views.booking,name='booking'),
    path('user/userid/advisor/booking/',views.showbooked,name='showbooked'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
