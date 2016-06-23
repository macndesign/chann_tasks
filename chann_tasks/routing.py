from channels.routing import route
from core.consumers import hello, hello2, foo

channel_routing = [
    route('bg-hello', hello),
    route('bg-hello2', hello2),
    route('bg-foo', foo),
]
