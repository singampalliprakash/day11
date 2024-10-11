price = float(input("Enter the price: "))
is_member = input("Are you a member? (yes/no): ")
if price > 100 and is_member:
    print("Eligible for a 20% discount of:",price)
elif price > 100:
    print("Eligible for a 10% discount of",price)
else:
    print("Not eligible for a discount")
