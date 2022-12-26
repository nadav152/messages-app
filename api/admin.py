from django.contrib import admin
from api.models import Message, MessageToUser

admin.site.register(Message)
admin.site.register(MessageToUser)
