from django import forms
from .models import Punch_In, Leave_By

class PunchInForm(forms.ModelForm):
	class Meta:
		model  = Punch_In
		fields = ('hr_in','min_in','hr_to_work','min_to_work',)

class LeaveByForm(forms.ModelForm):
	class Meta:
		model  = Leave_By
		fields = ('hr_in','min_in','hr_leave','min_leave',)
