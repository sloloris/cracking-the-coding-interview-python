""" 1.6 String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string 'aabcccccaaa' would become 'a2b1c5a3'. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z). """

def compress(strng):
    compressed = ""
    curr_char = strng[0]
    curr_count = 1
    for i in xrange(1, len(strng)):
        if strng[i] == curr_char:
            curr_count += 1
        else:
            compressed += curr_char
            compressed += str(curr_count)
            curr_char = strng[i]
            curr_count = 1
    compressed += curr_char 
    compressed += str(curr_count)
    return compressed

# runtime is O(n) where n is the length of the string
# make sure to clarify whether capital and lowercase letters count as the same or different (if same, add .lower() or .upper() method where necessary)


if __name__ == "__main__":
    print "TEST compress('aabcccccaaa') -> 'a2b1c5a3'"
    print compress('aabcccccaaa')