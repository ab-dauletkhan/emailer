from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .models import Mail
from .forms import MailModelForm


def mail_list(request):
    mails = Mail.objects.all()
    context = {"mails": mails}

    return render(request, "email_sender/mail_list.html", context)


def sent_mail(request):
    form = MailModelForm()
    if request.method == "POST":
        form = MailModelForm(request.POST)
        if form.is_valid():
            mail_instance = form.save()
            send_mail(
                subject=mail_instance.subject,
                message=mail_instance.body_text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[mail_instance.recipient],
                fail_silently=False,
            )
            return redirect(reverse("email_sender:mail-list"))
    context = {"form": form}
    return render(request, "email_sender/sending_page.html", context)
