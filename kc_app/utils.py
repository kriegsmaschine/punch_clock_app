from kc_app.utilClass import Punch_In_Copy

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