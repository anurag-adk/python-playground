names=[]
with open("names.txt") as file:
    for li in file:
        names.append(li.rstrip())
for name in sorted(names):
    print(f"Hello, {name}")