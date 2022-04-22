# -*- coding: utf-8 -*- 

import discord
from discord import Embed
from discord.ext import commands
import json
import sys, time
with open('./config.json', 'r', encoding='utf-8') as cjson:
    config = json.load(cjson)

with open('./liste.json', 'r', encoding='utf-8') as ljson:
    list = json.load(ljson)

bot = commands.Bot(command_prefix = config["prefix"], description = "Bot de Nathoune")

print('\033[36m' + '                     ██▓    ▓█████      ▄▄▄▄    ▒█████  ▄▄▄█████▓\n                    ▓██▒    ▓█   ▀     ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒\n                    ▒██░    ▒███       ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░\n                    ▒██░    ▒▓█  ▄     ▒██░█▀  ▒██   ██░░ ▓██▓ ░ \n                    ░██████▒░▒████    ▒░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ \n                    ░ ▒░▓  ░░░ ▒░     ░░▒▓███▀▒░ ▒░▒░▒░    ▒ ░░   \n                    ░ ░ ▒  ░ ░ ░      ░▒░▒   ░   ░ ▒ ▒░     ░    \n                      ░ ░      ░        ░    ░ ░ ░ ░ ▒    ░      \n                        ░  ░   ░      ░ ░          ░ ░          ')
print('\033[39m')

message = 'Mise en ligne, veuiller patientez un instant...\n\nTempts estimé : 5 secondes restantes . . . .'

for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

@bot.event
async def on_ready():
    activity = discord.Game(name="être inutile", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('\033[32m' + '\n\n                >En ligne< \n\n' + '\033' + '\n\n>>> NE SURTOUT PAS FERMER CETTE FENÊTRE ! LE BOT EST EN LIGNE UNIQUEMENT QUAND CETTE DERNIÈRE EST OUVERTE ! <<<' + '\033[39m' + '\n\n\n®Nathoune 2021')

   
@bot.event
async def on_message(message):
    
    [await message.channel.send(o['value']) for o in list if o['name'] == message.content.lower()]
    
    
    if message.content.lower() == ("{}h".format(config["prefix"])):
        embed1 = Embed(title="Commandes et mots :", color=0xffab33)
        embed1.add_field(name="{}h".format(config["prefix"]), value="Envoyer ce message", inline=False)
        embed1.add_field(name="{}news".format(config["prefix"]), value="Afficher les nouveautés !", inline=True)
        embed1.add_field(name="Salut", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Yo", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Comment tu vas ?", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bonjour", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Aide moi", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Aide-moi", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bravo", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Pourquoi ?", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Pourquoi ?", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Pk", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Pk ?", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Mdr", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Ptdr", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bot", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Le bot", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Le bot est éclaté", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Le bot est nul", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Tu sers à rien", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Re", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Nthoune", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bien et toi ?", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bien et toi", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Raid", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Tg le bot", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Tg", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Ta gueule", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Ta gueule le bot", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Putain", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Merde", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Jsp", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Je sais pas", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Lol", value="Réponse de Le_Bot", inline=False)
        embed1.set_image(url="https://cdn-0.emojis.wiki/emoji-pics/facebook/ok-hand-facebook.png")     
        await message.channel.send(embed=embed1)
        
    if message.content.lower() == ("{}news".format(config["prefix"])):
        embed1 = Embed(title="Voici le nouveautés !", color=0xffab33)
        embed1.add_field(name="Discord", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Ban", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bannir", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Python", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Java", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Abonnement", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Hello", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Vfx", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="3D", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="YouTube", value="Réponse de Le_Bot", inline=False)
        embed1.set_image(url="https://cdn-0.emojis.wiki/emoji-pics/facebook/ok-hand-facebook.png")     
        await message.channel.send(embed=embed1)

    
bot.run(config["token"])
