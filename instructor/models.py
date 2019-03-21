from django.core.validators import RegexValidator

from django.db import models


class Instruct(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
	course_name = models.CharField(max_length=20)

	def __str__(self):
		return self.first_name + " " + self.last_name
