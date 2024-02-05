"""
Each element is checked in sequence until you find
what you're looking for or the list ends.
If the current element equals what
we're looking for (X), return its position.

"""

# Linear search algorithm
def linear_search(array, element):
  for i in range(len(array)):
    if array[i] == element:
      return i
  return -1

# this function to find the element
def find_element(array, element):
  position = linear_search(array, element)
  if position != -1:
    print(f"{element} found at position {position}")
  else:
    print(f"No results")

# this function to do the search
def print_list(array, element_to_find):
  print(f"List = {array}")
  print(f"Searching for : {element_to_find}")
  find_element(array, element_to_find)
  print("")


"""
Here I will a list where to find
a member element passed as argument

"""

list = [121, 12, 1, 0, 457, 5, 65, 69, 32]
list2 = ["list", "of", "strings", "here"]
print_list(list, 0)
print_list(list2, "test")
print_list(list, 32)
