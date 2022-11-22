list=[1,2,3,4,5,6,7,8,9,10]
print("Original List:")
print(list)
for i in list:
    if i%2==0:
        list.remove(i)
print("List after removing even numbers from it:")
print(list)

