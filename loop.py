# # #while loop
# count=10
# while count>=1:
#     print(count)
#     count-=1

# # #even numbers
# count=int(input("enter : "))
# while count<=10:
#     if count%2==0:
#         print(count)
#     count+=1
# sum=0
# i=int(input("enter the number: "))
# while i!=-1:
#     sum=sum+i
#     i=int(input("enter the number"))
# print(sum)

# #Sum of digits
# sum=0
# n=0
# i=int(input("enter a number: "))
# while i!=0:
#     n=i%10
#     sum+=n
#     i=i//10
# print(sum)

# #Palindrome number
# temp=0
# rev=0
# i=int(input("enter a number: "))
# temp=i
# while temp!=0:
#     n=temp%10
#     rev=rev*10+n
#     temp=temp//10
# if rev==i:
#     print("It is a palindrome number")
# else:
#     print("It is not a palindrome number")

# #count the number of digits
# n=0
# count=0
# i=int(input("enter a number: "))
# while i!=0:
#     n=i%10
#     count +=1
#     i=i//10
# print(count)

# #digit
# i=int(input("enter a number: "))
# d=int(input("enter a digit"))
# while i!=0:
#     n=i%10
#     if n==d:
#         print("the digit is found")
#     else:
#         print("invalid")
#     i=i//10

#armstrong number
# n=0
# sum=0
# i=int(input("enter a number: "))
# temp=i
# while temp>0:
#     n=temp%10
#     sum+=n**3
#     temp=temp//10
# if sum==i:
#     print("it is an armstrong number")
# else:
#         print("it is not an armstrog number")

# print(range(15))
# print(list(range(15)))
# print(list(range(4,9)))
# print(list(range(5,25,4)))

# tuple_ =("Python","Loops","Sequence","Condition","Range")
# for iterator in range(len(tuple_)):
#     print(tuple_[iterator].upper(),end=" ")

# numbers=[4,2,6,7,3,5,8,10,6,1,9,2]
# square=0
# squares=[]
# for value in numbers:
#     square=value**2
#     squares.append(square)
# print("The list of squares is",squares)

# string="Python Loop"
# for s in string:
#     if s=="o":
#         print("If Block")
# else:
#     print(s)

# #for loop
# i=int(input("enter the number: "))
# rev=0
# n=len(str(i))
# for a in range(n):
#     n=i%10
#     rev=rev*10+n
#     i=i//10
# print(rev)

# num=int(input("enter a number: "))
# for i in range(1,num+1):
#     if i%2==0:
#         print(i)

# j=int(input("enter a range: "))
# num=int(input("enter a number: "))
# mul=0
# for i in range(1,j+1):
#     mul=i*num
#     print(i,"*",num ,"=",mul)    

#pattern
# for i in range(0,4):
#     for j in range(0,6):
#         print("* ",end=" ")
#     print()

# n=5
# count=0
# for i in range(0,n):
#     for j in range(0,n ):
#         count+=1
#         print(count," ",end=" ")
#     print()

# n=5
# count=0
# for i in range(0,n):
#     for j in range(0,i+1):
#         count+=1
#         print(count,end=" ")
#     print()

# Inverted right pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("* ",end=" ")
#     print()

# #Left hand pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()

#Right pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("* ",end=" ")
#     print()

# #Floyd'S triangle
# n=5
# count=0
# for i in range(0,n):
#     for j in range(0,i):
#         count+=1
#         print(count," ",end=" ")
#     print()

# #Full pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()

 #hourglass pyramid
# n=5
# for i in range(n,0,-1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#         print(" * ",end=" ")
#     print()
# n=5
# for i in range(0,n+1):
#     for j in range(0,n-i):
#         print(" ", end=" ")
#     for k in range(0,i+1):
#         print(" * ",end=" ")
#     print()

#Rhombus
# n=5
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end="")
#      for k in range(0,n-1):
#         print("*",end=" ")
#     print()

#Inverted triangle
# n=5
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for k in range(0,n-i):
#         print(" * ",end=" ")
#     print()

