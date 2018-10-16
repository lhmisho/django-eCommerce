import os
import random
from django.db import models

# Create your models here.

# taking finame from upload_image_path and dividing the filename and ext and return them back 
def get_file_name(filename):
    #basename = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext

# creating unique image name
def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,322345543)
    name, ext = get_file_name(filename)
    final_filename = f'{new_filename}{ext}'
    return f"Products/{new_filename}/{final_filename}"

class ProductQueryset(models.query.QuerySet):


    def active(self):
        return self.filter(active=True)
    
    def featured(self):
        return self.filter(featured=True, active=True)

# model manager for custom queryset
class ProductManager(models.Manager):
    
    def get_queryset(self):
        return ProductQueryset(self.model, using=self._db)

    # all is extend by active
    # if we do active false than all false item will not apear in all() method
    def all(self):
        return self.get_queryset().active()
    # custom query method for featured items
    def featured(self):
        query = self.get_queryset().featured()
        return query

    def get_by_id(self, pk):
        #return self.get_queryset().filter(id=pk) # i can use id as id or pk 
        qs = self.get_queryset().filter(id=pk)
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(default=10.00, decimal_places=2, max_digits=19)
    image       = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    featured    = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)
    objects     = ProductManager()
    
    def __str__(self):
        return self.title