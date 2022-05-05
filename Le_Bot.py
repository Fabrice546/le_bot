import asyncio
import discord
import json
import time
import sys
from discord import Embed
from discord.ext import commands
with open('./config.json', 'r', encoding='utf-8') as cjson:
    config = json.load(cjson)

with open('./liste.json', 'r', encoding='utf-8') as ljson:
    list = json.load(ljson)

bot = commands.Bot(command_prefix= config["prefix"], help_command=None)

def main():
    try:
        print('''
                    ██▓   ▓█████      ▄▄▄▄    ▒█████  ▄▄▄█████▓
                    ▓██▒   ▓█   ▀     ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
                    ▒██░   ▒███       ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
                    ▒██░   ▒▓█  ▄     ▒██░█▀  ▒██   ██░░ ▓██▓ ░
                    ░██████░▒████    ▒░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░
                    ░ ▒░▓  ░░ ▒░     ░░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░
                    ░ ░ ▒   ░ ░      ░▒░▒   ░   ░ ▒ ▒░     ░
                    ░ ░     ░        ░    ░ ░ ░ ░ ▒    ░ ░
                        ░     ░      ░ ░          ░ ░
        ''')

        message = '\nMise en ligne, veuiller patientez un instant...\n\nTempts estimé : 5 secondes restantes . . . .'

        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)

        page1 = embed1 = Embed(title="Commandes :", color=0xffab33)
        embed1.add_field(name="{}h".format(config["prefix"]), value="Envoyer ce message", inline=False)
        embed1.add_field(name="{}news".format(config["prefix"]), value="Afficher les nouveautés !", inline=False)
        embed1.add_field(name="{}serveur".format(config["prefix"]), value="Pour pouvoir rejoindre le serveur Discord !", inline=False)
        embed1.add_field(name="{}confidentiality".format(config["prefix"]), value="Connaître la politique de confidentialité.", inline=False)
        embed1.set_footer(text="🚨Réinvite moi pour pouvoir changer de pages : \nhttps://bit.ly/discord-le-bot ou clique sur le bouton bleu sur mon profil🚨")

        page2 = embed2 = Embed(title="Mots (page 1) :", color=0xffab33)
        embed2.add_field(name="Salut", value="Réponse", inline=True)
        embed2.add_field(name="Yo", value="Réponse", inline=True)
        embed2.add_field(name="Comment tu vas ?", value="Réponse", inline=True)
        embed2.add_field(name="Bonjour", value="Réponse", inline=True)
        embed2.add_field(name="Aide moi", value="Réponse", inline=True)
        embed2.add_field(name="Aide-moi", value="Réponse", inline=True)
        embed2.add_field(name="Bravo", value="Réponse", inline=True)
        embed2.add_field(name="Pourquoi ?", value="Réponse", inline=True)
        embed2.add_field(name="Pourquoi ?", value="Réponse", inline=True)
        embed2.add_field(name="Pk", value="Réponse", inline=True)
        embed2.add_field(name="Pk ?", value="Réponse", inline=True)
        embed2.add_field(name="Mdr", value="Réponse", inline=True)
        embed2.add_field(name="Ptdr", value="Réponse", inline=True)
        embed2.add_field(name="Bot", value="Réponse", inline=True)
        embed2.add_field(name="Le bot", value="Réponse", inline=True)
        embed2.add_field(name="Le bot est éclaté", value="Réponse", inline=True)
        embed2.add_field(name="Le bot est nul", value="Réponse", inline=True)
        embed2.add_field(name="Tu sers à rien", value="Réponse", inline=True)
        embed2.add_field(name="Re", value="Réponse", inline=True)
        embed2.add_field(name="Nathoune", value="Réponse", inline=True)
        embed2.add_field(name="Bien et toi ?", value="Réponse", inline=True)
        embed2.add_field(name="Bien et toi", value="Réponse", inline=True)
        embed2.add_field(name="Raid", value="Réponse", inline=True)
        embed2.add_field(name="Tg le bot", value="Réponse", inline=True)
        embed2.add_field(name="Tg", value="Réponse", inline=True)
        embed2.add_field(name="Ta gueule", value="Réponse", inline=True)
        embed2.add_field(name="Ta gueule le bot", value="Réponse", inline=True)
        embed2.add_field(name="Putain", value="Réponse", inline=True)
        embed2.add_field(name="Merde", value="Réponse", inline=True)
        embed2.add_field(name="Jsp", value="Réponse", inline=True)
        embed2.add_field(name="Je sais pas", value="Réponse", inline=True)
        embed2.add_field(name="Lol", value="Réponse", inline=True)  
        embed2.add_field(name="YouTube", value="Réponse", inline=True)
        embed2.add_field(name="3D", value="Réponse", inline=True)
        embed2.add_field(name="VFX", value="Réponse", inline=True)
        embed2.add_field(name="Hello", value="Réponse", inline=True)
        embed2.add_field(name="Abonnement", value="Réponse", inline=True)
        embed2.add_field(name="Java", value="Réponse", inline=True)
        embed2.add_field(name="Python", value="Réponse", inline=True)
        embed2.add_field(name="Bannir", value="Réponse", inline=True)
        embed2.add_field(name="Ban", value="Réponse", inline=True)
        embed2.add_field(name="Discord", value="Réponse", inline=True)
        embed2.set_footer(text="🚨Réinvite moi pour pouvoir changer de pages : \nhttps://bit.ly/discord-le-bot ou clique sur le bouton bleu sur mon profil🚨")

        page3 = embed3 = Embed(title="Mots (page 2) :", color=0xffab33)
        embed3.add_field(name="Ta gueule", value="Réponse", inline=True)
        embed3.add_field(name="Ta gueule le bot", value="Réponse", inline=True)
        embed3.add_field(name="Putain", value="Réponse", inline=True)
        embed3.add_field(name="Merde", value="Réponse", inline=True)
        embed3.add_field(name="Jsp", value="Réponse", inline=True)
        embed3.add_field(name="Je sais pas", value="Réponse", inline=True)
        embed3.add_field(name="Lol", value="Réponse", inline=True)  
        embed3.add_field(name="YouTube", value="Réponse", inline=True)
        embed3.add_field(name="3D", value="Réponse", inline=True)
        embed3.add_field(name="VFX", value="Réponse", inline=True)
        embed3.add_field(name="Hello", value="Réponse", inline=True)
        embed3.add_field(name="Abonnement", value="Réponse", inline=True)
        embed3.add_field(name="Java", value="Réponse", inline=True)
        embed3.add_field(name="Python", value="Réponse", inline=True)
        embed3.add_field(name="Bannir", value="Réponse", inline=True)
        embed3.add_field(name="Ban", value="Réponse", inline=True)
        embed3.add_field(name="Discord", value="Réponse", inline=True)
        embed3.set_footer(text="🚨Réinvite moi pour pouvoir changer de pages : \nhttps://bit.ly/discord-le-bot ou clique sur le bouton bleu sur mon profil🚨")

        page4 = embed4 = Embed(title="Informations :", color=0xffab33)
        embed4.add_field(name="Le_Bot, votre bot intéractif !", value="Le_Bot répondra à certains de vos mots en ajoutant de l'humour et du dynamisme sur votre serveur !\nSon code source se trouve sur GitHub, il est donc opensource ! Voici son lien : https://github.com/Nathoune-YT/le_bot. Vous pouvez l'améliorer ou simplement l'utiliser tout en suivant la procédure présente dans le README.\nVoici la politique de confidentialité : https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt", inline=True)
        embed4.set_footer(text="🚨Réinvite moi pour pouvoir changer de pages : \nhttps://bit.ly/discord-le-bot ou clique sur le bouton bleu sur mon profil🚨")

        bot.help_pages = [page1, page2, page3, page4]

        @bot.event
        async def on_ready():
            activity = discord.Game(name="être inutile", type=1)
            await bot.change_presence(status=discord.Status.online, activity=activity)
            print('\n\n\n                >En ligne< \n\n\n\n>>> NE SURTOUT PAS FERMER CETTE FENÊTRE ! LE BOT EST EN LIGNE UNIQUEMENT QUAND CETTE DERNIÈRE EST OUVERTE ! <<<\n\n\n®Nathoune 2022')

        @bot.event
        async def on_message(message):
            await bot.process_commands(message)
            
            [await message.channel.send(o['value']) for o in list if o['name'] == message.content.lower()]

        @bot.command()
        async def h(ctx):
            buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
            current = 0
            msg = await ctx.send(embed=bot.help_pages[current])

            for button in buttons:
                await msg.add_reaction(button)

            while True:
                try:
                    reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user : user == ctx.author and reaction.emoji in buttons, timeout=60.0)

                except asyncio.TimeoutError:
                    await msg.clear_reactions()

                else:
                    previous_page = current

                    if reaction.emoji == u"\u23EA":
                        current = 0

                    elif reaction.emoji == u"\u25C0":
                        if current > 0 :
                            current -= 1

                    elif reaction.emoji == u"\u25B6":
                        if current < len(bot.help_pages)-1:
                            current += 1

                    elif reaction.emoji == u"\u23E9":
                        current = len(bot.help_pages)-1
                    
                    for button in buttons:
                        await msg.remove_reaction(button, ctx.author)

                    if current != previous_page:
                        await msg.edit(embed=bot.help_pages[current])

        @bot.command()
        async def confidentiality(ctx):
            await ctx.send("**Voici la politique de condfidentialité de Le_Bot** : https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt")

        @bot.command()
        async def serveur(ctx):
            await ctx.send("**Voici le serveur Nathoune_Serveur Résurection** : https://discord.gg/b6jjy5yKXV")

        @bot.command()
        async def news(ctx):
            embed1 = Embed(title="Voici le nouveautés !", color=0xffab33)
            embed1.add_field(name="{}serveur".format(config["prefix"]), value="Pour pouvoir rejoindre le serveur Discord !", inline=False)
            embed1.add_field(name="{}confidentiality".format(config["prefix"]), value="Connaître la politique de confidentialité.", inline=False)
            embed1.add_field(name="Discord", value="Réponse", inline=True)
            embed1.add_field(name="Ban", value="Réponse", inline=True)
            embed1.add_field(name="Bannir", value="Réponse", inline=True)
            embed1.add_field(name="Python", value="Réponse", inline=True)
            embed1.add_field(name="Java", value="Réponse", inline=True)
            embed1.add_field(name="Abonnement", value="Réponse", inline=True)
            embed1.add_field(name="Hello", value="Réponse", inline=True)
            embed1.add_field(name="Vfx", value="Réponse", inline=True)
            embed1.add_field(name="3D", value="Réponse", inline=True)
            embed1.add_field(name="YouTube", value="Réponse", inline=True)     
            await ctx.channel.send(embed=embed1)

        bot.run(config["token"])

    except:
        main()
main()
