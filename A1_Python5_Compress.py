def compress(l):
   i=0
   while (i<len(l)-1):
       if(l[i]==l[i+1]):
           del l[i]
       else:
           i+=1
l=[]
n=int(input("enter n"))
print("enter elements")
for i in range(0,n):
    x=input()
    l.append(x)
compress(l)  
print(l)     
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:27:17 2019

@author: vatsa
"""
