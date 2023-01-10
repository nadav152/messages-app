from typing import List
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Q
from api.models import Message, MessageToUser, User
from api.serializers import MessageSerializer, MessageToUserSerializer
from api.constants import MESSAGE_FILTER_FIELDS, MESSAGE_TO_USER_FILTER_FIELDS
from api.filters import MessageFilter, MessageToUserFilter


class MessageViewSet(viewsets.ModelViewSet):
    """
    Messages endpoint.

    Operations:
    • GET - Get one of more messages. Filtered by the receiver.
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
        return (
            Message.objects.filter(
                Q(receiver=self.request.user) | Q(sender=self.request.user)
            )
            .select_related('sender', 'receiver')
            .order_by('id')
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = self.request.user
        self.validate_message_delete(instance, user)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def validate_message_delete(self, instance: Message, user: User) -> None:

        """
        This function validates if the message should be deleted.
        By checking if the sender and receiver are none, the validation happens
        """

        if instance.sender == user:
            instance.sender = None
        elif instance.receiver == user:
            instance.receiver = None

        if instance.receiver is None and instance.sender is None:
            self.perform_destroy(instance)
        else:
            instance.save()


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
        return MessageToUser.objects.filter(receiver=self.request.user).order_by('id')

    def update_page_seen(self, page: List[MessageToUser]) -> None:

        for obj in page:
            obj.was_seen = True

        MessageToUser.objects.bulk_update(page, ['was_seen'])

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            self.update_page_seen(page)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
