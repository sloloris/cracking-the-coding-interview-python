""" 1.5 One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. """


def one_edit_away(s1, s2):
    """ Example inputs and outputs

        >>> one_edit_away("pale", "ple")
        True

        >>> one_edit_away("pales", "pale")
        True

        >>> one_edit_away("pale", "bale")
        True

        >>> one_edit_away("pale", "bake")
        False

    """
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) >= len(s2):
        longer = s1
        shorter = s2
    else:
        longer = s2
        shorter = s1
    edit = False
    l = s = 0
    while l < len(longer) and s < len(shorter):
        if longer[l] != shorter[s]:
            if edit:
                return False
            edit = True
            if len(longer) == len(shorter):
                s += 1
                l += 1
            else:
                l += 1
        else:
            s += 1
            l += 1
    return True




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "tests pass"


