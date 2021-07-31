import django_filters
from .models import Bacsi,Donviyte,User
from django_filters import DateFilter
class BacsiFilter(django_filters.FilterSet):
    class Meta:
        model = Bacsi
        fields = 'ten','gioitinh','donviyte'
        # exclude= ['tinhthanh','quanhuyen','xaphuong','gioitinh','mabaohiem'.'bhyt_ngaycap','bhyt_ngaysudung','baohiemyte']

class DonviyteFilter(django_filters.FilterSet):
    class Meta :
        model=Donviyte
        fields='ten','diachi',


class UserFilter(django_filters.FilterSet):
    class Meta :
        model=User
        fields='phone','email'
