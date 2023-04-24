from django.db import models

class User():
    name = models.CharField()
    email = models.CharField()
