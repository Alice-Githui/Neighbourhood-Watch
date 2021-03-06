from . import views
from django.conf import settings
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[
    path('register/', views.Registration.as_view(), name="registeruser"),
    path('getuser/', views.Registration.as_view(), name="getusers"),
    path('loginuser/', views.LoginUser.as_view(), name="loginuser"),
    path('authlogin/', ObtainAuthToken.as_view(), name="authlogin"),
    path('api/neighbours/', views.NeighborhoodList.as_view(), name="neighbour"),
    path('api/business/', views.BusinessList.as_view(), name="business"),
    path('api/users/', views.UserList.as_view(), name="users"),
    path('api/neighbours/<int:pk>/', views.NeighbourhoodDetails.as_view(), name="one-neighbourhood"),
    path('api/business/<int:pk>/', views.BusinessDetails.as_view(), name="one-business"),
    path('api/users/<int:pk>/', views.UserDetails.as_view(), name="one-user"),
    path('api/update/neighbours/<int:pk>/', views.NeighbourhoodDetails.as_view(), name="update-neighbourhood"),
    path('api/update/business/<int:pk>/', views.BusinessDetails.as_view(), name="update-business"),
    path('api/update/users/<int:pk>/', views.UserDetails.as_view(), name="update-user"),
    path('api/delete/neighbours/<int:pk>/', views.NeighbourhoodDetails.as_view(), name="delete-neighbourhood"),
    path('api/delete/business/<int:pk>/', views.BusinessDetails.as_view(), name="delete-business"),
    path('api/delete/user/<int:pk>/', views.UserDetails.as_view(), name="delete-user"),
    path('api/posts/', views.PostsList.as_view(), name="allposts"),
]