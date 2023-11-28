from django.db import models

class User(models.Model):
    name = models.CharField(max_length=1000)
    surname = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)

class Room(models.Model):
    name = models.CharField(max_length=1000)

class RoomParticipants(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Messages(models.Model):
    type = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)

