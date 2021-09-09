from django.urls import path, include

from django.contrib.auth import views as auth_views

from users.views import index, signup, send_email

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('send_email/', send_email, name='send_email'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),

    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),

    path("password_reset_confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="users/passowrd_reset_confirm.html"), name="password_reset_done"),

    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),

    path('passwod-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete'),
]
