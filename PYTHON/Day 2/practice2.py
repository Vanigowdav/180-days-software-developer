#Grading marks
name = input("enter your name: ")
marks = int(input("Enter your marks: "))
if 90 <= marks <= 100:
    print(name,"you have scored A grade")
elif 80 <= marks < 90:
    print(name,"you have scored B grade")
elif 70 <= marks < 80:
    print(name,"you have scored C grade")
elif 60 <= marks < 70:
    print(name,"you have scored D grade")
elif 50 <= marks < 60:
    print(name,"you have scored E grade")
else:
    print(name, "you are fail")