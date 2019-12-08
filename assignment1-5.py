def compress(l):
    c=0
    for i in range(0, n-1):
        for k in range(i+1,n-1):
            if(l[i]==l[k]):
                c=c+1
                l[k]=l[k+1]

    for i in range (0,n-c+1):            
        print(l[i])            


l=[]
n = int(input("Enter number of elements : "))
print('Enter the elements')
for i in range(0, n):
    ele = (input())
    l.append(ele)

compress(l)    

assert(compress([1, 2, 2])) == [1, 2]
assert(compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x'])) == [1, 2, 1, 3, 'x']