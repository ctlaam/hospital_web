import django_filters
from .models import Benhnhan
from django_filters import DateFilter,CharFilter
class BenhnhanFilter(django_filters.FilterSet):
    ten =CharFilter(field_name='ten',lookup_expr='icontains')
    class Meta:
        model = Benhnhan
        fields = 'ten','phone','email','donviyte'
        # exclude= ['tinhthanh','quanhuyen','xaphuong','gioitinh','mabaohiem'.'bhyt_ngaycap','bhyt_ngaysudung','baohiemyte']
