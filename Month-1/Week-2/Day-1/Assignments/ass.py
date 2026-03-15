# Make an object class



# class car:
#     cat="SUV"
#     color="red"
#     wheel=4

# car1 =()
# car2 =()
# car3 =()
# car4 =()

# print(car1.cat)
# print(car1.color)




# METHODs

# class Student():
#     name="Rahul"
#     age=14
#     def studentDetails(self):
#         print("Student name is",self.name,"Age is",self.age)
#     def viewInput(self,address,roll):
#         print("This is the address",address,"This is the roll",roll)    

# s1=Student()  
# s1.studentDetails() 
# s1.viewInput("Bhubaneswar",40)  
# print(s1.age)  



# CONSTRUCTOR

# class Citizen:
#     Country = "India"
#     def __init__(self,aadhar,phone,name):
#         self.aadhar = aadhar
#         self.phone=phone
#         self.name = name

#     def printCitizen(self):
#         print("Aadhar-" , self.aadhar)
#         print("phone-" , self.phone) 
#         print("name-" , self.name)  
#         print("Country-" , self.Country)

# c1 = Citizen("1325472434", "85645587558","RAhul") 
# c2 = Citizen("8767465235", "78456568656", "Prabha")   
# c3 = Citizen("5464756755", "74655768487", "Names")     

# c2.printCitizen()


class Building:
    country = "India"

    def __init__(self):
        self.location = input("Enter your location :")
        self.pin = input("Enter pincode :")
        self.floor = input ("Enter floor count :")
        self.roomInFloor = input("Enter room in each floor :")


        print("country -",self.country)
        print("location -",self.location)
        print("pin -",self.pin)
        print("floor-",self.floor)
        print("Rooms in Floor -",self.roomInFloor)

    def DisplayBuild(self):
        print("The building has ", self.floor, "floor")   


 
building1 = Building()        
building1.DisplayBuild()         