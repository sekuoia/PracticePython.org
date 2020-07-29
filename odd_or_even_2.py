num = int(input("Please enter a number: "))
check = int(input("Please enter another number: "))
result = num / check

if num % check == 0:
    print("Your second number divides evenly into your first number.")
    print(f"{num} '/' {check} = {result}")
else:
    print("Your second number does not divide evenly into your first number.")