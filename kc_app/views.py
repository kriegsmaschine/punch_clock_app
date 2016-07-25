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
			form.save()
			final_out = getClockOutTime(form)
			return render(request, 'kc_app\\clock_out.html', 
						 {'kc_form':form,'punch_out':final_out})
	else:
		form = PunchInForm()

	return render(request, 'kc_app\\index.html', {'form':form})
