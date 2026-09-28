from client import QRDecomposition

def main():
    A = [[12.0, -51.0], [6.0, 167.0], [-4.0, 24.0]]
    Q, R = QRDecomposition.decompose(A)
    print("Orthogonal Q matrix rows:", len(Q))
    print("Upper-triangular R diagonal:", [round(R[i][i], 2) for i in range(2)])

if __name__ == "__main__":
    main()
