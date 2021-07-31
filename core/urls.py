from django.urls import path
from .views import Index,Logout,Dangki,Login
app_name= 'core'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dangki/',Dangki.as_view(),name='dangki'),
    path('login/',Logout.as_view(),name='login')
]