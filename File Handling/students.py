# with open('names.csv') as file:
#     for line in file:
#         row=line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}.")


#FOR A SORTED LIST
students=[]
with open("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
        dic={"name":name,"house":house}
        students.append(dic)

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")
