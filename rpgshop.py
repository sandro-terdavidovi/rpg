import json

with open("hi.json", "r") as f:
    data = json.load(f)

hi = input("what do you want to buy? (sword/armor)")

if hi == "sword":
    print("we have multiple things there! (copper sword/iron sword/great sword)")
    hi2 = input("what do you want to buy?")
    
    if hi2 == "copper sword" and data["coins"] >= 50 and data["coppersword"] == False:
        print("you bought copper sword!")
        data["playerdamage"] *= 2
        data["coppersword"] = True
        data["coins"] -= 50
    
    elif hi2 == "iron sword" and data["coins"] >= 100 and data["ironsword"] == False:
        print("you bought iron sword!")
        data["playerdamage"] *= 4
        data["ironsword"] = True
        data["coins"] -= 100
    
    elif hi2 == "great sword" and data["coins"] >= 500 and data["greatsword"] == False:
        print("you bought great sword!")
        data["playerdamage"] *= 10
        data["greatsword"] = True
        data["coins"] -= 500
    
    else:
        print("uh oh! you dont have enough or already own it")
        
elif hi == "armor":
    print("we have multiple things there! (copper armor, iron armor, titanium armor)")
    hi2 = input("what do you want to buy?")
    if hi2 == "copper armor" and data["coins"] >= 50 and data["copperarmor"] == False:
        data["coins"] -= 50
        data["playerhp"] *= 2
        data["copperarmor"] == True
    elif hi2 == "iron armor" and data["coins"] >= 100 and data["ironarmor"] == False:
        data["coins"] -= 100
        data["playerhp"] *= 4
        data["ironarmor"] == True
    elif hi2 == "titanium armor" and data["coins"] >= 500 and data["titaniumarmor"] == False:
        data["coins"] -= 500
        data["playerhp"] *= 10
        data["titaniumarmor"] == True
else:
    print("deleting win34...")

with open("hi.json", "w") as f:
    json.dump(data, f)
