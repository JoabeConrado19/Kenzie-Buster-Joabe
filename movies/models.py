from django.db import models
from users.models import User

# Create your models here.

class RatingChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    

class Movie(models.Model):
    title = models.CharField(null=False, max_length=127)
    duration = models.CharField(null= True, max_length=10, default=None)
    rating = models.CharField(null=False, max_length=20, choices=RatingChoices.choices, default="G")
    synopsis = models.CharField(null=True, default=None, max_length=500)
    added_by = models.CharField(null=True, max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movies", null=True)

class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    buyed_by = models.CharField(max_length=100, null=True)
    title = models.CharField(null=True, max_length=127)



    