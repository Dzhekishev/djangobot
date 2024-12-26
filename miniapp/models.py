from django.db import models

# Create your models here.


class Info(models.Model):
	name=models.CharField('name', max_length=100)
	description=models.TextField('description')
	image = models.ImageField(upload_to='product_images/', blank=True, null=True)


	def __str__(self):
		return self.name


class Phrases(models.Model):
	name=models.CharField('name', max_length=200)
	words=models.TextField('words')
	image=models.ImageField(upload_to='product_images/', blank=True, null=True)


	def __str__(self):
		return self.name