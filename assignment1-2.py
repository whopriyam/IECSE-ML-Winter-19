def num_elements(finallist):
    num = len(finallist) 
    print("The number of elements are"  + str(num))

inputlist = input("Enter a list seperated by space")
finallist = inputlist.split()

num_elements(finallist)

assert num_elements([2, 3, 4])==3
