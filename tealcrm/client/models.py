from django.contrib.auth.models import User
from django.db import models
from common.mixins import IDasUUIDMixin

class Client(IDasUUIDMixin):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    telegram_id = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    @property
    def name(self):
        return f'{self.firstname} {self.last_name}' 

    def __str__(self):
        return self.name
    