from django.db import models

class User(models.Model):
    telegram_id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    coins = models.IntegerField(default=0)

    def __str__(self):
        return self.username
