tring1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if len(str1) > len(str2):
    print(f'"{str1}" is longer than "{str2}".')
elif len(str1) < len(str2):
    print(f'"{str2}" is longer than "{str1}".')
else:
    print("Both strings are of equal length.")

