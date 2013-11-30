from django.shortcuts import render, redirect
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
	name = forms.CharField(label=_('Name'))
	mail = forms.EmailField(label=_('Mail'), required=False)


def index(request):

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['name'], form.cleaned_data['mail'], 'pass')
			return redirect('index')
	else:
		form = RegistrationForm()
	return render(request, 'core/index.html', {'form': form})
