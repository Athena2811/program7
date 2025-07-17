        #fuctions

# def square(num):
#     return num**2
# object_=square(6)
# print("The square of the given number is:",object_)

# def square(num):
#     print(num**2)
# square(6)

        #Calling a function
# def a_function(string):
#     return len(string)
# print(a_function("Functions"))
# print(a_function("Python"))

    #with argument with return type
# def square(num):
#     return num*num
# result=square(5)
# print(result)

    #with argument without return type
# def greet(name):
#     print("Hello",name+"!")
# greet("Anu")

        #without argument with return type
# def get_message():
#     return "Welcome to python programming!"
# msg=get_message()
# print(msg)

        #without argument without return type
# def print_numbers():
#     for i in range(1,6):
#         print(i)
# print_numbers()

        #Default arguments
# def function(n1,n2=20):
#     print("Number 1 =",n1)
#     print("Number 2 =",n2)
# print("Passing only one argument")
# function(30)

        #Keyword arguments
# def function(n1,n2):
#     print("Number 1 is:",n1)
#     print("Number 2 is:",n2)
# print("Without using keyword")
# function(n1=50,n2=20)

# def process_data(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# process_data(1, 2, 3, name="Alice", age=30)

# def iseven(num):
#             if num%2==0:
#                 print(num, "is even")
#             else:
#                 print(num, "is odd")
# a=int(input("Enter a number: "))
# iseven(12)

#Factorial
# def fact_num(num):
#         fact=1
#         for i in range(1,num+1):
#                 fact=fact*i
#         return fact
# a=int(input("Enter a number: "))
# f=fact_num(a)
# print(f)

# def Display(name,age):
#         print(f"My name is {name} , Im {age} years old")
# Display(age=27 ,name="Bob",course="python")

# def fun(*num):
#         print(sum(num))
# fun(8,5,6,10)

# def display(**a):
#         print(f"")
# ans=0
# def add(x,y):
#         ans=x+y
#         display(f"sum of the numbers {x} and {y} is {ans}")
# def sub(x,y):
#         ans=x-y
#         display(f"difference of the numbers {x} and {y} is {ans}")
# def mul(x,y):
#         ans=x*y
#         display(f"product of the numbers {x} and {y} is {ans}")
# def div(x,y):
#         ans=x/y
#         display(f"Division of the numbers {x} and {y} is {ans}")
# def display():
#         print(v)
# choice=0
# while True:
#     print("1.ADDITION")
#     print("2.SUBSTRACTION")
#     print("3.MULTIPLICATION")
#     print("4.DIVISION")
#     print("5.EXIT")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#        a=int(input("Enter a number: "))
#        b=int(input("Enter a number: "))
#        add(a,b)
#     elif choice==2:
#        a=int(input("Enter a number: "))
#        b=int(input("Enter a number: ")) 
#        sub(a,b)
#     elif choice==3:
#        a=int(input("Enter a number: "))
#        b=int(input("Enter a number: "))
#        mul(a,b)
#     elif choice==4:
#         a=int(input("Enter a number: "))
#         b=int(input("Enter a number: "))
#         if b!=0:
#             div(a,b)
#         else:
#             print("not defined")
#     elif choice==5:
#         break
#     else:
#         print("Invalid choice")
#         break


# for i in range(1,6):
#         for j in range(1,i+1):
#                 print(i*j,end=" ")
#         print()

# for r in range(5):
#         n=65
#         for j in range(r+1):
#                 print(chr(n),end=" ")
#                 n+=1
#         print("")


# #Global
# a=10
# def fun():
#         global a
#         a+=10
#         print(a)
# fun()

#Recursion
# def fact(num):
#         if num==1:
#                 return num
#         else:
#                 return num*fact(num-1)
# print(fact(7))

# def sample():
#         print('HELLO')
#         sample()
# sample()

first, second=0,1
print(first,second,end=" ")
for j in range(8):
        third=first+second
        print(third,end=" ")
        first,second=second,third