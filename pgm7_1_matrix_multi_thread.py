import threading

def matrix_multiply_element(row, col, A, B, result):
    # Calculate the element at position (row, col) in the result matrix
    value = sum(A[row][k] * B[k][col] for k in range(len(A[0])))
    result[row][col] = value

def multiply_matrices(A, B):
    # Get the dimensions of the matrices
    m, n = len(A), len(A[0])
    p, l = len(B), len(B[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(l)] for _ in range(m)]

    # Create threads for matrix multiplication
    threads = []
    for i in range(m):
        for j in range(l):
            thread = threading.Thread(target=matrix_multiply_element, args=(i, j, A, B, result))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return result

def main():
    # Example matrices A and B
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    B = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]

    # Get the dimensions of matrices A and B
    m, n = len(A), len(A[0])
    p, l = len(B), len(B[0])

    if n != p:
        print("Matrix multiplication not possible. Number of columns in A must be equal to the number of rows in B.")
        return

    # Multiply matrices using multiple threads
    result = multiply_matrices(A, B)

    # Display the result matrix
    print("Result Matrix:")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()

