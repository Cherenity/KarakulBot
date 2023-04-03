import discord
import os
import token2 as tk
import requests
import random
from bs4 import BeautifulSoup
import messageMethods as mm
from PIL import Image

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

    if message.content.lower().startswith('!glamour'): 
        
        #Url for Eorzean Collection glamours page
        url1 = 'https://ffxiv.eorzeacollection.com/glamours'
        # Saves user input to variable
        variable = message.content.lower()[8:]
        variable = variable.strip()
        print(f"mo{variable}")

        # pageNumbers method checks how many pages of glamours
        # and returns a random page number 
        url1 = f"{url1}?page={mm.pageNumbers(url1)}"

        if not variable:
            print("IS EMPTY")       
        else:
            # modifys url by color
            url1 += mm.checkColor(variable)
            # modifys url by gender
            url1 += mm.checkGender(variable)
            # modifys url by classification
            url1 += mm.checkClassification(variable)

        print(url1)
        # if mm.checkColor(variable) != 0:
        #     color = mm.checkColor(variable)
        #     print(color)
        #     url1 = f"{url1}?&filter%5Bcolor%5D={color}"
        #     url1 = f'{url1}&page={mm.pageNumbers(url1)}'

        # Edits the url according to the genre  
        # url1 = f"{url1}{mm.checkGender(variable)}"
        # print(url1)

        response = requests.get(url1)
        soup = BeautifulSoup(response.text, 'html.parser')

        img_tags = soup.find_all('img')
        img_list = []
        for img in img_tags:
            if img['src'].startswith('https'):
                img_list.append(img['src'])

        random_img = random.choice(img_list)

        await message.channel.send(random_img)

    if message.content.startswith('!karakulBot'):
                # Get the path to the image
        image_path = r'D:\codeProjects\KarakulBot\rsz_1karakul.png'
        # Open the image using PIL
        image = Image.open(image_path)
        await message.channel.send('Hello! I am a karakul Bot. ')
        await message.channel.send(file=discord.File(image_path))
    

def main():
    print("--main program--")
    client.run(token)

# Defining main program
if __name__ == "__main__":
    main()