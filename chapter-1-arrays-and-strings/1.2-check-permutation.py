""" 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other. """

def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    perm_dict = {}

    for char in s1:
        if char in perm_dict:
            perm_dict[char] += 1
        else:
            perm_dict[char] = 1

    for char in s2:
        if char in perm_dict:
            if perm_dict[char] <= 0:
                return False
            else:
                perm_dict[char] -= 1

    for char in perm_dict:
        if perm_dict[char] != 0:
            return False

    return True

# runtime is O(n), where n is the length of one of the strings

def check_permutation2(s1, s2):
    s1_lst = []
    s2_lst = []

    for char in s1:
        s1_lst.append(char)
    for char in s2:
        s2_lst.append(char)

    if sorted(s1_lst) == sorted(s2_lst):
        return True
    else:
        return False

# runtime is likely O(nlogn) (runtime of most sorting algorithms) as the lengths of the strings grow


if __name__ == "__main__":
    print "TEST: check_permutation('alba', 'blaa') -> True"
    print check_permutation('alba', 'blaa')
    print "TEST: check_permutation('alba', 'blaaa') -> False"
    print check_permutation('alba', 'blaaa')
    print "TEST: check_permutation('alba', 'blee') -> False"
    print check_permutation('alba', 'blee')
    print "TEST: check_permutation('alba', 'bl') -> False"
    print check_permutation('alba', 'bl')

    print "TEST: check_permutation2('alba', 'blaa') -> True"
    print check_permutation2('alba', 'blaa')
    print "TEST: check_permutation2('alba', 'blaaa') -> False"
    print check_permutation2('alba', 'blaaa')
    print "TEST: check_permutation2('alba', 'blee') -> False"
    print check_permutation2('alba', 'blee')
    print "TEST: check_permutation2('alba', 'bl') -> False"
    print check_permutation2('alba', 'bl')