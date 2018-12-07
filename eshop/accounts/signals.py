from django.dispatch import Signal

"here instance means product id or title etc and request is for do someting for get ip of this request"

user_logged_in = Signal(providing_args=['instance', 'request'])