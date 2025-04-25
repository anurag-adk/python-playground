#greatest among 4 numbers
num=[]
for i in range(4):
    n=int(input("Enter a number: "))
    num.append(n)

# Method no. 1
print(f"The greatest number among {num} is {max(num)}")

# # Method no. 2
# num.sort()
# print(f"The greatest number in {num} is {num[3]}")

# # Method no. 3
# if(num[0]>num[1]):
#     first=num[0]
# else:
#     first=num[1]

# if(num[2]>num[3]):
#     sec=num[2]
# else:
#     sec=num[3]

# if(first>sec):
#     print(f"The greatest number among {num} is {first}")
# else:
#     print(f"The greatest number among {num} is {sec}")
