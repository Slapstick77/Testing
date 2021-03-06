import logging

logger = logging.getLogger(__name__)


class NotificationHandler(logging.Handler):
    def emit(self, record):
        from django.contrib.auth.models import User, Permission
        from django.db.models import Q
        from . import notify
        from .models import Notification

        try:
            perm = Permission.objects.get(codename="logging_notifications")
        except Permission.DoesNotExist:
            return

        message = record.getMessage()
        if record.exc_text:
            message += "\n\n"
            message = message + record.exc_text

        users = User.objects.filter(
            Q(groups__permissions=perm) | Q(user_permissions=perm) | Q(is_superuser=True)).distinct()
        for user in users:
            notify(
                user,
                f"{record.levelname} [{record.funcName}:{record.lineno}]",
                level=Notification.Level.from_old_name(record.levelname),
                message=message
            )
