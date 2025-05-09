# # USING CSV READER

# import csv
# students=[]
# with open("home.csv") as file:
#     reader=csv.reader(file)
#     for row in reader:
#         students.append({"name":row[0], "home":row[1]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# USING CSV DICTREADER

import csv
students=[]
with open("home.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"],
                         "home": row["home"]})
        
for student in sorted(students, key=lambda student: student["name"], reverse=False):
    print(f"{student['name']} is from {student['home']}")