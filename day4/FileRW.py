with open ("s.txt","r") as f:
    data = f.read()
    print(data)

with open ("s.txt","a") as f:
    f.write("\nnew line added.")