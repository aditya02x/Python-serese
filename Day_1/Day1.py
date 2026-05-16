name = input("Enter your name : ")
location = input("Enter your location : ")
print("Hello " + name + " from " + location)




num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
operator = input("Enter your operator : ")
if operator == "+":
    print(num1 + num2)  

elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:    print("Invalid operator")



celcius = float(input("Enter the temperature in Celsius : "))
fahrenheit = (celcius * 9/5) + 32
print("The temperature in Fahrenheit is : " + str(fahrenheit))