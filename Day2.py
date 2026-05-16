#condions lopps & functions

#conditions

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:    print("You are a minor.")

#operator 
# and or not 

id = True
if age >= 18 and id == True:
    print("You are an adult with ID.")
else:    print("You are either a minor or do not have ID.")


#Loops 

for i in range(5):
    print(i)

    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)



        #while loop
count  = 1 
while count <= 10:
    print(count)
    count += 1