import datetime
from datetime import timedelta

def currentFrontline():
    #Organising all frontline map names in dictionary
    frontlineMaps = {0: "Seal Rock", 1: "The Fields of Glory", 2: "Onsal Hakair"}

    givenDate = datetime.datetime(2023, 6, 16) 

    currentDay = datetime.datetime.today()
    delta = currentDay - givenDate
    deltaDays = delta.days
    # calculate daily reset FFXIV
    if currentDay.hour >= 18:
        deltaDays += 1

    print(f"There are {deltaDays} resets between {givenDate.date()} and {currentDay.date()}")

    # % = modulo, delta (muutos)
    value = deltaDays % 3


    return frontlineMaps[value]

def upNext():
    upNext = ""
    sealRock = ["The Fields of Glory", "\nOnsal Hakair"]
    theFieldsofGlory = ["Onsal Hakair", "\nSeal Rock"]
    onsalHakair = ["\nSeal Rock :rock:", "\nThe Fields of Glory :ice_cube:"]
    

    currently = currentFrontline()
    
    if currently == "Seal Rock":
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
    print(f"--ongoing-- {currentF}!")
    if currentF == "The Fields of Glory":
        return "https://na.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/4/"
    elif currentF == "Onsal Hakair":
        return "https://na.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/5/"
    elif currentF == "Seal Rock":
        return "https://na.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/3/"
    else:
        return "https://na.finalfantasyxiv.com/lodestone/playguide/contentsguide/frontline/1/"

def addEmoji():
    print("--add pvpEmoji Function--")
    currentF = currentFrontline()
    print(f"--ongoingEmoji-- {currentF}!")
    if currentF == "The Fields of Glory":
        return ":ice_cube:"
    elif currentF == "Onsal Hakair":
        return ":monkey:"
    else:
        return ":rock:"


