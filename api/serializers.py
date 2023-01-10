from rest_framework import serializers
from api.models import Message, MessageToUser


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'message', 'subject', 'creation_time']


class MessageToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageToUser
        fields = ['id', 'receiver', 'message', 'creation_time', 'was_seen']
