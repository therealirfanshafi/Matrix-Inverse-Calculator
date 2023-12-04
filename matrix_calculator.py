# this module has two functions: one to find the determinant of a square matrix and the other to find the inverse
# matrices are represented as 2D arrays/Nested Lists

# function which returns the determinant of a matrix
# uses recursion along with dynamic programming to find the determinant
def determinant(matrix, memo = {}):
    if len(matrix) == 2:  # base case (matrix is a 2 x 2 matrix)
        return matrix[0][0] * matrix [1][1] - matrix[0][1] * matrix[1][0]  # uses the ac - bd formula for the determinant of a 2 x 2 matrix
    
    if str(matrix) in memo:  # returns a the determinant from the memo if it has already been solved (memoisation of recurring/overlapping subproblems)
        return memo[str(matrix)]
    
    result = 0  # variable used for total
    plus = True  # keeps track of whether addition or subtraction is to be performed
    for i in range(len(matrix[0])): # loops over the top row of the matrix
        new_matrix = list()
        for row in matrix[1:]:  # creates a matrix which does not include the row or column of element
            new_matrix.append(row[:i] + row[i+1:])
        memo[str(new_matrix)] = determinant(new_matrix, memo)  # finds the determinant of this matrix using recursion
        if plus:
            result += matrix[0][i] * memo[str(new_matrix)]  # adds/subtracts the product of the element and the determinant to find the determinant of the whole matrix 
        else:
            result -= matrix[0][i] * memo[str(new_matrix)]
        plus = not(plus)  # inverts the sign after each iteration of the loop (sign of top row is + - + - + - and so on)

    return result


# fucntion to find the inverse
def inverse(matrix):
    inverse_matrix = []  
    if len(matrix) == 2:  # if its a 2d matrix, uses the swapping and sign inversion method to find the inverse
        inverse_matrix = [[matrix[1][1], -matrix[0][1]] , [-matrix[1][0], matrix[0][0]]]
    else:

        """
        find inverse by calculating each element of the inverse matrix using determinants from the original matrix
        the element of the inverse in the i'th row and j'th column is equal to the determinant of the matrix formed by removing the j'th row and i'th column from the original matrix, divided by the determinant of the whole matrix
        also takes note of the sign of each element
        e.g [
        [+ - + -]
        [- + - +]
        [+ - + -]
        [- + - +]
        ] for a 4 x 4 matrix, thus mutplies the determinant by said sign
        """

        for i in range(len(matrix)): 
            inverse_matrix.append([])
            if i % 2 == 0:  # determines the sign of the row
                plus = True
            else:
                plus = False
            
            for j in range(len(matrix)):  # performs the above described algorithm
                new_matrix = list()
                for row in (matrix[:j] + matrix[j+1:]):
                    new_matrix.append(row[:i] + row[i+1:])
                if plus:
                    inverse_matrix[-1].append(determinant(new_matrix))
                else:
                    inverse_matrix[-1].append(-determinant(new_matrix))
                plus = not(plus)  # inverts the sign after each element of the row

    det = determinant(matrix)  # calculates the determinant of the whole matrix
    if det == 0:  # raises an error if the determinant is 0 (because singular matrices do not have an inverse)
        raise ValueError
    elif det < 0:  # inverts the sign of each element if the determinant is negative for better presentation in the GUI
        inverse_matrix = list(map(lambda x: list(map(lambda y: -y, x)), inverse_matrix))
    return abs(det), inverse_matrix  # returns the absolute determinant as well as the elements (without division by determinant) of the inverse matrix
