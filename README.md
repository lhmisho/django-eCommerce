# django-eCommerce
A light weight eCommerce site build with django


*) backup fixtures.
```python
python manage.py dumpdata products --format json --indent 4 > products/fixtures/products.json
```

*) load data form fixture

```python
python manage.py loaddata products/fixtures/products.py
```
