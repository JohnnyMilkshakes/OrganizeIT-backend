from django.urls import path
from .views import Home, LocationList, LocationDetail, ItemListCreate, ItemDetail
from .views import Home

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('locations/', LocationList.as_view(), name='location-list'),
  path('locations/<int:id>/', LocationDetail.as_view(), name='location-detail'),
  path('locations/<int:location_id>/items/', ItemListCreate.as_view(), name='item-list-create'),
  path('locations/<int:location_id>/items/<int:id>/', ItemDetail.as_view(), name='item-detail'),
]