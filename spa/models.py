from django.db import models
from django.contrib.auth.modelas import User
from cloudinary.models import CloudinaryField

CATEGORIES = ( 'Facials', 'Hands and Feet', 'Massage')


# Treatment Model
class Treatment(models.Model):
    """ TreatmentModel """
    image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.DurationField()


# Client Model
class Client(models.Model):
    """ ClientModel """
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    date_of_treatment = models.DateField()
    time_of_treatment = models.TimeField()
    length_of_treatment = models.DurationField()


# Booking Model
class Booking(models.Model):
    """ BookingModel """
    client = 

# Category Model
class Category(models.Model):
    """ CategoryModel """
    categories = models.(
