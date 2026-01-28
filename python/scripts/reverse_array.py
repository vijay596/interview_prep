#Reverse an array

# Method 1

def reverse_array(my_array):
    return my_array[::-1]
    
my_array = [1,2,3,4,5]
result = reverse_array(my_array)
print(result)

# Method 2

my_array = [1,2,3,4,5]
my_array.reverse()
print(my_array)

# Method 3

arr = [1, 2, 3, 4, 5]
reverse_arr = list(reversed(arr))
print(reverse_arr)

