import discord
import token2 as tk
import requests
import random
from bs4 import BeautifulSoup
import messageMethods as mm
from PIL import Image
import emoji

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
    
    if message.content.lower().startswith('!glamourhelp'):
        text = "Help option is currently in maintanance!"
        await message.channel.send(text)
        return

    if message.content.startswith('!check'):
        msg = await message.channel.send('React with an emoji!')
        reaction, user = await client.wait_for('reaction_add', check=lambda reaction, user: user == message.author)
        emoji = reaction.emoji
        if emoji == '👍':
            await message.channel.send(f'{user} reacted with 👍!')
        elif emoji == '👎':
            await message.channel.send(f'{user} reacted with 👎!')
        else:
            await message.channel.send(f'{user} reacted with {emoji}!')


    if message.content.startswith('!hello'):
        image = Image.open("karakul.png")
        image = image.resize((100, 100))
        image.save("resized_image.png")
        
        embed = discord.Embed(title="Hello!", description="I am karakul bot!", color=0xFFFFFF)
        file = discord.File("resized_image.png", filename="resized_image.png")
        embed.set_image(url="attachment://resized_image.png")
         
        await message.channel.send(file=file, embed=embed)

    if message.content.lower().startswith('!news'):
        embed = mm.newsMethod()
        await message.channel.send(embed=embed)

    if message.content.lower().startswith('!glamour'): 
        
        #Url for Eorzean Collection glamours page
        url1 = 'https://ffxiv.eorzeacollection.com/glamours'
        # Saves user input to variable
        variable = message.content.lower()[8:]
        variable = variable.strip()
        print(f"Variable is {variable}")

        url1 = f"{url1}?page={mm.pageNumbers(url1)}"

        if not variable:
            print("Variable is empty")       
        else:
            # modifys url by color
            url1 += mm.checkColor(variable)
            # modifys url by gender
            url1 += mm.checkGender(variable)
            # modifys url by classification
            url1 += mm.checkClassification(variable)
            # modifys url by gender
            url1 += mm.checkRace(variable)

        # pageNumbers method checks how many pages of glamours
        # and returns a random page number 
        
        print(url1)

        response = requests.get(url1)
        soup = BeautifulSoup(response.text, 'html.parser')

        img_tags = soup.find_all('img')
        img_list = []
        for img in img_tags:
            if img['src'].startswith('https'):
                img_list.append(img['src'])

        random_img = random.choice(img_list)

        glamourNro = random_img.split("/")[-2]
        link = f"https://ffxiv.eorzeacollection.com/glamour/{glamourNro}"

        # Gets a title from link and stores it to title variable
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').text
        title = title.split('|')[0].strip()

        tags = ""
        for tag in soup.find_all('div', {'class': 'c-tag-cloud'}):
            tags = tag.text
        
        tags = tags.replace("\n", " ")
        tags = tags.strip()
        print(tags)
        # Create a new embed message and set its title, description, and image
        embed = discord.Embed(title=title, url=link)
        embed.set_image(url=random_img)
        # embed.add_field(name="", value=f'[{title}]({link})', inline=False)
        embed.set_footer(text=f'Tags: {tags} ❀*~')
        embed.color = discord.Color.dark_blue()

        # Send the embed message to your Discord channel
        await message.channel.send(embed=embed)

        # await message.channel.send(f"<{link}>")
        # await message.channel.send(random_img)

        
        
        # 160294
        #https://ffxiv.eorzeacollection.com/glamour/

    if message.content.startswith('!karakulBot'):
                # Get the path to the image
        image_path = r'D:\codeProjects\KarakulBot\rsz_1karakul.png'
        # Open the image using PIL
        image = Image.open(image_path)
        await message.channel.send('Hello! I am a karakul Bot. ')
        await message.channel.send(file=discord.File(image_path))

def main():
    print(emoji.emojize(":smiling_face_with_heart-eyes:"))
    print("~main program~")
    client.run(token)

# Defining main program
if __name__ == "__main__":
    main()