from .models import MessageToUser, Message
import django_filters


class MessageToUserFilter(django_filters.FilterSet):
    class Meta:
        model = MessageToUser

        fields = {
            'message': ['exact'],
            'creation_time': ['gt', 'lt'],
            'was_seen': ['exact'],
        }


class MessageFilter(django_filters.FilterSet):
    class Meta:
        model = Message

        fields = {
            'message': ['icontains'],
            'subject': ['icontains'],
            'creation_time': ['gt', 'lt'],
        }
