#  1.LIST
fruits = ["Apple", "Banana"]

fruits.append("Orange")     
fruits.insert(1, "Grapes")   
fruits.remove("Banana")      
fruits.sort()                

print(fruits)



# 2.TUPLE
colors = ("Red", "Green", "Blue")

print(colors)
print(colors[1])


# 3.SET
numbers = {1, 2, 3}

numbers.add(4)
numbers.remove(2)

print(numbers)


# 4.DICTIONARY
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

print(student["name"])


# 5.STRING
text = "hello world"

print(text.upper())
print(text.lower())
print(text.replace("world", "Python"))
print(text.split())