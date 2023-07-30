import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter  # noqa: E402

from reactpy_django import REACTPY_WEBSOCKET_PATH  # noqa: E402

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()

from channels.auth import AuthMiddlewareStack  # noqa: E402
from channels.sessions import SessionMiddlewareStack  # noqa: E402


application = ProtocolTypeRouter(
    {
        "http": application,
        "websocket": SessionMiddlewareStack(
            AuthMiddlewareStack(
                URLRouter(
                    [REACTPY_WEBSOCKET_PATH],
                )
            )
        ),
    }
)