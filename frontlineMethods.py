import datetime


def currentFrontline():
    # Creating dict that contains all 4 FFXIV frontlines maps
    frontlineMaps = {0: "Borderland Ruins", 1: "Seal Rock", 2: "The Fields of Glory", 3: "Onsal Hakair"}

    givenDate = datetime.datetime(2023, 5, 10) 

    currentDay = datetime.datetime.today()
    delta = currentDay - givenDate
    deltaDays = delta.days
    # calculate daily reset FFXIV
    if currentDay.hour >= 18:
        deltaDays += 1

    print(f"There are {deltaDays} resets between {givenDate.date()} and {currentDay.date()}")

    # % = modulo, delta (muutos)
    value = deltaDays % 4

    print(frontlineMaps[value])

    return frontlineMaps[value]

def upNext():
    upNext = "Up Next:"
    borderlandRuins = ["**Seal Rock**,", "The Fields of Glor", "Onsal Hakair"]
    sealRock = ["**The Fields of Glory**,", "Onsal Hakair,", "Borderland Ruins"]
    theFieldsofGlory = ["**Onsal Hakair**,", "Borderland Ruins,", "Seal Rock"]
    onsalHakair = ["**Borderland Ruins**,", "Seal Rock,", "The Fields of Glory"]
    
    print("In development")

    currently = currentFrontline()
    
    if currently == "Borderland Ruins":
        for i in sealRock:
            upNext += " " + i
        return upNext
    
    elif currently == "Seal Rock":
        for i in sealRock:
            upNext += " " + i
        return upNext
    
    elif currently == "The Fields of Glory":
        for i in theFieldsofGlory:
            upNext += " " + i
        return upNext
    
    else:

        for i in onsalHakair:
            upNext += " " + i
            return upNext
    


hello = upNext()
print(hello)