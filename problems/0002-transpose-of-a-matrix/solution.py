def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    
    m = len(a)

    if m == 0:
        return []

    rs = []
    
    if isinstance(a[0], int):
        for i in range(m):
            rs.append([a[i]])
        return rs
    elif len(a[0]) == 1:
        for i in range(m):
            rs.append(a[i][0])
        return rs 
    
    n = len(a[0])

    for j in range(n):
        row = []
        for i in range(m):
            row.append(a[i][j])
        rs.append(row)
    
    return rs