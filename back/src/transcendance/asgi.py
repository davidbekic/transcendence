"""
ASGI config for transcendance project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from rooms.consumers import consumers

from rooms.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "transcendance.settings")

logging.debug("rooms routing: ", rooms.routing)

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "https": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns,
            )
        ),
    }
)
