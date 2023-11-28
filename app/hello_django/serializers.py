from rest_framework import serializers

from .models import User, Room, RoomParticipants, Messages


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'email')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('id', 'type', 'message', 'sender', 'receiver')

class RoomParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room', 'user')
