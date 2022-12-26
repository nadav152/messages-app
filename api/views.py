from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import MessageSerializer, MessageToUserSerializer
from api.constants import MESSAGE_FILTER_FIELDS, MESSAGE_TO_USER_FILTER_FIELDS
from api.filters import MessageFilter, MessageToUserFilter
from rest_framework import viewsets
from api.models import Message, MessageToUser
from rest_framework.permissions import IsAuthenticated


class MessageViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = MESSAGE_FILTER_FIELDS
    filterset_class = MessageFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user).order_by('id')

class MessageToUserViewSet(viewsets.ModelViewSet):

    serializer_class = MessageToUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = MESSAGE_TO_USER_FILTER_FIELDS
    filterset_class = MessageToUserFilter
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return MessageToUser.objects.all().order_by('id')

