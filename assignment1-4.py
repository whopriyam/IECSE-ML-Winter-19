def is_palindrome(l):
    rev=[]
    rev= l[::-1]
    if (rev == l):
        print('True')
    else:
        print('False')

l=[]
n = int(input("Enter number of elements : "))
print('Enter the elements')
for i in range(0, n):
    ele = (input())
    l.append(ele)    

is_palindrome(l)

assert(is_palindrome([1, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 4])) == False
