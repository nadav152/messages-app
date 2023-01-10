from api.constants import LOGGER
from api.models import Message, MessageToUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

# define the logger
logger_console = logging.getLogger(LOGGER)


@receiver(post_save, sender=Message)
def validate_client_creation_add_classifications(sender, instance, created, **kwargs):
    """
    This function responsible for making a connection between message and message to user.
    """
    try:
        if created:
            MessageToUser.objects.create(receiver=instance.receiver, message=instance)
            logger_console.debug(
                f"[CREATED MESSAGE TO USER] Message subject:{instance.subject} | Message receiver ID: {instance.receiver.id}",
                exc_info=True,
            )

    except Exception:
        logger_console.error(
            f"[FAILED CREATE MESSAGE TO USER] Message subject:{instance.subject}",
            exc_info=True,
        )
