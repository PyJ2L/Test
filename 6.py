import random

##allData = "Name1234@gmail.com,1234567890"
Student = "Name1234@gmail.com,1234567890"
Name = Student.split("@")[0]
print(Name)
PhoneNO = Student.split(",")
print(PhoneNO[1])

