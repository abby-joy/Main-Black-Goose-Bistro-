courses = ["MIT", "Cybersecurity", "Datascience"]
print(courses)

#Accessing an element in array
print(courses[1])
print(courses[2])
print(courses[0])

#Looping through array
for y in courses:
     print("course is", y)

#Adding a new element
courses.append("Android Development")
print(courses)

#Removing an element
courses.remove("MIT")
print(courses)

