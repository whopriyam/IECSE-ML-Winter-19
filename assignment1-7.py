def slice(l, i, k):
    sliced_list	= l[i:k]
    print(sliced_list)


l=[]
n = int(input("Enter number of elements : "))
print('Enter the elements')
for i in range(0, n):
    ele = (input())
    l.append(ele)
i = int(input("Enter the first limit : ")) 
k = int(input("Enter the second limit : "))    

slice(l, i, k)

assert(slice([1, 3, 8, 9, 7], 1, 3)) == [3,8]
assert(slice([1, 4, 6, 'x', 9, 0], 2, 10)) == [6, 'x', 9, 0]
