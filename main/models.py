from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
class Listing(models.Model):
  farmer = models.ForeignKey(User, on_delete=models.CASCADE)
#   labourous = models.ManyToManyField(User,blank=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  name = models.CharField(max_length=200)
  message = models.TextField(blank=True)
  planted_date= models.DateField()
  due_date = models.DateField(blank=True)
  estimated_cost = models.CharField(max_length=200)
  is_published = models.BooleanField(default=True)
  slug = models.SlugField(max_length=48)
  
  def __str__(self):
    return self.name


class ProductTagManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)

class ListingRecord(models.Model):
    title =  models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="record")
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date = models.DateField()
    activities = models.TextField(blank=True)
    method = models.TextField(blank=True)
    cost = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    slug = models.SlugField(max_length=48)

    objects = ProductTagManager()
    def __str__(self):
        return self.category

    def natural_key(self):
        return (self.slug,)    


class Labourer(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="labouror")
    projects = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="project")
    name = models.CharField(max_length=200)
 
    sex = models.CharField(max_length=50, choices=sex_choice, default='Male')

    def __str__(self):
        return self.name