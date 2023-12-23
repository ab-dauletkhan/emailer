from django.db import models


class Mail(models.Model):
    # id will be added automatically
    recipient = models.EmailField()
    subject = models.CharField(
        max_length=255,
    )
    body_text = models.TextField()
    date_send = models.DateTimeField(auto_now_add=True)

    def preview_text(self):
        if len(self.body_text) > 60:
            return self.body_text[:60] + "..."
        return self.body_text

    def __str__(self):
        return self.subject
