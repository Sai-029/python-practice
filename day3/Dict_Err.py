data ={"name":"sai"}
try:
    print(data["age"])
except KeyError:
    print("Key 'age' not found in the dictionary.")