
temp = input("is it hot today (yes/no/moderate): ")
temp.lower()
if temp == 'yes':
	msg = "Drink gallons of water"
elif temp == 'no':
	msg = "Wear warm clothes"
else:
	msg = "Enjoy your day"

print(msg)



name=''
while len(name) == 0:
	name= input("Enter your name: ")
print(f'Hello {name}')


for x in range(10):
	print('')
	for y in range(10):
		print(f'{x} x {y} = {x*y}')
