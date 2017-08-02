""" 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? """

# permitting additional data structures
def is_unique(strng):
    char_count = {}
    for char in strng:
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
    for char in char_count:
        if char_count[char] > 1:
            return False
    return True


# not permitting additional data structures
def is_unique2(strng):
    for i in xrange(len(strng)):
        for j in xrange(len(strng)):
            if strng[i] == strng[j] and i != j:
                return False
    return True



# Note: If you can assume the string contains only lowercase letters, you can add an additional if statement at the beginning to cut down on runtime:
# if len(strng) > 26:
#     return False
# If you can assume they are all upper- or lowercase, then 52.

if __name__ == "__main__":
    print "TEST: is_unique('hello') -> False"
    print is_unique('hello')
    print "TEST: is_unique('hullaballoo') -> False"
    print is_unique('hullaballoo')
    print "TEST: is_unique('abcdefg') -> True"
    print is_unique('abcdefg')
    print "TEST: is_unique('') --> True"
    print is_unique('')

    print "TEST: is_unique2('hello') -> False"
    print is_unique2('hello')
    print "TEST: is_unique2('hullaballoo') -> False"
    print is_unique2('hullaballoo')
    print "TEST: is_unique2('abcdefg') -> True"
    print is_unique2('abcdefg')
    print "TEST: is_unique2('') --> True"
    print is_unique2('')





