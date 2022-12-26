from api.models import Message, MessageToUser
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        
        
class MessageToUserSerializer(serializers.ModelSerializer):
       class Meta:
        model = MessageToUser
        fields = '__all__'