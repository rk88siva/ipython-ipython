# rec_ex.py

def rec_sum(a_list):
	if a_list == []:
		return 0
	
	else:	
		return a_list[0]+rec_sum(a_list[1:])


def fact(n):
	if n<0:
		return "Error - cannot accept neg number."
	elif n==0:
		return 1
	else:
		return n*fact(n-1)