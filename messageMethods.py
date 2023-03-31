import discord
import random
import requests
apiKey = 'd69a63c25402479d87c5db5f42bcd666'

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