import discord
import os
import token as tk

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


# Main program
def main():
    print("--main program--")
    client.run(token)


# Defining main program
if __name__ == "__main__":
    main()