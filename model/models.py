from django.db import models

# Create your models here.

#Table fields for saving the data
class Quiz(models.Model):
    user_name = models.CharField(max_length=122)
    best_player = models.CharField(max_length=122)
    flag_color = models.CharField(max_length=122)