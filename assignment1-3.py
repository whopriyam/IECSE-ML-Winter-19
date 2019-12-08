def reverse_list(lst):
	print(lst[::-1])

lst=[]
n = int(input("Enter number of elements : "))
n1=float(n)
print('Enter the elements')
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

reverse_list(lst)

assert reverse_list([2, 3, 4])== [4, 3, 2]