from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    date_of_login = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

    def __str__(self):
        return str(self.username)

