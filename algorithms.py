
# question 2: two examples

# INPUT MUST BE ALL LOWERCASE - use .lower() if user insists on
# using non-lowercase letters

def is_palindrome(string):
    if string != string[::-1]:
        return False
    return True

# The time complexity is O(n) where n is the string length,
# the space complexity is O(n) as the reversed string takes additional space of O(n)
# due to a new string being created in memory


def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] != string[-1]:
            return False
        return is_palindrome(string[1:-1])

# The time complexity is O(n) as each recursion will compare the first and last elements
# to see if they are equal, but each call will create a substring,
# which gives the effect of processing each chatacter once
# The space complexity is O(n), a smaller substring is processed by each
# recursive call. The depth of recursion, in this case, is proportional
# to n (the length of the string), hence O(n)


# question 3

def missing_num(list_):
    if any(isinstance(elem, str) for elem in list_):
        raise Exception("Ivalid input, non-numeric value detected")
    if any(elem < 0 for elem in list_):
        raise Exception("Invalid input, negative number detected")
    for num in range(1, len(list_)+1):
        if num not in list_:
            return f"Missing = {num}"
    return "Nothing is missing"


# time complexity O(n) in the worst case scenario if each number has to
# be processed to see if a number is missing
# space complexity O(n) as the size of the list is proprtional to the space
# occupied.

# I think for this implementation, there may be a better way to raise the
# exceptions. for the question it was required to raise individual
# exceptions. but that means that we have to do any() twice
# when an exception would be raised either way if the element is
# negative and/or a string.
