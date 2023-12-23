from django.urls import path
from . import views


app_name = "email_sender"

urlpatterns = [
    path("", views.mail_list, name="mail-list"),
    path("sent_mail/", views.sent_mail, name="sent-mail"),
]
