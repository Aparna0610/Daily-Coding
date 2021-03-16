from math import *

print("Hello World")

character_name = "Aparna"
character_age = 28
is_Male = False

person_reflections = 'Aparna\'s reflections'

print("Her name is " + character_name+ ".")
print("She is " +str(character_age)+ " years old.")

print('\n Aparna\'s traumas')
print(person_reflections + " are cool")

print("\n" + person_reflections.upper())

print("\n Concatenation only with Strings in print")
print("Checking if capitals:" + str(person_reflections.isupper()))

print("\n")

print(person_reflections.upper().isupper())

print("\n FIND LENGTH")
print(len(person_reflections))

print("\n Grabbing specific chars from string")
print(person_reflections[0])

print("\n Grabbing Index 1")
print(person_reflections.index("p"))

print("\n Grabbing Index 2")
print(person_reflections.index("flections"))

print("\n Replace")
print(person_reflections.replace("reflections", "traumas"))

print("\n NUMBERS")
print(5.0879)
print(-9)
print(-9 + 7)

print("\n ABS value of numbers")
my_num = -5
print(abs(my_num))

print("\n Finding power of numbers")
print(pow(my_num, 3))

print("\n MIN n MAX")
print(max(my_num, -2))
print(min(my_num, -2))

print("\n ROUND")
print(round(3.456))

print("\n FLOOR")
print(floor(3.7))

print("\n CEIL")
print(ceil(3.6))

print("\n Square root")
print(sqrt(4))

print("\n Getting input from a user")
input("Enter your name: ")