def last_element(lst):
    print ("The last element is : " +  str(lst[-1])) 

lst=[]
n = int(input("Enter number of elements : "))
print('Enter the elements')
for i in range(0, n):
    ele = (input())
    lst.append(ele)

last_element(lst)

assert last_element([1]) == 1
assert last_element(["Hello", "World"]) == "World"