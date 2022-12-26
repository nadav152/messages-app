from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import MessageSerializer, MessageToUserSerializer
from api.constants import MESSAGE_FILTER_FIELDS, MESSAGE_TO_USER_FILTER_FIELDS
from api.filters import MessageFilter, MessageToUserFilter
from rest_framework import viewsets
from api.models import Message, MessageToUser

# Create your views here.


class MessageViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = MESSAGE_FILTER_FIELDS
    filterset_class = MessageFilter
    # permission_classes = [DjangoModelPermissions]
    permission_classes = []

    def get_queryset(self):
        return Message.objects.all().order_by('id')

    # def delete(self, request, format=None, *args, **kwargs):

    #     attribute_arr = []
    #     for key in MESSAGE_FILTER_FIELDS:
    #         attribute = request.GET.get(key, None)
    #         attribute_arr.append(attribute)

    #     response = delete_by_filter(Person, PERSON_FILTER_FIELDS,
    #                                 attribute_arr)
    #     return Response(response)
    
    
class MessageToUserViewSet(viewsets.ModelViewSet):

    serializer_class = MessageToUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = MESSAGE_TO_USER_FILTER_FIELDS
    filterset_class = MessageToUserFilter
    # permission_classes = [DjangoModelPermissions]
    permission_classes = []

    def get_queryset(self):
        return MessageToUser.objects.all().order_by('id')

    # def delete(self, request, format=None, *args, **kwargs):

    #     attribute_arr = []
    #     for key in MESSAGE_FILTER_FIELDS:
    #         attribute = request.GET.get(key, None)
    #         attribute_arr.append(attribute)

    #     response = delete_by_filter(Person, PERSON_FILTER_FIELDS,
    #                                 attribute_arr)
    #     return Response(response)