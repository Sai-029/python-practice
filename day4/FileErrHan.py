try:
    with open("s.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found..")
