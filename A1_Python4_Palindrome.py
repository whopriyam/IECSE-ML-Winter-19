def is_palindrome(l):
    f=0
    i=0
    while(i<=n//2 and n!=0):
        if(l[i]!=l[n-i-1]):
            f=1
            break
        else:
            i+=1
    if(f==1):
        print("not palindrome")
    else:
        print("palinfrome")
l=[]
n=int(input("enter n"))
print("enetr elements")
for i in range(0,n):
    x=input()
    l.append(x)
is_palindrome(l)    
    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

