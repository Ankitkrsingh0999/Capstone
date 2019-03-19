from django import forms
from .models import Instruct

class instructForm(forms.ModelForm):
	class Meta:
		model = Instruct
		fields = ('first_name',
				  'last_name',
				  'email',
				  'phone',
				  'course_name')