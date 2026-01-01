#find the grade and print whole the result of a students

def grade(avg):
    if avg >=90:
        return "A+"
    elif avg >=80:
        return "A"
    elif avg >=70:
        return "B"
    elif avg >=60:
        return "C"
    elif avg >=50:
        return "D"
    else:
        return "F"

names=[]
all_marks=[]

n=int(input("Enter the number of students"))
for i in range(n):
    name=input(f"Enter name of student {i+1}:")
    marks = list(map(int,input("Enter marks separated by space:").split()))

    names.append(name)
    all_marks.append(marks)

print("\nRESULTS")

for i in range(n):
    total=sum(all_marks[i])
    avg=total/len(all_marks[i])
    grade=grade(avg)

    print(f"\nStudent:{names[i]}")
    print(f"Marks:{all_marks[i]}")
    print(f"Total:{total}")
    print(f"Average:{avg:.2f}")
    print(f"Grade:{grade}")
