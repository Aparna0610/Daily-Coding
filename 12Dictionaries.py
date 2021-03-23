monthConversions = { "Jan": "January",
                     "Feb": "February",
                     "Mar": "March",
                     "Apr": "April",
                     "May": "May",
                     "Jun": "June",
                     "Jul": "July",
                     "Aug": "August",
                     "Sep": "September",
                     "Oct": "October",
                     "Nov": "November",
                     "Dec": "December"
}

print(monthConversions)
print("\n Printing a value for a key")
print(monthConversions["Nov"])

print("\n Printing a value using get function")
print(monthConversions.get("Apr"))

print("\n Second parameter(default value) in get function for dict///Otherwise for a key that does not exist in dict, None is returned")
print(monthConversions.get("Lec", "Not a Valid Key"))

monthConversions = { 0: "January",
                     1: "February",
                     2: "March",
                     3: "April",
                     4: "May",
                     5: "June",
                     6: "July",
                     7: "August",
                     "Sep": "September",
                     "Oct": "October",
                     "Nov": "November",
                     "Dec": "December"
}
print(monthConversions)