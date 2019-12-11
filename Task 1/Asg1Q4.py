def is_palindrome(l):
    """
    Returns True if l is a palindrome, False otherwise
    """
    n = 0;
    for x in l:
    	n = n+1
    f = True
    for i in range(n):
    	if l[i] != l[n-1-i]:
    		f = False
    		break
    return f

"""Testing code for is_palindrome"""

assert(is_palindrome([1, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 4])) == False