def insert_element(l, i, elem):
    l.insert(i,elem)
    print(l)


l=[]
n = int(input("Enter number of elements : "))
print('Enter the elements')
for i in range(0, n):
    ele = (input())
    l.append(ele)
elem = str(input("Enter the element to be inserted : ")) 
i = int(input("Enter the index at which it should be inserted : "))   

insert_element(l, i, elem)

assert(insert_element([1, 2, 3, 4,], 2, 5)[2]) == 5
assert(insert_element([1, 5, ], 3, 5)) == [1, 5, 5]