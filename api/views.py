from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import MessageSerializer, MessageToUserSerializer
from api.constants import MESSAGE_FILTER_FIELDS, MESSAGE_TO_USER_FILTER_FIELDS
from api.filters import MessageFilter, MessageToUserFilter
from rest_framework import viewsets
from api.models import Message, MessageToUser
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication


class MessageViewSet(viewsets.ModelViewSet):
    """
    Messages endpoint.

    Operations:
    • GET - Get one of more messages. The messages will be filtered by the message receiver.
    • POST - Adding new message to the system.
    • FILTER - Getting a message by its ID.
    • DELETE - Deleting a message by its ID.
    • PUT - Edit an object record by supplying all its fields.
    • PATCH - Edit an object record by supplying only the updated fields.
    """
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = MESSAGE_FILTER_FIELDS
    filterset_class = MessageFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user).order_by('id')

class MessageToUserViewSet(viewsets.ModelViewSet):
    """
    Messages to Users endpoint.

    Operations:
    • GET - Get one of more object. 
    • POST - Adding new object to the system.
    • FILTER - Getting a object by its ID.
    • DELETE - Deleting a object by its ID.
    • PUT - Edit an object record by supplying all its fields.
    • PATCH - Edit an object record by supplying only the updated fields.
    """
    serializer_class = MessageToUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = MESSAGE_TO_USER_FILTER_FIELDS
    filterset_class = MessageToUserFilter
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return MessageToUser.objects.all().order_by('id')

