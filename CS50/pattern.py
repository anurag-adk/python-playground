"""
QN.1 Print This Pattern:
             *
           * * *
         * * * * * 
"""
# row = int(input("Enter number of row you want to see: "))
# for i in range(1, row + 1):
#     for space in range(row + 1 - i):
#         print(" " * 2, end="")
#     print("* " * (2 * i - 1))


"""
QN.2 Print This Pattern:
          *  *  * 
          *     *
          *  *  * 
"""
row = int(input("Enter odd number of rows: ")) 
for i in range(row + 1):
    for j in range(row + 1):
        if i == 0 or j == 0 or i == row or j == row:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
