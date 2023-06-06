import json


def getUser(username):
    f = open("data.json")
    data = json.load(f)
    for user in data["users"]:
        if user["username"] == username:
            f.close()
            return user
        
    print("User not Found!!!")
    return

def setCash(username, cash, edit=False):
    f = open("data.json")
    data = json.load(f)
    for user in data["users"]:
        if user["username"] == username:
            if edit:
                user["cash"] += cash
                
            else:
                user["cash"] = cash
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)
    f.close()
    return

def createUser(username, name, password):
    f = open("data.json")
    data = json.load(f)
    data.append({"username":username, "name":name,"password":password, "cash":1000})
    with open("data.json", "w") as outfile:
        json.dump(data, outfile)
    f.close()