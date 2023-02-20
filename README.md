# MoonDiscordBot
This is an ongoing project I am using for testing and for fun to learn more about python and how to use discord bots to manage an assortment of server tasks that would be timeconsuming for a human to perform.

I have the discord bot currently running using uptime robot which sends a ping to the webpage that is being hosted on replits every 30 minutes to keep the page awake.

How to test the bot for yourself:

1. Create a discord account and create a server or make sure you are currently the owner of one
2. Paste the following link in a new webpage: https://discord.com/api/oauth2/authorize?client_id=1072337712809512991&permissions=1634235578432&scope=bot
3. Add the link to the discord server you would like to test it in
4. Send any of the premade commands to the bot through the discord message bar in the server where you added the bot

Commands:

!test - this command has the bot send back a confirmation that it is active

!suggest - this command followed by a word or a phrase will add the following word or phrase into a suggestion list stored in a replits database

!suggestion_list - this command will print out the existing suggestion list or a message noting there is no suggestions yet

!clear_suggestions - this command will clear the existing database of suggestions

!coin_flip - this command will return either heads or tails
