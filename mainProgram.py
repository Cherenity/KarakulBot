import discord
import os
import token2 as tk
import requests
import random
from bs4 import BeautifulSoup
import messageMethods as mm

token = tk.token()

intents = discord.Intents.default()
intents.message_content = True

# Connection to the discord:
client = discord.Client(intents=intents)

# Called when bot is ready for use:
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.lower().startswith('!news'):
        embed = mm.newsMethod()
        await message.channel.send(embed=embed)

    if message.content.startswith('!_glamour'):
        url = 'https://ffxiv.eorzeacollection.com/glamours'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        img_tags = soup.find_all('img')
        img_list = []
        for img in img_tags:
            if img['src'].startswith('https'):
                img_list.append(img['src'])

        random_img = random.choice(img_list)
        await message.channel.send(random_img)
                    
def main():
    print("--main program--")
    client.run(token)


# Defining main program
if __name__ == "__main__":
    main()

    # classification
    # ?filter%5Bclassification%5D=4
    # 1=cool, 2=sdasd. 3=cute

    # https://ffxiv.eorzeacollection.com/glamours?filter%5Bclassification%5D=4

   # https://ffxiv.eorzeacollection.com/glamours?filter%5Bclassification%5D=1&filter%5Bgender%5D=female
   # gende female, male, any --> &filter%5Bgender%5D=[ADD HERE]

   # color: 

    # https://ffxiv.eorzeacollection.com/glamours?
  # &filter%5Bcolor%5D=46

  # https://ffxiv.eorzeacollection.com/glamours?&filter%5Bcolor%5D=46

  # 46 = Pink, 42 = Blue

  # female, divine, blue
  # https://ffxiv.eorzeacollection.com/glamours?filter%5Bclassification%5D=4&filter%5Bgender%5D=female&filter%5Bcolor%5D=42