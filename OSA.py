def OSA(A: str, B: str) -> int:
    m, n = len(A), len(B)
    
    D = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1): D[i][0] = i  
    for j in range(n + 1): D[0][j] = j  

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if A[i - 1] == B[j - 1] else 1  # Match or substitution
            
            D[i][j] = min(
                D[i - 1][j] + 1,        # Deletion
                D[i][j - 1] + 1,        # Insertion
                D[i - 1][j - 1] + cost  # Match or substitution
            )

            # Transposition
            if i > 1 and j > 1 and A[i - 1] == B[j - 2] and A[i - 2] == B[j - 1]:
                D[i][j] = min(D[i][j], D[i - 2][j - 2] + 1)

    return D[m][n] 

# source = "butterfly"
# target = "dragonfly"

# distance = OSA(source, target)
# print(distance)

source = "caper" 
target = "acer" 
output = OSA(source, target) 
print(output)