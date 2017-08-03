""" 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. """

def is_palindrome_permutation(strng):
    """ Example input and output (for palindrome "taco cat")

        >>> is_palindrome_permutation("Tact Coa")
        True

        >>> is_palindrome_permutation("ababada")
        True

        >>> is_palindrome_permutation("  tac ocats")
        False

    """
    strng_dict = {}
    for char in strng:
        if char != " ":
            if char.lower() in strng_dict:
                strng_dict[char.lower()] += 1
            else:
                strng_dict[char.lower()] = 1    

    odd_count = 0
    for char in strng_dict:
        if strng_dict[char.lower()] % 2 != 0:
            if odd_count >= 1:
                return False
            odd_count += 1

    return True

# runtime is O(n) where n = # of characters in the string


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "tests pass"

