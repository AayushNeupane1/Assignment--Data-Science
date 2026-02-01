#wite a program to opem a text file and print all its contents, handle file not found error

try:
    with open('qst1.txt', 'r') as file:
        contents = file.read()
        print(contents)
    
except FileNotFoundError:
    print("The file was not found.")