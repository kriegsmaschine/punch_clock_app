class Punch_In_Copy():
	def __init__(self, hr_in, min_in, hr_to_work, min_to_work):
		self.hr_in       = int(hr_in)
		self.min_in      = int(min_in)
		self.hr_to_work  = int(hr_to_work)
		self.min_to_work = int(min_to_work)

class Time_To_Leave():
	def __init__(self, hr_in, min_in, hr_to_leave, min_to_leave):
		self.hr_in       = int(hr_in)
		self.min_in      = int(min_in)
		self.hr_leave    = int(hr_to_leave)
		self.min_leave   = int(min_to_leave)