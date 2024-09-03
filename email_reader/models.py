from django.db import models


class EmailAccount(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    provider = models.CharField(max_length=50)  # e.g., 'yandex', 'gmail', 'mail'

    def __str__(self):
        return self.email


class EmailMessage(models.Model):
    email_account = models.ForeignKey(
        EmailAccount, on_delete=models.CASCADE, related_name="messages"
    )
    subject = models.CharField(max_length=255)
    sent_at = models.DateTimeField()
    received_at = models.DateTimeField()
    body = models.TextField()
    attachments = models.JSONField(
        default=list
    )  # Store attachment info as a list of file URLs or paths

    def __str__(self):
        return self.subject
