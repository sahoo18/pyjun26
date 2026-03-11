#// def runLoopFrom(x,y):
#  //   for i in range(x,y):
#    //     print(i)


# //def studentDetails():
# //    name = input("Enter your name:")
# //    age = input("Enter your age:")
# //    per = int(input("Enter your percentage:"))
# //    reg = input("Enter Registration number : ")

#//     print (name, age, per, reg)

#// studentDetails()    




#// fruit = "Apple"

#// def printFruit():

#//     student_1 = "Rahul"

#//     print(fruit,student_1)

#// print(fruit)   




def get_traffic_action(color):
    color = color.strip().lower()
    
    if color == "red":
        return "Stop"
    elif color == "orange":
        return "Start"
    elif color == "green":
        return "Go"
    else:
        return "invalid color"
   

