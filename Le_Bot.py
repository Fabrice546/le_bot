#Code officiel de Le_Bot par Nathoune#3630

#Importation des librairies nécéssaires
import asyncio
from inspect import Traceback
import discord
import json
import time
import sys
from discord import Embed
from discord.ext import commands
import os

#Ouverture et configuration des 2 fichiers json pour les mots auxquels Le_Bot réagit, le préfix et le token
with open('./config.json', 'r', encoding='utf-8') as cjson:
    config = json.load(cjson)

with open('./liste.json', 'r', encoding='utf-8') as ljson:
    list = json.load(ljson)

#Configuration des intents (rdv Discord Devlopper Portal)
intents = discord.Intents.default()
intents.members = True

#Mise en place du bot en précisant le préfix, les pages pour la commande "help" et "news" et les intents (les trois sont définis au dessus)
bot = commands.Bot(command_prefix= config["prefix"], help_command=None, news_pages=None, intents = intents)

#Définition de la fonction main
def main():
    #Il essaye de faire tout ce qui suit
    try:
        #Affichage d'une "interface"
        print("""
             ██▓    ▓█████      ▄▄▄▄    ▒█████  ▄▄▄█████▓
            ▓██▒    ▓█   ▀     ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
            ▒██░    ▒███       ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
            ▒██░    ▒▓█  ▄     ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
            ░██████▒░▒████    ▒░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
            ░ ▒░▓  ░░░ ▒░     ░░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
            ░ ░ ▒  ░ ░ ░      ░▒░▒   ░   ░ ▒ ▒░     ░    
              ░ ░      ░        ░    ░ ░ ░ ░ ▒    ░      
                ░  ░   ░      ░ ░          ░ ░           
        """)
        
        #Message pour prévenir que Le_Bot va bientôt être en ligne
        message = "Mise en ligne, veuiller patientez un instant.\n\nMise en ligne . . . ."

        #Affichage du message
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)

        #Définition des pages de la commande "help" car elle est dynamique
        #Page 1 :
        page1_h = embed_help_page_1 = discord.Embed(title="⚙️ Commandes :\n", color=0xffab33)
        embed_help_page_1.add_field(name="📃 {}h".format(config["prefix"]), value="`Envoyer ce message.`")
        embed_help_page_1.add_field(name="📑 {}news".format(config["prefix"]), value="`Afficher les nouveautés.`", inline=False)
        embed_help_page_1.add_field(name="📞 {}serveur".format(config["prefix"]), value="`Pour pouvoir rejoindre le serveur Discord.`", inline=False)
        embed_help_page_1.add_field(name="🗒️ {}confidentiality".format(config["prefix"]), value="`Connaître la politique de confidentialité.`", inline=False)
        embed_help_page_1.add_field(name="👌 {}site".format(config["prefix"]), value="`Le site officiel de Le_Bot.`", inline=False)
        embed_help_page_1.add_field(name="❓ {}how_work".format(config["prefix"]), value="`Comment fonctionne la nouvelle commande 'help'.`", inline=False)
        embed_help_page_1.add_field(name="🔗 {}github".format(config["prefix"]), value="`Le_Bot sur GitHub.`", inline=False)
        embed_help_page_1.add_field(name="📶 {}ping".format(config["prefix"]), value="`Tester la vitesse de réception de message.`", inline=False)
        embed_help_page_1.add_field(name="⚖️ {}toggle".format(config["prefix"]), value="`Permet de désactiver ou activer les commandes. Attention cette commande requiert les persmissions administrateur !`", inline=False)
        embed_help_page_1.add_field(name="🚮 {}delete invits".format(config["prefix"]), value="`Permet de désactiver ou activer la suppression automatique des liens d'invitation Discord. Attention cette commande requiert les persmissions administrateur !`", inline=False)
        embed_help_page_1.set_footer(text="\n ▶️ Mots | ⏩ Fin\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        #Page 2 :
        page2_h = embed_help_page_2 = discord.Embed(title="📋 Mots :", color=0xffab33,
        description="""`
🟡 Salut              🟡 Le bot est éclaté    🟡 Lol
🟡 Yo                 🟡 Le bot est nul       🟡 YouTube
🟡 Comment tu vas ?   🟡 Tu sers à rien       🟡 3D
🟡 Bonjour            🟡 Re                   🟡 VFX
🟡 Aide moi           🟡 Nathoune             🟡 Hello
🟡 Aide-moi           🟡 Bien et toi ?        🟡 Abonnement
🟡 Bravo              🟡 Bien et toi          🟡 Java
🟡 Pourquoi ?         🟡 Raid                 🟡 Python
🟡 Pourquoi ?         🟡 Tg le bot            🟡 Bannir
🟡 Pk                 🟡 Tg                   🟡 Ban
🟡 Pk ?               🟡 Ta gueule le bot     🟡 Discord
🟡 Mdr                🟡 Putain               🟡 Feur
🟡 Ptdr               🟡 Merde                🟡 Nyan Cat
🟡 Bot                🟡 Jsp                  🟡 Paypal
🟡 Le bot             🟡 Je sais pas          🟡 Coucou
🟡 GPU                🟡 CPU                  🟡 RAM
`""", inline=False)
        embed_help_page_2.set_footer(text="\nDébut ⏪ | Commandes ◀️ | ▶️ Informations | ⏩ Fin\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        #Page 3 :
        page3_h = embed_help_page_5 = Embed(title="📂 Informations :", color=0xffab33)
        embed_help_page_5.add_field(name="Le_Bot, votre bot interactif !", value="""▶️ Le_Bot répondra à certains de vos mots en ajoutant de l'humour et du dynamisme sur votre serveur !

▶️ Son code source se trouve sur GitHub, il est donc opensource ! Voici son lien : https://github.com/Nathoune-YT/le_bot. Vous pouvez l'améliorer ou simplement l'utiliser tout en suivant la procédure présente dans le README.

▶️ Voici la politique de confidentialité : https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt

▶️ Le site web officiel de Le_Bot : https://le-bot.cf (il prend un peu de temps à se charger chez certaines personnes)

▶️ Le prefix de Le_Bot change ! Il s'agit désormais de `{}` au lieu de `!`

▶️ Pour toutes questions, veuillez contacter le créateur de Le_Bot : `nathouneyoutube@hotmail.com` par mail ou `Nathoune#3630` sur Discord.""".format(config["prefix"]), inline=True)
        embed_help_page_5.set_footer(text="\nDébut ⏪ | Mots ◀️\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        #Mise en place des pages pour la commande "help"
        bot.help_pages = [page1_h, page2_h, page3_h]

        #Définition des pages de la commande "news" car elle est dynamique
        #Page 1 :
        page1_news = embed_news_page_1 = discord.Embed(title="📈 Nouvelles commandes :", color=0xffab33)
        embed_news_page_1.add_field(name="👌 {}site".format(config["prefix"]), value="`Le site officiel de Le_Bot.`", inline=False)
        embed_news_page_1.add_field(name="❓ {}how_work".format(config["prefix"]), value="`Comment fonctionne la nouvelle commande 'help'.`", inline=False)
        embed_news_page_1.add_field(name="🔗 {}github".format(config["prefix"]), value="`Le_Bot sur GitHub.`", inline=False)
        embed_news_page_1.add_field(name="📶 {}ping".format(config["prefix"]), value="`Tester la vitesse de réception de message. `", inline=False)
        embed_news_page_1.add_field(name="⚖️ {}toggle".format(config["prefix"]), value="`Permet de désactiver ou activer les commandes. Attention cette commande requiert les persmissions administrateur !`", inline=False)
        embed_news_page_1.add_field(name="🚮 {}delete invits".format(config["prefix"]), value="`Permet de désactiver ou activer la suppression automatique des liens d'invitation Discord. Attention cette commande requiert les persmissions administrateur !`", inline=False)
        embed_news_page_1.set_footer(text="\n ▶️ Nouveaux mots | ⏩ Fin\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        #Page 2 :
        page2_news = embed_news_page_2 = discord.Embed(title="⏏️ Nouveaux mots :", color=0xffab33, description="""`
🟡 Feur            🟡 RAM    
🟡 Paypal          🟡 GPU   
🟡 Nyan Cat        🟡 CPU   
`""")
        embed_news_page_2.set_footer(text="\n Début ⏪ | Nouvelles commandes ◀️ | ▶️ Nouveau préfix | ⏩ Fin\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        #Page 3 :
        page3_news = embed_news_page_3 = discord.Embed(title="🤟 Nouveau préfix !", color=0xffab33, description="Le_Bot possède un nouveau préfix, il s'agit désormais de `{}` au lieu de `!`.".format(config["prefix"]))
        embed_news_page_3.set_footer(text="\nDébut ⏪ | Nouveaux mots ◀️\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        #Mise en place des pages pour la commande "news"
        bot.news_pages = [page1_news, page2_news, page3_news]

        @bot.event
        async def on_ready():
            #Définition du statut
            activity = discord.Game(name="être inutile", type=1)
            await bot.change_presence(status=discord.Status.online, activity=activity)
            #Affichage d'un message lors de la mise en ligne
            print('\n\n\n                >En ligne< \n\n\n\n>>> NE SURTOUT PAS FERMER CETTE FENÊTRE ! LE BOT EST EN LIGNE UNIQUEMENT QUAND CETTE DERNIÈRE EST OUVERTE ! <<<\n\n\n®Nathoune 2022')

        
        @bot.event
        #Message privé lorsqu'un membre rejoint un serveur sur lequel il y a Le_Bot
        async def on_member_join(member):
            embed_new_member = discord.Embed(title="Salut jeune entrepeneur.", color=0xffab33)
            embed_new_member.add_field(name="""Tu as rejoins un serveur dans lequel je suis, donc attention à toi 😒. 
Non en vrai je rigole, je suis le bot qui te répond quand tu te prends des vents donc jsuis sympa un peu.
Bref, écris un petit message pour dire bonjour dans le serveur !""", value="""Le_Bot, votre bot intéracitf (https://le-bot.cf) !""")
            await member.send(embed=embed_new_member)

        @bot.event
        async def on_message(message):
            #Permet au bot de comprendre qu'il y a des commandes par la suite
            await bot.process_commands(message)
            
            #Détection de "liste.json" et réponse adéquate si un message envoyé correspond à une réponse possible
            [await message.reply(o['value']) for o in list if o['name'] == message.content.lower()]

            #Réponse du bot quand quelqu'un le mentionne
            if bot.user.mentioned_in(message):
                embed_mention = discord.Embed(title="Salut :wave:.\nJe suis **Le_Bot**, fais `{}h` pour en savoir plus sur moi et mes commandes !".format(config["prefix"]), color=0xffab33)
                await message.reply(embed=embed_mention)

        @bot.command()
        #Définition de la commande "help" dynamique
        async def h(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/h_toggle.txt', 'r') as file:
                #Lecture du fichier avec les IDs des serveurs où la commande est désactivée
                disabled_command = file.read().splitlines()

            #Récupération de l'ID du serveur actuelle
            now_id = str(ctx.message.guild.id)

            #Si l'ID du serveur actuel n'est pas dans le fichier
            if now_id not in disabled_command:
                #Début de la commande help
                #Déifnition des émojis des bouttons
                buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
                #Actuellement 0 cochés
                current = 0
                #Récupération des pages définies plus haut
                msg = await ctx.reply(embed=bot.help_pages[current])

                #Ajout des réactions au message
                for button in buttons:
                    await msg.add_reaction(button)

                #Si il le fait
                while True:
                    #Il essaye
                    try:
                        #De récupérer la réaction
                        reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user : user == ctx.author and reaction.emoji in buttons, timeout=60.0)

                    #Si le temps de 60 secondes est dépassé il enlève ses réactions
                    except asyncio.TimeoutError:
                        await msg.clear_reactions()

                    #Il change ensuite de page en fonction de la réaction ajoutée
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

            #Réponse du bot si la commande est désactivée
            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle h` pour la réactiver.".format(config["prefix"]), color=0xffab33)
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        #Définition de la commande "confidentiality"
        async def confidentiality(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/confidentiality_toggle.txt', 'r') as file:
                #Lecture du fichier avec les IDs des serveurs où la commande est désactivée
                disabled_command = file.read().splitlines()

            #Récupération de l'ID du serveur actuelle
            now_id = str(ctx.message.guild.id)

            #Si l'ID du serveur actuel n'est pas dans le fichier
            if now_id not in disabled_command:
                #Début de la commande "confidentiality"
                embed_confidentiality = discord.Embed(title="🧑‍⚖ La politique de confidentialité de Le_Bot", color=0xffab33, url="https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt")
                embed_confidentiality.add_field(name="Le lien vers la politique de confidentialité :", value="https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt")
                await ctx.reply(embed=embed_confidentiality)

            #Sinon réponse du bot si la commande est désactivée
            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle confidentiality` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        #Définition de la commande "serveur"
        async def serveur(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/serveur_toggle.txt', 'r') as file:
                #Lecture du fichier avec les IDs des serveurs où la commande est désactivée
                disabled_command = file.read().splitlines()

            #Récupération de l'ID du serveur actuelle
            now_id = str(ctx.message.guild.id)

            #Si l'ID du serveur actuel n'est pas dans le fichier
            if now_id not in disabled_command:
                #Début de la commande "serveur"
                embed_serveur = discord.Embed(title="🔥 Le serveur du créateur de **Le_Bot**.", color=0xffab33, url="https://discord.gg/b6jjy5yKXV")
                embed_serveur.add_field(name="Le lien du serveur de Nathoune :", value="https://discord.gg/b6jjy5yKXV")
                await ctx.reply(embed=embed_serveur)

            #Sinon réponse du bot si la commande est désactivée
            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle serveur` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        #Définition de la commande "news"
        async def news(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/news_toggle.txt', 'r') as file:
                #Lecture du fichier avec les IDs des serveurs où la commande est désactivée
                disabled_command = file.read().splitlines()

            #Récupération de l'ID du serveur actuelle
            now_id = str(ctx.message.guild.id)

            #Si l'ID du serveur actuel n'est pas dans le fichier
            if now_id not in disabled_command:
                #Début de la commande "news"
                #Déifnition des émojis des bouttons
                buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
                #Actuellement 0 cochés
                current = 0
                #Récupération des pages définies plus haut
                msg = await ctx.reply(embed=bot.news_pages[current])

                #Ajout des réactions au message
                for button in buttons:
                    await msg.add_reaction(button)

                #Si il le fait
                while True:
                    #Il essaye
                    try:
                        #De récupérer la réaction
                        reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user : user == ctx.author and reaction.emoji in buttons, timeout=60.0)

                    #Si le temps de 60 secondes est dépassé il enlève ses réactions
                    except asyncio.TimeoutError:
                        await msg.clear_reactions()

                    #Il change ensuite de page en fonction de la réaction ajoutée
                    else:
                        previous_page = current

                        if reaction.emoji == u"\u23EA":
                            current = 0

                        elif reaction.emoji == u"\u25C0":
                            if current > 0 :
                                current -= 1

                        elif reaction.emoji == u"\u25B6":
                            if current < len(bot.news_pages)-1:
                                current += 1

                        elif reaction.emoji == u"\u23E9":
                            current = len(bot.news_pages)-1
                        
                        for button in buttons:
                            await msg.remove_reaction(button, ctx.author)

                        if current != previous_page:
                            await msg.edit(embed=bot.news_pages[current])

            #Sinon réponse du bot si la commande est désactivée
            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle news` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                await ctx.reply(embed=embed_disabled_command)
        
        @bot.command()
        #Définition de la commande "how_work"
        async def how_work(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/how_work_toggle.txt', 'r') as file:
                #Lecture du fichier avec les IDs des serveurs où la commande est désactivée
                disabled_command = file.read().splitlines()

            #Récupération de l'ID du serveur actuelle
            now_id = str(ctx.message.guild.id)

            #Si l'ID du serveur actuel n'est pas dans le fichier
            if now_id not in disabled_command:
                #Début de la commande "how_work"
                embed_how_work = discord.Embed(title="Comment utiliser la nouvelle commande 'help' !", color=0xffab33)
                embed_how_work.set_image(url="https://i.imgur.com/m4YqCHC.gif") 
                await ctx.reply(embed=embed_how_work)

            #Sinon réponse du bot si la commande est désactivée
            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle how_work` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        #Définition de la commande "gihtub"
        async def github(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/github_toggle.txt', 'r') as file:
                #Lecture du fichier avec les IDs des serveurs où la commande est désactivée
                disabled_command = file.read().splitlines()

            #Récupération de l'ID du serveur actuelle
            now_id = str(ctx.message.guild.id)

            #Si l'ID du serveur actuel n'est pas dans le fichier
            if now_id not in disabled_command:
                #Début de la commande "github"
                embed_github = discord.Embed(title="🔗 Le_Bot est opensource et son code se trouve sur GitHub !", color=0xffab33, url="https://github.com/Nathoune-YT/le_bot")
                embed_github.add_field(name="🌍 Informations", value="Le_Bot est opensource et se trouve sur GitHub (https://github.com/Nathoune-YT/le_bot). Vous pouvez simplement regarder le script, le modifier et m'envoyer une pull request pour peut-être voir vos modifications dans le code officiel de Le_Bot ou l'utiliser et le modifier tout en suivant la procédure à lire dans le README !")
                await ctx.reply(embed=embed_github)
            
            #Sinon réponse du bot si la commande est désactivée
            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle github` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        #Définition de la commande "site"
        async def site(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/site_toggle.txt', 'r') as file:
                #Lecture du fichier avec les IDs des serveurs où la commande est désactivée
                disabled_command = file.read().splitlines()

            #Récupération de l'ID du serveur actuelle
            now_id = str(ctx.message.guild.id)

            #Si l'ID du serveur actuel n'est pas dans le fichier
            if now_id not in disabled_command:
                #Début de la commande "site"
                embed_site = discord.Embed(title="🤌 Le site web officiel de Le_Bot", color=0xffab33, url="https://le-bot.cf")
                embed_site.add_field(name="Le lien du site officiel :", value="https://le-bot.cf")
                await ctx.reply(embed=embed_site)

            #Sinon réponse du bot si la commande est désactivée
            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle site` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        #Définition de la commande "ping"
        async def ping(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/ping_toggle.txt', 'r') as file:
                #Lecture du fichier avec les IDs des serveurs où la commande est désactivée
                disabled_command = file.read().splitlines()

            #Récupération de l'ID du serveur actuelle
            now_id = str(ctx.message.guild.id)

            #Si l'ID du serveur actuel n'est pas dans le fichier
            if now_id not in disabled_command:
                #Début de la commande "ping"
                embed_ping = discord.Embed(title="Donc là je dois répondre 🤔 ?", color=0xffab33)
                embed_ping.add_field(name=f"📶 J\'ai bien reçu ton message en : `{round(bot.latency * 1000)}ms`", value=f"(je te réponds c'est le principal ok.)")
                await ctx.reply(embed=embed_ping)

            #Sinon réponse du bot si la commande est désactivée
            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle ping` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                await ctx.reply(embed=embed_disabled_command)

        #Permission administrateur pour éxécuter cette commande
        @commands.has_permissions(administrator=True)
        @bot.command()
        #Définition de la commande "toggle"
        async def toggle(ctx, command_name=None):
            #Réponse du bot si aucune commande n'est saisie après "toggle"
            if command_name == None: 
                embed_no_toggle = discord.Embed(title="Donne moi le nom de la commande à désactiver/activer comme ceci :", color=0xffab33)
                embed_no_toggle.add_field(name="`{}toggle commande`".format(config["prefix"]), value="Pour retrouvez l'ensemble des commandes, fais celle ci `{}h`.".format(config["prefix"]))
                await ctx.reply(embed=embed_no_toggle)
                return

            #Si il y en a une il essaye :
            try:
                command = bot.get_command(command_name)
                
                #Si la commande existe :
                if command.enabled :
                    
                    #Définition de l'ID du serveur actuel
                    now_id = str(ctx.message.guild.id)
                    #Ouverture du fichier contenant les ID des serveurs où la commande est désactivée
                    with open(f"./toggle/{command_name}_toggle.txt", 'r') as toggle:
                        #Lecture des lignes
                        remove = toggle.read().splitlines()

                    #Si l'ID actuelle du serveur n'est pas dans la liste il l'ajoute et donc désactive la commande
                    if now_id not in remove:
                        with open(f"./toggle/{command_name}_toggle.txt", "a") as file:
                            file.write(str(f"{now_id}\n"))
                        #Réponse du bot lors de la désactivation
                        embed_toggle_disabled = discord.Embed(title=f"❌ J'ai désactivé la commande `{command_name}`.", description="Pour la réactiver, fais `{}toggle {}`".format(config["prefix"], command_name), color=0xff0000)
                        await ctx.reply(embed=embed_toggle_disabled)
                        return

                    #Si l'ID actuelle du serveur est dans la liste, il l'a supprime et donc active la commande
                    else:
                        file = open(f'./toggle/{command_name}_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        lst = []
                        for line in file:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            lst.append(line)
                        file.close()
                        file = open(f'./toggle/{command_name}_toggle.txt','w')
                        for line in lst:
                            file.write(line)
                        file.close()
                        #Réponse du bot lors de l'activation
                        embed_toggle_enabled = discord.Embed(title=f"✅ J'ai activé la commande `{command_name}`.", description="Pour la désactiver, fais `{}toggle {}`".format(config["prefix"], command_name),color=0x00d731)
                        await ctx.reply(embed=embed_toggle_enabled)

            #Si la commande n'existe pas :
            except:
                embed_wrong_toggle = discord.Embed(title=f"C'est pas une commande valide, t'es dyslexique ou quoi ?", description="Pour activer ou désactiver des commandes, fais `{}toggle commande`. Tu retrouves l'ensembles des commandes en faisant celle ci `{}h`.".format(config["prefix"], config["prefix"]),color=0xffab33)
                await ctx.reply(embed=embed_wrong_toggle)
                return

        #Permission administrateur pour éxécuter cette commande
        @commands.has_permissions(administrator=True)
        @bot.command()
        #Définition de la commande "delete invits"
        async def delete(ctx, extension):
            try:
                #Il essaye d'activer l'extension
                bot.load_extension(f'cogs.{extension}')
                embed_toggle_enabled = discord.Embed(title="✅ A partir de maintenant, je supprimerai les invitations vers d'autre serveurs Discord.", description="Fais `{}delete invits` pour désactiver la suppression automatique des liens d'invitations Discord.".format(config["prefix"]),color=0x00d731)
                await ctx.reply(embed=embed_toggle_enabled)
            except:
                #Si elle est déjà activée, il la désactive
                bot.unload_extension(f'cogs.{extension}')
                embed_disabled_command = discord.Embed(title="❌ A partir de maintenant, je ne supprimerai plus les invitations vers d'autre serveurs Discord.", description="Fais `{}delete invits` pour réactiver la suppression automatique des liens d'invitations Discord.".format(config["prefix"]), color=0xff0000)
                await ctx.reply(embed=embed_disabled_command)

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')

        #Démarrage du bot avec le token fournit dans le fichier "config.json"
        bot.run(config["token"])

    #Si il y a un problème lors du programme
    except:
        #Il recommence la fonction "main", il n'y a donc jamais d'interruptions si le programme crash
        main()

#Lancement du bot
main()
