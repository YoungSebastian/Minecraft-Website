from django.urls import path
from .views import home,payment

app_name = "shop"

urlpatterns = [
    path('', home, name="home"),
    path('platnosc/<product>', payment, name="payment"),
]
