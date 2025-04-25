n=int(input())
roll_list=list(map(int,input().split()))

total_sum=(n*(n+1))//2
roll_sum=sum(roll_list)

k=total_sum-roll_sum

roll_list.sort()

if k>len(roll_list):
    selected=-1
else:
    selected=roll_list[-k]

print(k,selected)