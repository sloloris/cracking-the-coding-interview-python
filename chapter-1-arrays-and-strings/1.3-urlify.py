""" 1.3 URLify: Write a method to replace all spaces in a string with '%20'."""

def urlify(strng):
    """ Example input & output

        >>> urlify('Mr John Smith')
        'Mr%20John%20Smith'

        >>> urlify('    ')
        '%20%20%20%20'

        >>> urlify('%20 %20')
        '%20%20%20'
        
    """
    urled = ""
    for char in strng:
        if char == " ":
            urled += "%20"
        else:
            urled += char

    return urled




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "tests pass"