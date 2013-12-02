from django.shortcuts import render, redirect
from django.forms import ModelForm
from core.models import Registration


class RegistrationForm(ModelForm):
	class Meta:
		model = Registration


def index(request):

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = RegistrationForm()
	return render(request, 'core/index.html', {'form': form})
