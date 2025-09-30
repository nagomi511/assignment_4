from django.contrib import admin
from django.urls import path
from calculator.views import calculator_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calculator_view, name='home'),
]
