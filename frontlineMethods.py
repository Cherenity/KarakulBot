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
    upNext = ""
    borderlandRuins = ["Seal Rock", "\nThe Fields of Glory", "\nOnsal Hakair"]
    sealRock = ["The Fields of Glory", "\nOnsal Hakair", "\nBorderland Ruins"]
    theFieldsofGlory = ["Onsal Hakair", "\nBorderland Ruins", "\nSeal Rock"]
    onsalHakair = ["Borderland Ruins [gonna be removed soon]", "\nSeal Rock :rock:", "\nThe Fields of Glory :ice_cube:"]
    
    print("In development")

    currently = currentFrontline()
    
    if currently == "Borderland Ruins":
        for i in borderlandRuins:
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
    
def untilReset():
    print("In development")
    currentDay = datetime.datetime.today()
    
    reset = datetime.datetime(currentDay.year,currentDay.month, currentDay.day, 18, 0)

    if currentDay.hour >= 18:
        reset = reset + datetime.timedelta(days=1)

    reset -= currentDay

    hours = reset.seconds//3600
    minutes = (reset.seconds//60)%60

    return(f"{hours} hours and {minutes} minutes")

def frontlinesImg():
    currentF = currentFrontline()
    print(f"CURRENTLYYYYYYY {currentF}!")
    if currentF == "The Fields of Glory":
        return "fieldsof.png"
    elif currentF == "Onsal Hakair":
        return "onsalhak.png"
    elif currentF == "Seal Rock":
        return "sealrock.png"
    else:
        return "bordeland.png"

def frontlinesLink():

    currentF = currentFrontline()
    print(f"CURRENTLYYYYYYY {currentF}!")
    if currentF == "The Fields of Glory":
        return "https://na.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/4/"
    elif currentF == "Onsal Hakair":
        return "https://na.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/5/"
    elif currentF == "Seal Rock":
        return "https://na.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/3/"
    else:
        return "https://na.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/1/"

def addEmoji():
    print("Moi")

    currentF = currentFrontline()
    print(f"CURRENTLYYYYYYY {currentF}!")
    if currentF == "The Fields of Glory":
        return ":ice_cube:"
    elif currentF == "Onsal Hakair":
        return ":monkey:"
    elif currentF == "Seal Rock":
        return ":rock:"
    else:
        return "[gonna be removed soon]"




tas = frontlinesImg()
print("tuleeks oikein", tas)