#4)   A programme to input percentage marks of a student and find the grade as per:
#                 Marks                      Grade
#                  >=90                       A
#                  75-89                      B
#                  60-75                      C
#                   <60                       D

print("This program will asign you ur grade")
print()
sci = int(input("Enter your science marks (out of 100): "))
math = int(input("Enter your maths marks (out of 100): "))
sst = int(input("Enter your SST marks (out of 100): "))

total = sci + math + sst
percentage = (total/300) * 100

if percentage >=90:
    print("Your grade: A")
    print("Your percentage:", percentage,"%")
elif percentage >= 75 and percentage <=89:
    print("Your grade: B")
    print("Your percentage:", percentage,"%")
elif percentage >= 60 and percentage <=75:
    print("Your grade: C")
    print("Your percentage:", percentage,"%")
elif percentage < 60:
    print("Your grade: D")
    print("Your percentage:", percentage,"%")
else:
    print("invalid marks entered ")