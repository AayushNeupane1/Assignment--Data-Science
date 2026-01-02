# remove duplicate of list using set

list1= [1,2,3,4,4,5,6,7,7,8,9,9,1,2,3,4]

print("Original List:", list1)

list2= list(set(list1))
print("List after removing duplicates:", list2)