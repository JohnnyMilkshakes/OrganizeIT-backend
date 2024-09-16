from django.urls import path
from .views import Home, LocationList, LocationDetail
from .views import Home

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('locations/', LocationList.as_view(), name='location-list'),
  path('locations/<int:id>/', LocationDetail.as_view(), name='location-detail'),
]