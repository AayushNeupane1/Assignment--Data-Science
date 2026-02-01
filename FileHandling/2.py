try:
    with open('qst2.txt','r') as file:
        contents = file.read()
        words=contents.split()
        print("Number of words in the file:", len(words))

        #reading total lines in file 
        file.seek(0)  #seek moves the cursor of the file to the top 
        lines = file.readlines()
        print("Number of lines in the file:", len(lines))
except FileNotFoundError:
    print("The file was not found.")