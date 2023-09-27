from django.urls import path
from .views import user_login_view, user_logout_view, user_registration_view, UserListView


urlpatterns = [
  
    path('login/', user_login_view, name='user-login'),
    path('logout/', user_logout_view, name='user-logout'),
    path('register/', user_registration_view, name='user-registration'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserListView.as_view(), name='users')
]
