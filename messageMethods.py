import discord
import random
import requests
import token2
from bs4 import BeautifulSoup

apiKey = token2.apiKey()

def newsMethod():
    try:
        # Set the URL for the News API request
        url = f'https://newsapi.org/v2/top-headlines?country=us&pageSize=100&apiKey={apiKey}'

        # Make a request to the News API and get the response as JSON
        response = requests.get(url).json()

        # Get the list of articles from the response
        articles = response['articles']

        # Select a random article from the list of articles
        article = random.choice(articles)

        # Get the title, description, and URL of the selected article
        title = article['title']
        description = article['description']
        url = article['url']

        # Create an embedded message with the title, description, and URL of the selected article
        embed = discord.Embed(title=title, description=description, url=url)

        # Send the embedded message to the Discord channel
        return embed
        
    except Exception as e:
    # Print any errors that occur to the console
     print(e)

def pageNumbers(urlParameter):
    # URL to scrape
    url =  urlParameter

    # return value if reading URL gives an error
    rvalue = 500

    try:
        # Create a session object to persist cookies across requests
        session = requests.Session()

        # Send a GET request to the URL and get the response
        response = session.get(url)

        # Parse the HTML content of the response using BeautifulSoup
        soup = BeautifulSoup(response.content, 'lxml')

        # Find the heading element with class 'l-section-label l-section-pagination-title'
        heading = soup.find('h3', {'class': 'l-section-label l-section-pagination-title'})

        # Get the page count from the text of the heading element
        page_count = int(heading.text.split()[-1])

        # Return page_count
        return random.randint(1, page_count)

    except requests.exceptions.RequestException as e:
        print("Error occurred while making a request to the server:", e)
        return random.randint(1, rvalue)

    except Exception as e:
        print("An error occurred:", e)
        return random.randint(1, rvalue)
    
def checkSpaces(Test_string):
    return Test_string.count(" ")

def checkColor(word):    
    # Color options added to colorsDictionary   
    colorsDictionary = {"beige":40,"black":41, "blue": 42, "brown":43, "grey":44,
                            "orange":45, "pink": 46, "purple":47, "red": 48, "white": 49, 
                            "yellow": 50, "green": 51, "silver": 52, "gold":53, "metallic": 63, 
                            "pastel": 64, "monochromatic": 62}
    
    words = word.split(" ")
    # Initializing a new empy dictionary
    newDictionary = {}

    for word in words:
        if word in colorsDictionary:
            newDictionary[word] = colorsDictionary[word]
    
    if len(newDictionary) == 1:
        newList = list(newDictionary.items())
        value = newList[0][1]
        newValue = f"&filter%5Bcolor%5D={value}"
        return newValue
    else:
        return ""

def checkGender(word):
    if 'female' in word:
        print('female')
        return '&filter%5Bgender%5D=female'
    elif 'male' in word:
        print('male')
        return '&filter%5Bgender%5D=male'
    else:
        print('any')
        return '&filter%5Bgender%5D=any'

def checkClassification(word):    
    # Color options added to colorsDictionary   
    colorsDictionary = {"athletic":1,"cool":2, "cute": 3, "divine": 4, "elegant": 5, 
                        "fashionable" : 6, "glamorous" : 7, "sexy": 8, "sweet": 9,
                        "youthful": 10, "heroic": 11, "villainous": 12, "strong": 13}

    words = word.split(" ")
    # Initializing a new empy dictionary
    newDictionary = {}

    for word in words:
        if word in colorsDictionary:
            newDictionary[word] = colorsDictionary[word]
    
    if len(newDictionary) == 1:
        newList = list(newDictionary.items())
        value = newList[0][1]
        newValue = f"&filter%5Bclassification%5D={value}"
        return newValue
    else:
        return ""

def checkRace(word): 
    # Color options added to colorsDictionar
    list = ["hyur", "elezen", "highlander", "miqote", "lalafell", 
            "roegadyn", "aura", "viera", "hrothgar"] 
    
    words = word.split(" ")
    # Initializing a new empy dictionary
    
    nword = ""

    for word in words:
        if word in list:
            nword = word
            break

    return f"&filter%5Brace%5D%5B%5D={nword}"

def checkJob(word): 
    # Color options added to colorsDictionar
    list = [""]
    words = word.split(" ")
    list = ["pld","war","drk", "gnb", "rdm", "whm", "ast", "sch", "sge", 
            "mnk", "drg", "rpr", "nin", "sam", "blm", "smn", "brd",  "dnc",
            "mch", "blu"]  
    nword = ""

    for word in words:
        if word in list:
            nword = word
            break

    return f"&filter%5Bjob%5D%5B%5D={nword}&filter%5BrestrictJob%5D=1"

    
    
    