from django.shortcuts import render
from .forms import instructForm
# Create your views here.
def instr(request):
	template="instruct.html"

	if request.method == "POST":
		form = instructForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = instructForm()

	context = {
		'form' : form ,
	}			

	return render(request, template, context)