# #Inverted leftangle triangle
# n=5
# for i in range(0,n):
#     for j in range(0,i):
#         print("   ",end="")
#     for k in range(0,n-i):
#             print("* ",end=" ")
#     print()

#Hallow square
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("* ",end="")
#         else:
#             print(" ",end=" ")
#     print()
# # #Hallow full pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(end=" ")
#     for k in range(0,i+1):
#         if(i==0  or k==0 or k==n-1 or i==n-1 or k==i ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #Diamond
# n=5
# for i in range(0,n-1):
#     for j in range(0,n-i):
#         print("",end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()
# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("",end=" ")
#     for k in range(0,n-i):
#         print("*",end=" ")
#     print()
#Hallow diamond
# n = 5
# for i in range(0, n):
#     for j in range(0, n - i):
#         print(" ", end="")

#     for k in range(0, i + 1):
#         if k == 0 or k == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#hallow inverted triangle
# n=5
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print(" ", end="")

#     for k in range(0, n - i):
#         if k == 0 or k == n - i - 1 or i==0 :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # to print A
# n=6
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(end=" ")
#     for k in range(0,i+1):
#         if(i==3 or k==0 or k==n-1 or k==i ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# #mennudriven program
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
#        sum=a+b
#        print(sum)
#     elif choice==2:
#        a=int(input("Enter a number: "))
#        b=int(input("Enter a number: ")) 
#        sub=a-b
#        print(sub)
#     elif choice==3:
#        a=int(input("Enter a number: "))
#        b=int(input("Enter a number: "))
#        mul=a*b
#        print(mul)
#     elif choice==4:
#         a=int(input("Enter a number: "))
#         b=int(input("Enter a number: "))
#         if b!=0:
#             div=a/b
#             print(div)
#         else:
#             print("not defined")
#     elif choice==5:
#         break
#     else:
#         print("Invalid choice")
#         break 
#Menudriven prgm2
# choice=0
# name=0
# age=0
# address=0
# username=0
# p=0
# usrname=0
# p2=0
# while True:
#     print("1.REGISTRATION")
#     print("2.LOGIN")
#     print("3.Exit")
#     choice=int(input("enter your choice: "))
#     if choice==1:
#         name=(input("Enter your name:"))
#         age=int(input("Enter your age:"))
#         address=(input("Enter your address:"))
#         username=(input("Enter your username:"))
#         p=(input("Enter your password:"))
#         phno=str(input("Enter your phone number:"))
#     elif choice==2:
#         usrname=(input("Enter the user name:"))
#         p2=(input("Enter the password:"))
#         b=18
#         if usrname==username and p2==p and age>=18 and len(phno)==10:
#             print("Name: ",name)
#             print("Address:",address)
#             print("Age:",age)
#             print("Number:",phno)
#         else:
#             print("Invalid")   
#     elif choice==3:
#         break
#     else:
#         print("Invalid choice")

# a="Hello World"
# print(a[::-1])

# a="Hello World"
# a[1]="y"
# print(a)

               #string functions
# #lower
# message='PYTHON IS FUN'
# print(message.lower())

#Upper
# message=("python is fun")
# print(message.upper())

# #count
# txt="I love apples,apples are my favorite fruit"
# x=txt.count("I")
# print(x)

# #find
# message="Python is a fun programming language"
# print(message.find("fun"))

# #replace
# message="bat ball"
# replacetxt=message.replace("ba","ro")
# print(replacetxt)

#list
#append
# numbers=[21,34,54,12]
# print("Before append",numbers)
# numbers.append(32)
# print("After append",numbers)

# #insert
# vowel=["a","e","i","u"]
# vowel.insert(3,"o")
# print("List:",vowel)

#extend
# primenumbers=[2,3,5]
# print("prime numbers:",primenumbers)
# evennumbers=[4,6,8]
# print("even numbers:",evennumbers)
# primenumbers.extend(evennumbers)
# print("list after appnding:",primenumbers)

