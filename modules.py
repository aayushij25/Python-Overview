# import my_module as mm
# from my_module import * 
# import antigravity
from my_module import find_index as fi, test

courses = ["Math", "History", "Physics", "CompSci"]

# index = mm.find_index(courses, 'History')
index = fi(courses, 'CompSci')
print(index, test)