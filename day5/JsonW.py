import json
St={
    "name":"sai",
    "role":"Devops"
}
with open("St.json","w") as f:
    json.dump(St,f,indent=4)


St["age"]= 20
with open("st.json","w") as f:
    json.dump(St,f,indent=4)