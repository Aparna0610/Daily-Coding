print("IF STATEMENTS")

is_female = False
is_tall = False

if is_female and is_tall:
    print("You are a tall female")
elif is_female and not(is_tall):
    print("You are a short female")
elif not(is_female) and is_tall:
    print("You are a tall male")
else:
    print("You are a short male")
print("\n")
if is_female or is_tall:
    print("You are a female or tall or both")
else:
    print("You are neither a female nor tall")