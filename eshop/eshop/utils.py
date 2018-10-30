# link for slug generator:- https://www.codingforentrepreneurs.com/blog/a-unique-slug-generator-for-django/
# link for random string generator:- https://www.codingforentrepreneurs.com/blog/random-string-generator-in-python/
import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# creating unique order id for order apps
def unique_order_id_generator(instance):
    """
    This is for generating unique order_id for order processing on orders/models.py
    """
    new_order_id = random_string_generator().upper() # key : 1DSWA3FG somthing like that

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=new_order_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return new_order_id


def unique_slug_generator(instance, new_slug=None):
    """
    This is for django project with and it's assume that your
    instance has a model with a slug field and title character (char) field
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug