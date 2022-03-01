
#accessing element by index
students = ['Lusani', 'Nikky', 'Waston', 'Lusani', 'Destiny']
student = students[0]
print(student)

#removing element using index
studentt = students[2]
students.remove(studentt)
print(students)

#editing elements
students[0]='Ndlovu'
print(students)

alphabets = ['M', 'N', 'O', 'Q', 'D', 'M', 'N', 'O']
print(f'The index of O is {alphabets.index("O" , 5)}')
