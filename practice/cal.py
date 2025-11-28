print("select operations:")
print("1. add:")
print("2. subtract:")
print("3. multiply:")
print("4. division:")

choice = input("enter choice  (1/2/3/4):")

num1 =float(input("enter first num:"))
num2 =float(input("enter second  num:"))

if choice == '1':
    result = num1 + num2
    print("Result: ", result)
elif choice == '2':
    result = num1 - num2
    print("Result: ", result)
elif choice == '3':
    result = num1 * num2
    print("Result: ", result)
elif choice == '4':
    result = num1 / num2
    print("Result: ", result)
else:
    print("Invalid input")



