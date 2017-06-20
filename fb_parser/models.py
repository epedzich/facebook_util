from django.db import models

class FbThread(models.Model):
    users = models.CharField(max_length=200)

class FbMessage(models.Model):
    thread = models.ForeignKey(FbThread, related_name='messages')
    text = models.TextField(blank=True)
    user = models.CharField(max_length=200)
    meta = models.CharField(max_length=200)
