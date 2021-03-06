""" 1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring. """


def is_rotation(s1, s2):
    """ Example inputs

        >>> is_rotation("waterbottle", "erbottlewat")
        True
    """
    if len(s1) != len(s2) or len(s1) == 0:
        return False

    superstring = s1 + s1
    return isSubstring(superstring, s2)


# theoretically this should work, hard to test though


    
            



