from django.db import models

class Punch_In(models.Model):
	hr_in  = models.IntegerField('Clock in hour', default=0)
	min_in = models.IntegerField('Clock in minute', default=0)

	hr_to_work  = models.IntegerField('Hours to work', default=0)
	min_to_work = models.IntegerField('Minutes to work', default=0)

	def __str__(self):
		lead_zero_min_in       = addLeadZero(self.min_in)
		lead_zero_min_to_work  = addLeadZero(self.min_to_work)

		return ("Start: " + str(self.hr_in) + ':' + lead_zero_min_in +
				"\nWork for: " + str(self.hr_to_work) + ':' +
				lead_zero_min_to_work)

class Leave_By(models.Model):
	hr_in     = models.IntegerField('Clock in hour', default=0) 
	min_in    = models.IntegerField('Clock in minute', default=0)

	hr_leave  = models.IntegerField('Clock out hour', default=0)
	min_leave = models.IntegerField('Clock out minute', default=0)

	def __str__(self):
		lead_zero_min_in    = addLeadZero(self.min_in)
		lead_zero_min_leave = addLeadZero(self.min_leave)

		return ("Start: " + str(self.hr_in) + ':' + lead_zero_min_in +
				"\nLeave at: " + str(hr_leave) + ':' + 
				lead_zero_min_leave) 

"""helper function"""

#function to add leading zero to minutes < 10
def addLeadZero(ttime):
	if ttime < 10:
		s_time = '0' + str(ttime)
	else:
		s_time = str(ttime)

	return s_time