def num_elements(l):
    """
    Returns number of elements in the list l
    """
    n = 0
    for x in l:
    	n = n + 1   

    return n

"""Testing code for num_elements"""
assert num_elements([2, 3, 4]) == 3