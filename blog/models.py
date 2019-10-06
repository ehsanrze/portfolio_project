from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=30)
	pub_date = models.DateTimeField()
	body = models.CharField(max_length=250)
	image = models.ImageField()
	def date(self):
		return self.pub_date.strftime('%b %e %Y')
	def __str__(self):
		return self.title