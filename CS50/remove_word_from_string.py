def main():
    string=input("Enter a string: ")
    word=input("What word do you want to remove from string: ")
    print(f"{strfun(string,word)}")

def strfun(string,word):
    new=string.replace(word,"")
    return new.strip()

main()