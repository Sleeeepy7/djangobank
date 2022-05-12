from django.urls import path
from . import views

urlpatterns = [
    path("", views.money_transfer, name="money_transfer"),
    # path("", views.show_history),
    path("register/", views.register, name="signup"),
    path("login/", views.sign_in, name="signin"),
    path("logout/", views.logout_view, name="logout"),
]