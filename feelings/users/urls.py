from django.urls import include, path
from . import views

app_name = 'users'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]