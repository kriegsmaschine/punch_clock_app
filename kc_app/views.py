from django.shortcuts import render
from .models import Punch_In
from .forms import PunchInForm
from .utils import *

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	if request.method == 'POST':
		form = PunchInForm(request.POST)
		if form.is_valid():
			#form.save()
			final_out = getClockOutTime(form)
			dict_form = {'hr_in':form['hr_in'].value(),
						 'min_in':int(form['min_in'].value()),
						 'hr_to_work':form['hr_to_work'].value(),
						 'min_to_work':int(form['min_to_work'].value()),
						}
			
			return render(request, 'kc_app\\clock_out.html', 
						 {'kc_form':dict_form,'punch_out':final_out})
	else:
		form = PunchInForm()

	return render(request, 'kc_app\\index.html', {'form':form})

'''
def hours_worked(request):
	if request.method == 'POST':
		form = PunchInForm(request.POST)
		if form.is_valid():
			#form.save()
			hrs_worked = getHoursWorked(form)
			return render(request, 'kc_app\\hours_worked.html',
						 {'kc_form':form,'hrs_worked':hrs_worked})
	else:
		form = PunchInForm()

	return render(request, 'kc_app\\leave_at.html', {'form':form})

'''