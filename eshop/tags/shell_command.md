>> python manage.py shell

#### for Tag Apps
>>> from tags.models import Tag
>>> Tag.objects.all()
<QuerySet [<Tag: my car>, <Tag: black cycle>]>>>> Tag.objects.last()
<Tag: black cycle>
>>> black = Tag.objects.all()
>>> black.titleTraceback (most recent call last):
  File "<console>", line 1, in <module>AttributeError: 'QuerySet' object has no attribute 'title'
>>> opt = Tag.objects.all()>>> opt.title
Traceback (most recent call last):
  File "<console>", line 1, in <module>AttributeError: 'QuerySet' object has no attribute 'title'
>>> opt = Tag.objects.first()>>> opt
<Tag: my car>
>>> opt = Tag.objects.last()
>>> opt
<Tag: black cycle>
>>> black = Tag.objects.last()
>>> black
<Tag: black cycle>
>>> bleack.title
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'bleack' is not defined
>>> black = Tag.objects.all()
>>> black
<QuerySet [<Tag: my car>, <Tag: black cycle>]>
>>> Tag.objects.last()
<Tag: black cycle>
>>> black = Tag.objects.last()
>>> black
<Tag: black cycle>
>>> black.slug
'black-cycle'
>>> black.title
'black cycle'
>>> black.products
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7f49499a9518>
>>> black.products.all()
<ProductQueryset [<Product: car>, <Product: cycle>, <Product: cycle>]>
>>> product = black.products.all()
>>> products
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'products' is not defined
>>> product
<ProductQueryset [<Product: car>, <Product: cycle>, <Product: cycle>]>
>>> products.title
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'products' is not defined
>>> products
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'products' is not defined
>>> product.title
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ProductQueryset' object has no attribute 'title'
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit(
... )


######Experiment for Product apps
(eCommerce)lhmisho@lhmisho:~/myPythonProjects/eCommerce/eshop$python manage.py shell
Python 3.6.6 (default, Sep 12 2018, 18:26:19)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] onlinux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> Product.objects.all()
<ProductQueryset [<Product: car>, <Product: truck>, <Product: but>, <Product: rikshaw>, <Product: cycle>, <Product: cycle>, <Product: shirt>]>
>>> shirt = Product.objects.first()
>>> shirt.title
'car'
>>> shirt.slug
'car-qj22'
>>> shirt.tags
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Product' object has no attribute 'tags'
>>> shirt.tag_set.all()
<Quer