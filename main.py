# Import libraries
import os
import discord
import requests
import json
import random
import tweepy 
from replit import db
from Keep_alive import keep_alive

# Set Discord client and Intents to all
intents = discord.Intents().all()
client = discord.Client(intents=intents);

# Event listener for successful client login
@client.event
async def on_ready():
  print('We have logged in as {0.user} '.format(client))

# Event listener for incoming messages
@client.event
async def on_message(message):
  msg = message.content

# If the message is sent by the bot, ignore it
  if message.author == client.user:
    return 

# Test section--------------------------------------------------------------------------- 
  if message.content.startswith('!test'):
    await message.channel.send("I am working properly!")

# Help section---------------------------------------------------------------------------
  if message.content == "!help":
    await message.channel.send("Here are all the commands I know \n!test\n!suggest\n!suggestion_list\n!clear_suggestions\n!coin_flip\n I am also programmed to respond to some sad words with a response!")
    
# Complimnet section----------------------------------------------------------------------
# List of words that trigger the bot to send a compliment message
  sad_words = ["sad", "upset", "depressed", "unhappy", "miserable", "heartbroken", "cry"]

# Open the file containing compliments and read its contents into a list
  with open('compliments.txt') as f:
    compliments = f.readlines()

# Get a random compliment from the list
  compliment = random.choice(compliments)
# If the user sends a message containing a sad word, send a compliment message
  if any(word in msg for word in sad_words):
    await message.channel.send(compliment)

    
# Suggestion section----------------------------------------------------------------------
  suggestion = []
  suggestions = []
  
# If the message starts with '!suggest ', save the following text as a suggestion
  if message.content.startswith('!suggest '):
    suggestion = message.content[9:]

# If there is a suggestion, save it to a database and notify the user
  if suggestion:
    db[message.author.name] = suggestion
    await message.channel.send("Thank you for the suggestion!")

# If the message is '!suggestion_list', grab all suggestions from the database and display them
  if message.content == '!suggestion_list':
    for key in db.keys():
      if message.guild.get_member_named(key):
        suggestions.append(f'{key}: {db[key]}')
    if suggestions:
      await message.channel.send('\n'.join(suggestions))
    if len(suggestions) == 0:
      await message.channel.send("Im sorry, I haven't received any suggestions yet!")

# If the message is '!clear_suggestions', clear the suggestion database
  if message.content == '!clear_suggestions':
    db.clear()
    await message.channel.send("I have cleared the suggestions database for you!")
#Coin flip section---------------------------------------------------------------------------
# If the message is '!coin_flip', randomly determine heads or tails and send a message
  if message.content == '!coin_flip':
    coin_value = random.randint(1,2)

    if coin_value == 1:
      await message.channel.send("It's heads!")
    else:
      await message.channel.send("It's tails!")

#-------------------------------------------------------------------------------------------
    
# Start the keep_alive function
keep_alive()

# Start the Discord bot with the token stored in the environment variables
client.run(os.environ['Token'])


