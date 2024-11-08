
number = 25 #Integer
second = 56.78 #float
text = "Hello there" #string
isPythonInteresting = True #Boolean

#Ata Structures- Multiple values stored in a single variable
cars = ["Toyota","Nissan","Vw"] #List-Ordered and changeable
fruits = ("Banana","Orange","Apple") #Tuple-ordered but unchangeable
countries = {"Kenya","Tunisia","Algeria"} #Set-unordered and unchangeable
student = {
    "firstname" : "Mary",
    "age" : 34,
    "course" : "Web development",
    "nationality" : "Kenyan"
} # Dictionary-Key and value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["nationality"])

print(number)
print(second)
print(text)
print(isPythonInteresting)


#Determining a data type
print(type(countries))
print(type(student))
print(type(second))

# Typecasting-Process of converting from one datatype to another
print(float(number))
print(int(second))