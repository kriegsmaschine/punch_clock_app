from kc_app.utilClass import Punch_In_Copy

form = {'hr_in':7,'min_in':21,'hr_to_work':8,'min_to_work':15,}
print(form)

p = Punch_In_Copy(form['hr_in'], form['min_in'],
				  form['hr_to_work'], form['min_to_work'])
print(str(p.hr_in) + '\n' + str(p.min_in) + '\n' +
	  str(p.hr_to_work) + '\n' + str(p.min_to_work) + '\n')

p.hr_in = 11
print("p.hr_in now is: %d" % p.hr_in)