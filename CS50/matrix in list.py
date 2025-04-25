matrix=[]

for row in range(0,5):
    k=[]
    for col in range(0,5):
        k.append(col)
    matrix.append(k)

print(matrix)

# Alternatively:
# matrix=[[col for col in range(5)] for row in range(5)]
# print(matrix)