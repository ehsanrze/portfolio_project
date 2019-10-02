from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=30)
	pub_date = models.DateTimeField()
	body = models.CharField(max_length=250)
	image = models.ImageField()
