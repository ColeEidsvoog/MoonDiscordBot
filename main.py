import os
import discord
import requests
import json
import random
import tweepy 
from replit import db
from Keep_awake import keep_awake


intents = discord.Intents().all()
client = discord.Client(intents=intents);
  
@client.event
async def on_ready():
  print('We have logged in as {0.user} '.format(client))

@client.event
async def on_message(message):
  msg = message.content

  if message.author == client.user:
    return 

# Test section--------------------------------------------------------------------------- 
  if message.content.startswith('!test'):
    await message.channel.send("I am working properly!")

# Test section---------------------------------------------------------------------------
  if message.content == "!help":
    await message.channel.send("Here are all the commands I know \n!test\n!suggest\n!suggestion_list\n!clear_suggestions\n!coin_flip")
    
# Encouraging words section---------------------------------------------------------------
  sad_words = ["sad", "upset", "depressed", "unhappy", "miserable", "heartbroken"]

  happy_list = [
    "It will be okay!", 
    "You will make it though this!",
    "It's always darkest before the dawn!",
    "Times can be tough, just take it one step at a time and you'll make it through this!",
    "Don't dwell on the past, make tommorow a better day!"
  ]
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(happy_list))

    
# Suggestion section----------------------------------------------------------------------
  suggestion = []
  suggestions = []
  
  if message.content.startswith('!suggest '):
    suggestion = message.content[9:]
    
  if suggestion:
    db[message.author.name] = suggestion
    await message.channel.send("Thank you for the suggestion!")

  if message.content == '!suggestion_list':
    for key in db.keys():
      if message.guild.get_member_named(key):
        suggestions.append(f'{key}: {db[key]}')
    if suggestions:
      await message.channel.send('\n'.join(suggestions))
    if len(suggestions) == 0:
      await message.channel.send("Im sorry, I haven't received any suggestions yet!")
        
  if message.content == '!clear_suggestions':
    db.clear()
    await message.channel.send("I have cleared the suggestions database for you!")
#Coin flip section---------------------------------------------------------------------------
  if message.content == '!coin_flip':
    coin_value = random.randint(1,2)

    if coin_value == 1:
      await message.channel.send("It's heads!")
    else:
      await message.channel.send("It's tails!")

#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------    
  
keep_awake()


client.run(os.environ['Token'])


