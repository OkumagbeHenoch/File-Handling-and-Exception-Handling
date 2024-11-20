file = open("hello.txt", "w")
name = input("What is your name ?") 

print(f"Welcome {name}")


try:
    with open("hello.txt", "w") as file:
        data = file.write(f"Welcome {name}")
except :
    print ("Empty")
