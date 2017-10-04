from django.db import models

# Create your models here.
class Companies(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	slug = models.SlugField(unique=True)


