from django.contrib import admin
from django.urls import path, include
from accounts import views
import turtle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('allauth.account.urls')),
    path('account/', include('accounts.urls')),
   
    
]
