# 1. Variables and Data Types
# 1.2. Data Types
# 1.3. Type Conversion
# 1.4. Type Checking


#2. Basic Operators
#2.1. Arithmetic Operators
#2.2. Comparison Operators
#2.3. Logical Operators


#3. String Manipulation
#3.1. Basic String Operations
#3.2. String Methods
#3.3. String Slicing

########################################################################################################################


# variable
age = 25 # integer variable
name = "ahmed" # string variable
is_student =True # boolean Variable

# Data Types

num = 10
print(type(num))

price = 15.5
print(type(price))

greeting = "Hello , World !"
print(type(greeting))

is_valid=True
print(type(is_valid))


result  = 10 + 15.5 # 25.5
print(type(result))

result = 1.5+1.5 # 3 or 3.0
float = float(result) # 3.0
int= int(result) # 3
STR = str(result)
print("#####################################")
print(type(float))
print(type(int))
print(type(STR))

#Arithmetic Operators
print("Arithmetic Operators")
sum  = 5+3
print(sum )
difference = 10 - 4
print(difference)
product = 7*6
print(product)
quotient = 20 / 4
print(quotient)

Floor= 22//7
print(Floor)
Floor= 22/7
print(Floor)
power = 2**3
print(power)


#2.2. Comparison Operators

print("Comparison Operators")
is_equal = (5  == 5)
print(is_equal)

is_not_equal = (5 != 3)
print(is_not_equal)

greater = (10 > 5)
print(greater)


less = (5 < 10)
print(less)

greater_equal = (10 >= 10)
print(greater_equal)

less_equal = (5 <= 8)
print(less_equal)

result = ( 5 < 3 ) or  (2 < 5)  # and

print(result)









# 3. String Manipulation




full_name = "John" + " " + "Doe"
print(full_name)

echo = "Hello! " * 3
print(echo)

length = len("Hello")
print(length)

upper_case = "hello".upper()
print(upper_case)

cleaned = "  hello  ".strip()
print(cleaned)

new_string = "Hello world".replace("world", "Python")
print(new_string)

words = "Hello world".split()
print(words)

joined = ", ".join(["apple", "banana", "cherry"])
print(joined)



