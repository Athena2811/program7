# a=15
# b=5
# if a>b:
#     print("a is greater")

# a=2
# if a==4:
#     print("both are equal")
# print("Invalid")


# i=20
# if i<15:
#     print("i is smaller than 15")
#     print("i'm in if block")
# else :
#     print("i is greater than 15")
#     print("i'm in else block")   
# print("i'm not in if and else block")

# i=10
# if i==10:
#     if i<15:
#         print("i is smaller than 15")
#     if i<12:
#         print("i is samller than 12 too")
#     else:
#         print("i is greater than 15")


# i=20
# if i==10:
#     print("i is 10")
# elif i==15:
#     print("i is 15")
# elif i==20:
#     print("i is 20")
# else:
#     print("i is not present")

# i=81
# if i<=100 and i>=0:
#     if i>=90:
#         print("Grade A")
#     elif i>=80:
#         print("Grade B")
#     elif i>=70:
#         print("Grade C")
#     else:
#         print("fail")
# else:
#     print("Invalid number")

# #Positive Number
# a=-10
# if a>=0:
#     print("a is positive")
# else:
#     print("a is negative")

# #Divisible by 5
# a=10
# if a%5==0:
#     print("number is divisible by 5")
# else:
#     print("number is not divisible by 5")

# #check a string
# a="python"
# if a=="python":
#     print("the entered string is correct")
# else:
#     print("it is invalid")

# #Odd number
# a=6
# if a%2==0:
#     print("Even number")
# else:
#     print("Odd number")

# #Age
# a=16
# if a>=18:
#     print("Eligible")
# else:
#     print("Not eligible")

# #Greatest of 2 numbers
# a=15
# b=5
# if a>b:
#     print("a is greater")

#     a=int(input("Enter the  unit "))
# if a<=100:
#     cal=a*5
#     print(cal)
# elif a<=200:
#     cal=(100*5)+(a-100)*8
#     print(cal)
# else:
#     cal=(100*5)+(100*8)+(a-200)*10
#     print(cal)
n = 7
for i in range(0,3):
    m= int(input("Guess the secret number (1-10): "))
    if m == n:
        print(" Congratulations! You guessed it right.")
    else:
        print("Oops! That's not it.")

if i!=0:
    print("Sorry, you've used all your attempts. Better luck next time!")
# password=(input("Enter the passwoed:"))
# while password != "python123": 
#     password = input("Enter password: ") 
# else: 
#     print("Correct password")
numbers=[1,2,3,4,5,6]
target =int(input("Enter the number to be found:"))
for num in numbers: 
    if num == target: 
        print("Number is found at",num ,"th position")
    else: 
        print("Number not found")