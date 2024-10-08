import numpy as np

def rref(matrix):
    # Convert to float for division operations
    A = np.array(matrix, dtype=float)
    m, n = A.shape
    
    lead = 0
    for r in range(m):
        if lead >= n:
            return A
        i = r
        while A[i, lead] == 0:
            i += 1
            if i == m:
                i = r
                lead += 1
                if n == lead:
                    return A
        A[i], A[r] = A[r], A[i]
        lv = A[r, lead]
        A[r] = A[r] / lv
        for i in range(m):
            if i != r:
                lv = A[i, lead]
                A[i] = A[i] - lv * A[r]
        lead += 1
    return A

def test_rref():
    # Test case 1
    matrix = np.array([
        [1, 2, -1, -4],
        [2, 3, -1, -11],
        [-2, 0, -3, 22]
    ])
    expected_output = np.array([
        [ 1.,  0.,  0., -8.],
        [ 0.,  1.,  0.,  1.],
        [-0., -0.,  1., -2.]
    ])
    assert np.allclose(rref(matrix), expected_output), "Test case 1 failed"
    
    # Test case 2
    matrix = np.array([
        [2, 4, -2],
        [4, 9, -3],
        [-2, -3, 7]
    ])
    expected_output = np.array([
        [ 1.,  0.,  0.],
        [ 0.,  1.,  0.],
        [ 0.,  0.,  1.]
    ])
    assert np.allclose(rref(matrix), expected_output), "Test case 2 failed"

if __name__ == "__main__":
    test_rref()
    print("All rref tests passed.")
