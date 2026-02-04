
age = 18 #integer
weight = 47.54 #Float
greeting = "Hello there" #String
isMammal = True #Boolean

#Data structures - Multiple elements in one variable
fruits = ["Banana","Mango","Cherry"] #List - Ordered and changeable
courses = ["MIT","Datascience","Cybersecurity"] #Array - Similar datatypes
cars = ("Ford", "G-Wagon","Mazda","Mistubishi") #Tuple - Ordered and unchangeable
countries = {"Tanzania","India","Italy"} #Set - Unordered and unchangeable
student  = {
    "firstname": "Jeff",
    "course": "MIT",
    "age": 18,
    "nationality": "Kenya"

} #Dictionary - Key value pair

print("Student is", age , "years old")
print(weight)
print("is animal a mammal ? :", isMammal)
print(fruits)
print(countries)

#Typecasting - Converting one data type to another
print(float(age))
print(int(weight))
