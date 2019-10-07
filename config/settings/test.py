from .base import *  # NOQA

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "errors_db.tests.layer_utils.MockedRedisInMemoryChannelLayer"
    }
}
