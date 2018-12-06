from django.dispatch import Signal

"here instance meace product id or title etc and request is for do someting for get ip of this request"

object_viewd_singnal = Signal(providing_args=['instance', 'request'])