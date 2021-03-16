print("\nLISTS ARE MUTABLE")
lucky_numbers = [4, 8, 15, 20, 26, 33, 41]
friends = ["Klimu", "Pathu", "Gachu", "Abhi", "Shalu"]
print(friends)

print(friends[3])

print(friends[-2])

print("\n SLICING")
print(friends[1:4])
print(friends[2:])
print(friends[-2:])
print(friends[:-3])

print("\n Mutable Lists")
friends[1] = "Dipu"
print(friends)

print("\nEXTEND FUNCTION - APPEND ANOTHER LIST TO A LIST")
friends.extend(lucky_numbers)
print(friends)

print("\n APPEND FUNCTION - APPEND ANOTHER ITEM ON TO THE END OF THE LIST")
friends.append("Pittu")
print(friends)

print("\n INSERT FUNCTION - ADD AN ITEM IN TO THE MIDDLE OF THE LIST")
friends.insert(5, "Pathu")
print(friends)

print("\n REMOVE FUNCTION - REMOVE ITEMS FROM THE LIST")
friends.remove("Pittu")
print(friends)

print("\n CLEAR FUNCTION - REMOVE ALL ITEMS FROM A LIST")
print(lucky_numbers)
lucky_numbers.clear()
print(lucky_numbers)

print("\n POP FUNCTION - REMOVES LAST ITEM FROM THE LIST")
friends.pop()
print(friends)

print("\n INDEX FUNCTION - SAME AS IN STRINGS")
print(friends.index("Dipu"))
'''print(friends.index("Ami")) '''

friends.append("Abhi")

print("\n COUNT FUNCTION - COUNTS HOW MANY TIMES A VALUE SHOWS UP IN THE LIST")
print(friends.count("Abhi"))

friends.clear()
friends = ["Abhi", "Klimu", "Shalu"]
lucky_numbers = [23, 12, 34, 5]
print(friends)
print("\n SORT FUNCTION - SORT THE LIST IN ASC ORDER")
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

print("\n REVERSE FUNCTION - REVERSES ITEMS IN A LIST")
lucky_numbers.reverse()
print(lucky_numbers)

print("\n COPY FUNCTION - COPIES ITEMS OF A LIST TO ANOTHER LIST")
friends2 = friends.copy()
print(friends2)