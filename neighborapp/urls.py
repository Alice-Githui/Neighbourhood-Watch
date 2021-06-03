from . import views
from django.conf import settings
from django.urls import path, re_path

urlpatterns=[
    path('api/neighbours/', views.NeighborhoodList.as_view(), name="neighbour"),
    path('api/business/', views.BusinessList.as_view(), name="business"),
    path('api/users/', views.UserList.as_view(), name="users"),
    path('api/neighbours/<int:pk>/', views.NeighbourhoodDetails.as_view(), name="one-neighbourhood"),
]