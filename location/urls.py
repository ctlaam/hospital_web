from django.urls import path
from .views import Xaphuong,Quanhuyen,Tinhthanh
app_name= 'location'
urlpatterns = [
    path('xaphuong/',Xaphuong,name='xaphuong'),
    path('quanhuyen/',Quanhuyen, name='quanhuyen'),
    path('tinhthanh/',Tinhthanh, name='tinthanh'),
]