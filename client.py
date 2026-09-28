"""QR Decomposition via Gram-Schmidt Orthogonalization.
100% Python Standard Library.
"""

import math

class QRDecomposition:
    """QR factorization decomposing matrix A into orthogonal Q and upper-triangular R."""

    @staticmethod
    def decompose(A: list) -> tuple:
        m = len(A)
        n = len(A[0])
        cols = [[A[r][c] for r in range(m)] for c in range(n)]
        q_cols = []
        R = [[0.0] * n for _ in range(n)]

        for j in range(n):
            v = cols[j][:]
            for i in range(j):
                q = q_cols[i]
                dot = sum(v[k] * q[k] for k in range(m))
                R[i][j] = dot
                for k in range(m):
                    v[k] -= dot * q[k]
            norm = math.sqrt(sum(x * x for x in v))
            R[j][j] = norm
            q_cols.append([x / norm for x in v])

        Q = [[q_cols[c][r] for c in range(n)] for r in range(m)]
        return Q, R