# a=[]
# n=int(input("Enter the range:"))
# for i in range(0,n):
#     j=int(input("enter the value:"))
#     a.append(j)
# print("list:",a)

#  #list of even numbers
# a=[]
# n=int(input("Enter the range:"))
# for i in range(0,n):
#     if i%2==0:
#         a.append(i)
# print("list:",a)

# my_list = ['p','r','o','g','r','a','m','i','z']
# print(my_list[2:5])
# print(my_list[5:])
# print(my_list[:])

#Pop()
# prime_numbers = [2, 3, 5, 7]
# removed_element = prime_numbers.pop()
# print('Removed Element:', removed_element)
# print('Updated List:', prime_numbers)

# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(a)):
#     if i<=len(a)-1:
#         if a[i]%2!=0:
#             a.pop(i)
# print("List=",a)

# a=[]
# while True:
#     print("1.Add")
#     print("2.Remove")
#     choice=int(input("Enter your choice:"))
#     if choice==1:
#         n=int(input("Enter a number:"))
#         a.append(n)
#         print(a)
#     elif choice==2:
#         r=int(input("Enter the number:"))
#         for i in range (len(a)):
#             if i<=len(a)-1:
#                 if a[i]==r:
#                     remove=a.pop(i)
#         print(a)

#Del()
# languages=['python','swift','c++','c','java','rust','r']
# del languages[1]
# print(languages)
# del languages[-1]
# print(languages)
# del languages[0:2]
# print(languages)

#Remove()
# languages=['python','swift','c++','c','java','rust','r']
# languages.remove('python')
# print(languages)

#Reversing a list
# prime_numbers=[2,3,5,7]
# prime_numbers.reverse()
# print("Reversed List:",prime_numbers)

#Repetation
# list1=[12,14,16,18,20]
# l=list1*2
# print(l)

# #Concatenation
# list1=[12,14,16,17,18]
# list2=[9,10,32,54,86]
# l=list1+list2
# print(l)

# #length
# list1=[12,14,16,17,18,20,32,4,1,5,39]
# a=len(list1)
# print(a)

# #Iteration
# list1=[12,14,16,17,18]
# for i in list1:
#     print(i)

#membership
# list1=[12,14,16,17,18]
# print(17 in list1)
# print(3 in list1)


# list1=[12,14,16,17,18]
# print(max(list1))
# print(min(list1))

# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]
# # intersection1=set(list1).intersection(list2)
# # print(intersection1)
# intersection2=set(list1) & set(list2)
# print(intersection2)

# a=[1,2,3,4,5,6]
# b=[3,4,5,6,7,8,9]
# n=[]
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             n.append(b[j])
# print(n)

#Maxinum and minimum
# a=[1,2,3,4,5,6]
# greatest=a[0]
# for i in range(len(a)) :
#     if a[i]<greatest:
#          greatest=a[i]
# print(greatest)

#list comprehension
# numbers=[1,2,3,4,5]
# a=[x**2 for x in numbers]
# print(a)

#Matrix
# matrix=[[j for j in range(3)] for i in range(3)]
# print(matrix)

#Tuple
# tuple_data=(0,1,2,3,2,3,1,3,2)
# print(tuple_data)

#Empty Tuple
# my_tuple=()
# print (my_tuple)

#nested tuple
# my_tuple=("mouse",[1,2,3],(8,4,5,6))
# print(my_tuple)

#indexing
# i=('p','q','r','s')
# print(i[3])
# print(i[1])

#negative indexing
# i=('p','q','r','s')
# print(i[-2])
# print(i[-1])

#Repetation
# t=('python','tuples')
# print("Orginal tuple:",t)
# t=t*3
# print("New tuple:",t)

#slicing
# m = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# print(m[1:5])
# print(m[-7])
# print(m[:])

#tuple methods
# t=("a","p","p","l","e")
# print(t.count("p"))
# print(t.index("a"))

# #Iteration
# lang=("python","c++","c")
# for lang in lang :  
#     print(lang)

#Membership
# lang=("python","c++",'c')
# print("c" in lang)
# print("car"in lang)