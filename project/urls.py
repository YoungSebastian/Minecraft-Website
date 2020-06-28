from django.contrib import admin
from django.urls import path,include
from base.views import home,contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('sklep/', include('shop.urls')),
    path('kontakt/', contact, name="contact"),
]
