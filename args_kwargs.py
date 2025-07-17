# **args
# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     print("Sum:", total)

# add_numbers(2, 4,7,8)
# add_numbers(1, 2, 3, 4, 5)

# def iseven(*num):
#         for i in num:
#             if i%2==0:
#                 print(i, "is even")
#             else:
#                 print(i, "is odd")
# iseven(12,3,34,56)

#Kwargs
# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_details(name="Bob", age=21,place="Kochi")
# print_details(course="Python", level="Beginner")

#using args and kwargs in asame function
# def student_info(subject, *args, **kwargs):
#     print("Subject:", subject)
#     print("Other Grades:", args)
#     print("Details:", kwargs)
# student_info("Math", 90, 85, 92,57, name="Bob", class_="12th",rollno="18")

def show_info(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

show_info(10, 20, name="Athena", city="Delhi")