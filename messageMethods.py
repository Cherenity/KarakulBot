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

