from django.core.validators import MaxValueValidator
import datetime
from django.db import models
from django.urls import reverse

# Create your models here.
class CarsModel(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,)
    year  = models.IntegerField(default=2020, validators=[MaxValueValidator(datetime.datetime.now().year)])
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_created = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.brand)+str(self.model)
    
    def get_absolute_url(self):
        return reverse("car", kwargs={"car_slug": self.slug})
    
    

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})
