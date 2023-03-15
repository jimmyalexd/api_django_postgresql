from django.urls import path
from .views import PointView
from .views import map_view

urlpatterns = [
    path('points/',PointView.as_view(),name='points_list'),
    path('points/<int:id>',PointView.as_view(),name='points_process'),
    path('map/', map_view, name='map_view'),
]
