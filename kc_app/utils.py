from kc_app.utilClass import Punch_In_Copy, Time_To_Leave

def getClockOutTime(form):
	'''
	Variable map from original c++ code
	
	t1.hours   = hr_in
	t1.minutes = min_in
	t2.hours   = hr_to_work
	t2.minutes = min_to_work
	'''

	#convert form PunchInForm to type class instead of dictionary
	#class Punch_In_Copy converts BoundField to int
	tform = Punch_In_Copy(form['hr_in'].value(), form['min_in'].value(),
				  	 form['hr_to_work'].value(), form['min_to_work'].value())

	checkTime(tform)
	differ = timeToWork(tform)
	fout = formatOutput(differ)
	return fout

#add 30 minutes to clock in time for the lunch break
def checkTime(tform):
	if tform.hr_in >= 6:
		tform.min_in += 30
		if tform.min_in > 59:
			tform.hr_in += 1
			tform.min_in -= 60

def timeToWork(tform):
	tdiffer = {'hours':0, 'minutes':0}
	thour = 0
	t1_hr  = tform.hr_in
	t1_min = tform.min_in 

	if tform.min_in + tform.hr_to_work > 59:
		thour += 1

		t1_hr += tform.hr_to_work + thour
		t1_min = (t1_min + tform.min_to_work) - 60
	else:
		t1_hr  += tform.hr_to_work
		t1_min += tform.min_to_work

	tdiffer['hours']   = t1_hr
	tdiffer['minutes'] = t1_min

	return tdiffer

def formatOutput(tdiffer):
	upperHr = lowerHr = tdiffer['hours']
	upperMin = tdiffer['minutes'] + 7
	lowerMin = tdiffer['minutes'] - 7

	if tdiffer['minutes'] + 7 > 59:
		upperHr  = tdiffer['hours'] + 1
		upperMin = tdiffer['minutes'] + 7 - 60
		lowerMin = tdiffer['minutes'] - 7

	if tdiffer['minutes'] - 7 < 0:
		lowerHr  = tdiffer['hours'] - 1
		lowerMin = tdiffer['minutes'] - 7 + 60
		upperMin = tdiffer['minutes'] + 7

	if upperHr > 12:
		upperHr -= 12
	if lowerHr > 12:
		lowerHr -= 12

	tfout = {'lower_hr':lowerHr, 'lower_min':lowerMin,
			'upper_hr':upperHr, 'upper_min':upperMin}

	return tfout




'''
get time must leave by return total time worked from
	clock in to time to leave
'''

def checkRemoveBreak(tdiff):
	if tdiff.hr_leave >= 6:
		tdiff.min_leave -= 30

		if tdiff.min_leave < 0:
			tdiff.hr_leave -= 1
			tdiff.min_leave += 60

def getTimeDifference(tform):
	tdiff = Time_To_Leave(0,0,0,0)

	tdiff.hr_leave = tform.hr_leave - tform.hr_in
	if tdiff.hr_leave < 0:
		tdiff.hr_leave = tform.hr_leave + 12 - tform.hr_in
	else:
		tdiff.hr_leave = tform.hr_leave - tform.hr_in

	tdiff.min_leave = tform.min_leave - tform.min_in
	if tdiff.min_leave < 0:
		tdiff.min_leave += 60
		tdiff.hr_leave  -= 1

	if tdiff.hr_leave <= 1:
		tdiff.hr_leave += 12

	checkRemoveBreak(tdiff)
	return tdiff

def getHoursWorked(form):
	tform = Time_To_Leave(form['hr_in'].value(), form['min_in'].value(),
				  		  form['hr_leave'].value(), form['min_leave'].value())

	diff = getTimeDifference(tform)

	return diff

