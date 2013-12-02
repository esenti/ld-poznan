from django.db import models
from django.utils.translation import ugettext_lazy as _

class Registration(models.Model):
	name = models.CharField(_('Name'), max_length=200)
	mail = models.EmailField(_('Email'), max_length=200, blank=True)
	info = models.TextField(_('Additional info'), max_length=4000, blank=True)
	time_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name