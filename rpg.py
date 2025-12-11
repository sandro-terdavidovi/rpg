import json
enemy = 10
with open("hi.json", "r") as f:
    data = json.load(f)


def update_level():
    while data["playerxp"] >= data["playerlvl"] * 100:
        data["playerxp"] -= data["playerlvl"] * 100
        data["playerlvl"] += 1
        

def safeprogress():
    with open("hi.json", "w") as f:
        json.dump(data, f)
    

def updatestats():
    data["playerhp"] = data["playerlvl"] * data["basehp"]
    data["playerdamage"] = data["playerlvl"] * data["basedamage"]

def levelup():
    update_level()
    updatestats()

data["hpcap"] = data["playerhp"]
while enemy > 0:
    lol = input("type what you will do ")
    if data["playerhp"] <= 0:
        print("you died!")
        break
    else:
        if lol == "punch":
            data["playerhp"] = data["playerhp"] - 1
            enemy = enemy - data["playerdamage"]
            print(f"your hp: {data['playerhp']}")
            print(f"enemy hp {enemy}")
            
        elif lol == "heal":
            data["playerhp"] = data["playerhp"] + 3
            if data["playerhp"] > data["hpcap"]:
                data["playerhp"] = data["hpcap"]
            print(f"your hp: {data['playerhp']}")
        else:
            print("uh oh! you just failed use punch or heal next time!")

if enemy <= 0 and data["playerhp"] > 0:
    print("you won!")
    data["playerxp"] += 100
    levelup()
    print(f"you increased your level!: {data['playerlvl']}")


elif data["playerhp"] <= 0:
    print("you died")
    
safeprogress()


    

    