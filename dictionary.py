student = {'name': 'John', 'age': 26, 'courses': ['Math', 'CompSci']}
# student['phone'] = '555-55555'
# student['name'] = 'Jane'
student.update({'name': 'Jane', 'age': 22, 'phone': '555-55555'})
del(student['age'])
phone = student.pop('phone')
print(student, student['courses'], student.get('phone', 'Not Found'), phone, len(student))
print(student.keys(), student.values(), student.items())

for key, value in student.items():
    print(key, value)