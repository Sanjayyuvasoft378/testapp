from django.urls import path
from . import views
urlpatterns = [
    # path('signup/',views.signup,name='signup'),
    path('register/',views.RegistrationAPI.as_view(),name='register'),
    path('login/',views.LoginAPI.as_view(),name='login'),
    path('logout/',views.LogoutAPI.as_view(),name='logout'),
    path('changepassword/',views.ChangePasswordAPI.as_view(),name='changepassword'),

    
]
