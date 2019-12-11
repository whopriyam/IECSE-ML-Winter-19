def insert_ele(l,pos,ele):
    l.insert(pos,ele)
    print(l)
l=[]
n=int(input("enter n"))
print("enetr elements")
for i in range(0,n):
    x=input()
    l.append(x)
print("enter pos and element to insert")
pos=int(input())
ele=int(input())
insert_ele(l,pos,ele)
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:09:14 2019

@author: vatsa
"""

