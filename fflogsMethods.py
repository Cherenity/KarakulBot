import discord
import random
import requests
import token2
from bs4 import BeautifulSoup
from selenium import webdriver

lightDataCenter = ["alpha", "lich", "odin", "phoenix", "raiden", "shiva", "twintania", "zodiark"]
expansions = ["endwalker", "shadowbringers", "stormblood", "heavensward"]

def getLightDataCenterList():
    return lightDataCenter

def urlReplaceServerfNamelName(url, server, fName, lName):
    url = url.replace("fName", fName)
    url = url.replace("lName", lName)
    url = url.replace("server", server)
    return url

def checkIfExpansionParameter(variable):
    print("test ", variable)
    expansion = []

    for word in variable.split(" "):
        if word in expansions:
            expansion.append(word)
        else:
            print("nej")

    if len(expansion) != 0:  
        if expansion[0] == "endwalker":
            return "?zone=49"
        elif expansion[0] == "shadowbringers":
            return "?zone=38"
        elif expansion[0] == "stormblood":
            return "?zone=25"
        else:
            return "?zone=13"
    else:
        return ""

def getCharacterImage(url):

    # Make a GET request to the website and get the HTML content
    response = requests.get(url)
    html = response.content
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser") 
    # Search for player Image
    playerImage = soup.find_all("img", {"id": "character-portrait-image"})
    print(playerImage)

    return playerImage

def returnLogs(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    rendered_html = driver.page_source

    soup = BeautifulSoup(rendered_html, 'html.parser')
    text = soup.find('b').text.strip()

    return text






