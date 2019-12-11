def last_element(l):
    """
    Returns last element of list l
    """
    return l[-1]
def num_elements(l):
    """
    Returns number of elements in the list l
    """
    return len(l)

def reverse_list(l):
    """
    Returns the reverse of a list l
    """
    return l[::-1]
def is_palindrome(l):
    """
    Returns True if l is a palindrome, False otherwise
    """
    if (l== reverse_list(l)):
        return True
    else:
        return False
def compress(l):
    """
    Returns a list with consecutive duplicate elements replaced by a single element
    """
    new=[]
    new+=[l[0]]
    for i in l:
        if(new [-1] != i):
            new+=[i]
    return new
def pack(li):
    """
    Returns a list with consecutive duplicate elements packed into sublists
    """
    finallist=[]
    templist=[li[0]]
    for i in li[1:]:
        if i == templist[-1]:
            templist+=[i]
        else:
            finallist+=[templist]
            templist=[i]
    if(len(templist)!=0):
        finallist+=[templist]
    print(finallist)
    return finallist
def slice(l,i,k):
 if i>=0 and k>len(l):
  return l[i:len(l)]
 else:
  return l[i:k]
def insert_element(l, i, elem):
    """
    Returns a new list containing elem at index i. If i > len (l), insert element at the end of the list
    """      
    
    li=[]
    for element in l:
      if(i<0):
        li=l
        break
      if(i>=len(l)):
        li=l+[elem]
        break
      if(i<len(l)):
        li[i:]=[elem]+l[i:]
    return li
        



