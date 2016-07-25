from django import forms
from .models import Punch_In

class PunchInForm(forms.ModelForm):
	class Meta:
		model  = Punch_In
		fields = ('hr_in','min_in','hr_to_work','min_to_work',)
