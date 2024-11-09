# 1. Conditional Statements
#1.1. Simple If-Else Statements
#1.2. Nested If Statements

#2. Loops (for, while)

#3. Break and Continue Statements
#3.2. Continue Statement

#4. List Comprehensions


#####################################
# input


X = float(input("add 1st num "))
Y = float(input("Add 2nd num "))
Z =X + Y
print(Z)

number = float(input("Add number u wanna Test "))
if number > 0 :
    print("Positive")
elif number < 0 :
    print("Negative ")
else:
    print("Zero")
    
#############################
number = int(input("Check even or odd  "))

if number %2 == 0 :
    print("Even")
    print(number %2)
else:
    print("Odd")
    print(number %2)

# 4/2 = 2.0 --> 0
# 3/2 = 1.5  --> .5

###########################

if number <=10 :
    print("LOW")
elif number >=11 and number <=20 :
    print("Meduim")
elif number >= 21 and number <= 30:
    print("High")
else :
    print("Out of range ")


#2. Loops (for, while)



for adham in  range(100) :
    print(adham)

for i in range(1, 11):
    print(i)


for i in range(1 , 101):
    # i= 1
    # i = 2
    if i % 2 ==0 :# 1 --> Flase
        print(i)


# list
# [1 ,  2.5  , 7 ,7  ]
# ['Ahmed' , 'yaser' ]
lst = [1 , 2 , 3 , 4]
# index 1 -->0


#print(lst[0])
str_lst=["Ahmed" , "Yasser" , "Sara"  , "Menna"]

print(str_lst[1:4])


fruits = ["apple", "banana", "cherry"]
print('##############################################################')
for X in fruits :
    if X == "apple":
        print(fruits[0])



numbers = [1, 2, 3, 7, 8, 9]
for num in numbers:
    if num == 7:
        print("Stopped at 7")
        break
    print(num)

#######################
favorite_foods = ["pizza", "ice cream", "pasta"]

for food in favorite_foods:
    print('I Love ' , food)




# Countdown from 5 to 1

count= 5
while count >0 :
    print(count)
    count =  count-1

print("Countdown complete!")

#3. Break and Continue Statements

#Finding a target number and stopping the loop.


numbers = [1, 3, 5, 7, 9, 11]
target = 7

for num in numbers:
    if num == target:
        print("Found the target:", target)
        break

#Looping through names and breaking when you find "Alice."
names = ["Jack", "Tom", "Alice", "Anna"]

for name in names:
    if name == "Alice":
        print("Alice found!")
        break
    print(name)


#Skipping even numbers.
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip the rest of the code in the loop if i is even
    print(i)
#Ignoring certain items in a list.
items = ["apple", "banana", "cherry", "durian"]

for item in items:
    if item == "banana":
        continue  # Skip "banana"
    print(item)

#List Comprehensions

#Create a list of squares for numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]
print(squares)

#Filtering only the odd numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)

#Create a list of first names from a list of full names.

names = ["John Doe", "Jane Smith", "Alice Johnson"]
first_names = [name.split()[0] for name in names]
print(first_names)



"""


"""