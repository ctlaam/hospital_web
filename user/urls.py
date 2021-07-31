from django.urls import path
from .views import BacsiSignUpView,Editprofile,DonviyteSignUpView,donviyte,Editprofiledvyt,bacsi

app_name= 'user'
urlpatterns = [
    path('bacsi/',BacsiSignUpView.as_view(),name='bacsisu'),
    path('edit/',Editprofile.as_view(), name='editprofile'),
    path('donviyte/',DonviyteSignUpView.as_view(),name='donviytesu'),
    path('donviyteview/', donviyte, name='donviyteview'),
    path('donviyteedit/', Editprofiledvyt.as_view(), name='donviyteedit'),
    path('danhsachbacsi/', bacsi, name='dsbacsi')
]
