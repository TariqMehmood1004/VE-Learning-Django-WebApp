

from django.urls import path
from . import views

app_name = "veapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("showUsers/", views.showUsers, name="showUsers"),
    path('vpn-info/', views.vpn_info_without_ip, name='vpn_info_without_ip'),
    path('vpn-info/<str:user_ip>/', views.vpn_info_with_ip, name='vpn_info_with_ip'),
    path("registration/", views.registration, name="registration"),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
