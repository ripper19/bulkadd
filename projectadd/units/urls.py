from django.urls import path
from .views import BulkInsert

urlpatterns = [
    path('bulk-insert/', BulkInsert.as_view(), name ='bulk-add-products')
]