name=input("What's your Name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")