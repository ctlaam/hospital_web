from django.urls import path
from . import views
app_name= 'patient'
urlpatterns = [
    path('',views.Patient,name='benhnhan'),
    path('addbenhnhan/',views.Thembenhnhan,name='addbenhnhan'),
    path('updatebenhnhan/<str:pk>/',views.Updatebenhnhan,name='updatebenhnhan'),
    path('deletebenhnhan/<str:pk>/', views.Deletecbenhnhan, name='deletebenhnhan')
]