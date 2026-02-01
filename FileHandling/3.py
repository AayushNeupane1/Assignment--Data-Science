# Take a user's name and age and save it to a text file using write or append mode 

try:
    name=input("Enter the name: ")
    age=int(input("enter the age:"))

    with open("qst3.txt","a") as file:
        file.write(f"Name: {name}, Age: {age}\n")

except Exception as e:
    print(f"An error occurred: {e}")