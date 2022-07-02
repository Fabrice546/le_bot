import asyncio
from inspect import Traceback
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

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= config["prefix"], help_command=None, news_pages=None, intents = intents)

def main():
    try:
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
        
        message = "Mise en ligne, veuiller patientez un instant.\n\nMise en ligne . . . ."

        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)

        page1_h = embed1 = discord.Embed(title="⚙️ Commandes :\n", color=0xffab33)
        embed1.add_field(name="📃 {}h".format(config["prefix"]), value="`Envoyer ce message.`")
        embed1.add_field(name="📑 {}news".format(config["prefix"]), value="`Afficher les nouveautés.`", inline=False)
        embed1.add_field(name="📞 {}serveur".format(config["prefix"]), value="`Pour pouvoir rejoindre le serveur Discord.`", inline=False)
        embed1.add_field(name="🗒️ {}confidentiality".format(config["prefix"]), value="`Connaître la politique de confidentialité.`", inline=False)
        embed1.add_field(name="👌 {}site".format(config["prefix"]), value="`Le site officiel de Le_Bot`", inline=False)
        embed1.add_field(name="❓ {}how_work".format(config["prefix"]), value="`Comment fonctionne la nouvelle commande 'help'.`", inline=False)
        embed1.add_field(name="🔗 {}github".format(config["prefix"]), value="`Le_Bot sur GitHub.`", inline=False)
        embed1.add_field(name="📶 {}ping".format(config["prefix"]), value="`Tester la vitesse de réception de message.`", inline=False)
        embed1.set_footer(text="\n ▶️ Mots | ⏩ Fin\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        page2_h = embed2 = discord.Embed(title="📋 Mots :", color=0xffab33,
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
        embed2.set_footer(text="\nDébut ⏪ | Commandes ◀️ | ▶️ Informations | ⏩ Fin\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.gq ou clique sur le bouton bleu sur mon profil🚨")

        page3_h = embed3 = Embed(title="📂 Informations :", color=0xffab33)
        embed3.add_field(name="Le_Bot, votre bot interactif !", value="""▶️ Le_Bot répondra à certains de vos mots en ajoutant de l'humour et du dynamisme sur votre serveur !

▶️ Son code source se trouve sur GitHub, il est donc opensource ! Voici son lien : https://github.com/Nathoune-YT/le_bot. Vous pouvez l'améliorer ou simplement l'utiliser tout en suivant la procédure présente dans le README.

▶️ Voici la politique de confidentialité : https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt

▶️ Le site web officiel de Le_Bot : https://le-bot.cf (il prend un peu de temps à se charger chez certaines personnes)

▶️ Le prefix de Le_Bot change ! Il s'agit désormais de `{}` au lieu de `!`

▶️ Pour toutes questions, veuillez contacter le créateur de Le_Bot : `nathouneyoutube@hotmail.com` par mail ou `Nathoune#3630` sur Discord.""".format(config["prefix"]), inline=True)


        embed3.set_footer(text="\nDébut ⏪ | Mots ◀️\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        bot.help_pages = [page1_h, page2_h, page3_h]

        page1_news = embed4 = discord.Embed(title="📈 Nouvelles commandes :", color=0xffab33)
        embed4.add_field(name="👌 {}site".format(config["prefix"]), value="`Le site officiel de Le_Bot`", inline=False)
        embed4.add_field(name="❓ {}how_work".format(config["prefix"]), value="`Comment fonctionne la nouvelle commande 'help'.`", inline=False)
        embed4.add_field(name="🔗 {}github".format(config["prefix"]), value="`Le_Bot sur GitHub.`", inline=False)
        embed4.add_field(name="📶 {}ping".format(config["prefix"]), value="`Tester la vitesse de réception de message.`", inline=False)
        embed4.set_footer(text="\n ▶️ Nouveaux mots | ⏩ Fin\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        page2_news = embed4 = discord.Embed(title="⏏️ Nouveaux mots :", color=0xffab33, description="""`
🟡 Feur            🟡 RAM    
🟡 Paypal          🟡 GPU   
🟡 Nyan Cat        🟡 CPU   
`""")
        embed4.set_footer(text="\n Début ⏪ | Nouvelles commandes ◀️ | ▶️ Nouveau préfix | ⏩ Fin\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        page3_news = embed4 = discord.Embed(title="🤟 Nouveau préfix !", color=0xffab33, description="Le_Bot possède un nouveau préfix, il s'agit désormais de `{}` au lieu de `!`.".format(config["prefix"]))
        embed4.set_footer(text="\nDébut ⏪ | Nouveaux mots ◀️\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        bot.news_pages = [page1_news, page2_news, page3_news]

        @bot.event
        async def on_ready():
            activity = discord.Game(name="être inutile", type=1)
            await bot.change_presence(status=discord.Status.online, activity=activity)
            print('\n\n\n                >En ligne< \n\n\n\n>>> NE SURTOUT PAS FERMER CETTE FENÊTRE ! LE BOT EST EN LIGNE UNIQUEMENT QUAND CETTE DERNIÈRE EST OUVERTE ! <<<\n\n\n®Nathoune 2022')

        
        @bot.event
        async def on_member_join(member):
            await member.send("https://tenor.com/view/hey-beautiful-blow-kiss-wave-smile-gif-16278801")
            embed10 = discord.Embed(title="Salut jeune entrepeneur.", color=0xffab33)
            embed10.add_field(name="""Tu as rejoins un serveur dans lequel je suis, donc attention à toi 😒. 
Non en vrai je rigole, je suis le bot qui te répond quand tu te prends des vents donc jsuis sympa un peu.
Bref, écris un petit message pour dire bonjour dans le serveur !""", value="""Le_Bot, votre bot intéracitf (https://le-bot.cf) !""")
            await member.send(embed=embed10)

        @bot.event
        async def on_message(message):
            await bot.process_commands(message)
            
            [await message.reply(o['value']) for o in list if o['name'] == message.content.lower()]

        @bot.command()
        async def h(ctx):
            buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
            current = 0
            msg = await ctx.reply(embed=bot.help_pages[current])

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
            await ctx.reply("**Voici la politique de condfidentialité de Le_Bot** : https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt")

        @bot.command()
        async def serveur(ctx):
            embed11 = discord.Embed(title="🔥 Le serveur du créateur de **Le_Bot**.", color=0xffab33, url="https://discord.gg/b6jjy5yKXV")
            embed11.add_field(name="Le lien du serveur de Nathoune :", value="https://discord.gg/b6jjy5yKXV")
            await ctx.reply(embed=embed11)

        @bot.command()
        async def news(ctx):
            buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
            current = 0
            msg = await ctx.reply(embed=bot.news_pages[current])

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
                        if current < len(bot.news_pages)-1:
                            current += 1

                    elif reaction.emoji == u"\u23E9":
                        current = len(bot.news_pages)-1
                    
                    for button in buttons:
                        await msg.remove_reaction(button, ctx.author)

                    if current != previous_page:
                        await msg.edit(embed=bot.news_pages[current])
        
        @bot.command()
        async def how_work(ctx):
            embed6 = discord.Embed(title="Comment utiliser la nouvelle commande 'help' !", color=0xffab33)
            embed6.set_image(url="https://i.imgur.com/m4YqCHC.gif") 
            await ctx.reply(embed=embed6)

        @bot.command()
        async def github(ctx):
            embed7 = discord.Embed(title="🔗 Le_Bot est opensource et son code se trouve sur GitHub !", color=0xffab33, url="https://github.com/Nathoune-YT/le_bot")
            embed7.add_field(name="🌍 Informations", value="Le_Bot est opensource et se trouve sur GitHub (https://github.com/Nathoune-YT/le_bot). Vous pouvez simplement regarder le script, le modifier et m'envoyer une pull request pour peut-être voir vos modifications dans le code officiel de Le_Bot ou l'utiliser et le modifier tout en suivant la procédure à lire dans le README !")
            await ctx.reply(embed=embed7)

        @bot.command()
        async def site(ctx):
            embed8 = discord.Embed(title="🤌 Le site web officiel de Le_Bot", color=0xffab33, url="https://le-bot.cf")
            embed8.add_field(name="Le lien du site officiel :", value="https://le-bot.cf")
            await ctx.reply(embed=embed8)

        @bot.command()
        async def ping(ctx):
            embed9 = discord.Embed(title="Donc là je dois répondre 🤔 ?", color=0xffab33)
            embed9.add_field(name=f"📶 J\'ai bien reçu ton message en : `{round(bot.latency * 1000)}ms`", value=f"(je te réponds c'est le principal ok.)")
            await ctx.reply(embed=embed9)

        bot.run(config["token"])

    except:
        main()
main()
