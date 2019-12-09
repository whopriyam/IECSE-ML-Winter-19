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

