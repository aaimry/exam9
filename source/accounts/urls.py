from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import RegisterView, UserProfileView, UserPasswordChangeView, UpdateUserView


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path("update/", UpdateUserView.as_view(), name="update_user"),
    path("change_password/", UserPasswordChangeView.as_view(), name="change_password"),

]

