# # USING CSV WRITER

# import csv
# name=input("What's your Name? ")
# home=input("Where's your Home? ")
# with open("home.csv", "a", newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow([name, home])

# USING CSV DICTWRITER

import csv
headers=["name","home"]
name=input("What's your Name? ")
home=input("Where's your Home? ")
with open("home.csv", "a", newline="") as file:
    writer=csv.DictWriter(file, fieldnames=headers)
    writer.writerow({"home":home,
                     "name":name})
    