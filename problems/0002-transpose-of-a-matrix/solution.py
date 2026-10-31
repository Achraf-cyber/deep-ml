def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    n = len(a)
    m = len(a[0])
    b = [ [ 0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    return b