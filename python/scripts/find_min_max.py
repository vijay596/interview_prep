#Find max & min in a list without built-in functions

def find_min_max(my_list):
    # Validate that input is a list
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list, got {}".format(type(my_list).__name__))
    
    if len(my_list) == 0:
        raise ValueError("Cann't find min/max of an empty list.")
        
    max_val = my_list[0]
    min_val = my_list[0]
    for val in my_list:
        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val
    return max_val, min_val

lst = [1,2,5,3,6,9]
max_val, min_val = find_min_max(lst)
print(max_val)
print(min_val)
