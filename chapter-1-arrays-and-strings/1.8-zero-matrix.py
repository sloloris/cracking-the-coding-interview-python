""" 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0. """

def zero_matrix(matrix):
    """ Example input and output

        >>> zero_matrix([['x', 'x', 0, 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x']])
        [[0, 0, 0, 0], ['x', 'x', 0, 'x'], ['x', 'x', 0, 'x']]

        >>> zero_matrix([])
        []
    """
    if len(matrix) > 0:
        for lst_i in xrange(len(matrix)):
            if len(matrix[lst_i]) > 0:
                for i in xrange(len(matrix[lst_i])):
                    if matrix[lst_i][i] == 0:
                        zero_index = i
                        lst_index = lst_i
                        break
            break

        for lst in matrix:
            lst[zero_index] = 0
        for item in xrange(len(matrix[lst_index])):
            matrix[lst_index][item] = 0
    return matrix




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "tests pass"