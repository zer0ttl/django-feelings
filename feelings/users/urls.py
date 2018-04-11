from django.urls import include, path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'users'
urlpatterns = [
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]