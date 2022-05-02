from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

CATEGORIES = ((0, 'Facial'), (1, 'Hands and Feet'), (2, 'Massage'))

# Treatment Model
class Treatment(models.Model):
    """ TreatmentModel """
    featured_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.IntegerField(choices=CATEGORIES)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return self.title


# Client Model
class Client(models.Model):
    """ ClientModel """
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Booking Model
class Booking(models.Model):
    """ BookingModel """
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    date_of_treatment = models.DateField()
    time_of_treatment = models.TimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client} {self.treatment}"
