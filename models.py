from distutils.command.upload import upload
from email.mime import image
from telnetlib import STATUS
from turtle import title
from django.db import models

class fanfic(models.Model):

    STATUS = (
        ('terminada', 'terminada'),
        ('em andamento', 'em andamento'),
    )

    title = models.CharField(max_length=255)
    sinopse = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
