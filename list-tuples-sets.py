############## Lists (mutable/ can be modified) ##################################################
courses = ["history", "math", "physics", "compsci"]
# print(courses, courses[-1], courses[:2], courses[2:])
courses.append('art')
courses.insert(0, 'chemistry')
courses_2 = ["environmentalsci", "geography"]
courses.extend(courses_2)
# print(courses)
popped = courses.pop()
# print(courses, popped)
courses.remove('environmentalsci')
# print(courses)
courses.reverse()
# print(courses)
sorted_courses = sorted(courses)
# print(sorted_courses)
courses.sort(reverse=True)
# print(courses)

num = [1,2,3,4,5]
# print(min(num), max(num), sum(num), num.index(3), 6 in num, 4 in num)

# for index, course in enumerate(courses, start=1):
#     print(index, course)

course_str = ', '.join(courses)
# print(course_str)

new_list = course_str.split(', ')
# print(new_list)

list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1
# print(list_1, list_2)
list_1[0] = 'Art'
# print("Mutable", list_1, list_2)

############## Tuples (immutable/ cannot be modified) ##################################################
tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1
# print(tuple_1, tuple_2)
# tuple_1[0] = "Art"
# print("Immutable", tuple_1, tuple_2)

############## Sets ##################################################
cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}
art_courses = {"History", "Math", "Art", "Design"}
print(cs_courses, "Math" in cs_courses, 
      cs_courses.intersection(art_courses), cs_courses.difference(art_courses),
      cs_courses.union(art_courses))



# Empty list
empty_list = []
empty_list = list()

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty set
empty_set = {} # wrong, {} will create dictionary
empty_set = set()