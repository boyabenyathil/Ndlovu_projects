temp= ""
while temp!="0":
	temp= input('Enter temperature: ')
	if int(temp) >=100:
		msg='its hot: '
	elif int(temp) <=60:
		msg='its cold'
	elif  int(temp) < 100 and int(temp) > 60:
		msg='its right: '
	print(msg)

pass
	
