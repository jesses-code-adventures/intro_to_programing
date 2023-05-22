"""
    Arrays are collections of multiple values.
    In more rigid programming languages, you often need to know what types of values you'll store.
    You would also often need to know the capacity that the array can hold when you make it.

    Python has neither of these things, and as a result doesn't really have "true" arrays.
    Instead we have lists, and lists can be of any length and can have varying types of data.
    However, you generally want to try to make your lists have only one type of values.
"""

### EXAMPLE
## Basic list
list_of_ints = [1, 2, 6, 7]
list_of_strings = ["hello", "these", "are", "strings"]

"""
    Moving through each value in a list is called iterating.
    The easiest way to iterate through a list is by using a for loop.
"""

### EXAMPLE
## Prints each value to its own line
## I use enumerate on the list and add the 'i' in the for loop to make the printing nicer.
## You can ignore it for now, or you can google it to see how it works if you're keen.
print("FOR LOOP OUTPUT")
for i, value in enumerate(list_of_strings):
    print(f"---> list item {i}: {value}")

"""
    You can also run certain operations on lists.
    For example, we can call sum() on list_of_ints to get the sum of the numbers.
"""

### EXAMPLE
total: int = sum(list_of_ints)
print("\nSUM OUTPUT")
print(f"---> Sum of list of ints: {total}\n")

"""
    Lists also have methods.
    For example, we can add an element to a list using .append()
    See the different list methods: https://www.w3schools.com/python/python_ref_list.asp
"""

print("\nAPPEND OUTPUT")
list_of_strings.append("Newly appended string")
for i, value in enumerate(list_of_strings):
    print(f"---> list item {i}: {value}")
