def reverse_element(l):
    l1=l
    l.sort(reverse=True)
    if l1==l:
        print("palindrome")
    else:
        print("not a palindrome")
l=[]
n=int(input("enter n"))
print("enetr elements")
for i in range(0,n):
    x=input()
    l.append(x)
reverse_element(l)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

