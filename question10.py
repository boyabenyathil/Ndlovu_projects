total = 0
for x in range(5):
	marks = input(f'Enter a mark of test {x + 1}: ')
	total = int(total) + int(marks)
average = total/5
percentage = (total / 500) * 100
if percentage >= 60:
	symbol = 'Distiction'
elif percentage <= 59 and percentage >= 50:
		symbol = 'Merit'
elif percentage <= 49:
		symbol = 'Fail'
print(f'average: {average} , percentage: {percentage}% , symbol: {symbol}')

