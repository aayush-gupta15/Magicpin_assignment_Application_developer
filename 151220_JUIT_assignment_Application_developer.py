''' Sunday 24-Feb-2019
    Aayush Gupta
    151220
    jUIT'''

import re

def password_checker(password):
	
	# Checking each condition
	if len(password) < 6:
		return 'Failure Password must be at least 6 characters long.'
	
	if len(password) > 12:
		return 'Failure Password must be at max 12 characters long.'
	
	if re.search(r"[a-z]", password) is None:
		return 'Failure Password must contain at least one letter from a-z.'
	
	if re.search(r"\d", password) is None :
		return 'Failure Password must contain at least one digit from 0-9.'

	if re.search(r"[A-Z]", password) is None :
		return 'Failure Password must contain at least one letter from A-Z.'
	
	if re.search(r"[*$_#=@]", password) is None:
		return 'Failure Password must contain at least one letter from *$_#=@.'
		 	
	if re.search(r"[%!)(]", password) is not None:
		return 'Failure Password cannot contain %!)(.'
	
	if ' ' in password or '\t' in password:
		return 'Failure Password must not contain whitespaces.'

	return 'Success'
	
	

string = raw_input()
# Splitting and Stripping string to form list of passwords. 
pass_list = [x.strip() for x in string.split(',')]
for each in pass_list:
	print("%s %s" % (each, password_checker(each)))
