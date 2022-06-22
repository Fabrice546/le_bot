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

        page1 = embed1 = discord.Embed(title="⚙️ Commandes :\n", color=0xffab33)
        embed1.add_field(name="📃 {}h".format(config["prefix"]), value="`Envoyer ce message.`")
        embed1.add_field(name="📑 {}news".format(config["prefix"]), value="`Afficher les nouveautés.`", inline=False)
        embed1.add_field(name="📞 {}serveur".format(config["prefix"]), value="`Pour pouvoir rejoindre le serveur Discord.`", inline=False)
        embed1.add_field(name="🗒️ {}confidentiality".format(config["prefix"]), value="`Connaître la politique de confidentialité.`", inline=False)
        embed1.add_field(name="👌 {}site".format(config["prefix"]), value="`Le site officiel de Le_Bot`", inline=False)
        embed1.add_field(name="❓ {}how_work".format(config["prefix"]), value="`Comment fonctionne la nouvelle commande 'help'.`", inline=False)
        embed1.add_field(name="🔗 {}github".format(config["prefix"]), value="`Le_Bot sur GitHub.`", inline=False)
        embed1.set_footer(text="\n ▶️ Mots | ⏩ Fin\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        page2 = embed2 = discord.Embed(title="📋 Mots :", color=0xffab33,
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

        page3 = embed3 = Embed(title="📂 Informations :", color=0xffab33)
        embed3.add_field(name="Le_Bot, votre bot interactif !", value="▶️ Le_Bot répondra à certains de vos mots en ajoutant de l'humour et du dynamisme sur votre serveur !\n\n ▶️ Son code source se trouve sur GitHub, il est donc opensource ! Voici son lien : https://github.com/Nathoune-YT/le_bot. Vous pouvez l'améliorer ou simplement l'utiliser tout en suivant la procédure présente dans le README.\n\n ▶️ Voici la politique de confidentialité : https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt\n\n ▶️ Le site web officiel de Le_Bot : https://le-bot.cf (il prend un peu de temps à se charger chez certaines personnes)", inline=True)
        embed3.set_footer(text="\nDébut ⏪ | Mots ◀️\n\n🚨Réinvite moi pour pouvoir changer de pages : \nhttps://le-bot.cf ou clique sur le bouton bleu sur mon profil🚨")

        bot.help_pages = [page1, page2, page3]

        @bot.event
        async def on_ready():
            activity = discord.Game(name="être inutile", type=1)
            await bot.change_presence(status=discord.Status.online, activity=activity)
            print('\n\n\n                >En ligne< \n\n\n\n>>> NE SURTOUT PAS FERMER CETTE FENÊTRE ! LE BOT EST EN LIGNE UNIQUEMENT QUAND CETTE DERNIÈRE EST OUVERTE ! <<<\n\n\n®Nathoune 2022')

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
            await ctx.reply("**Voici le serveur Nathoune_Serveur Résurection** : https://discord.gg/b6jjy5yKXV")

        @bot.command()
        async def news(ctx):
            embed4 = discord.Embed(title="📈 Nouvelles commandes :", color=0xffab33)
            embed4.add_field(name="📞 {}serveur".format(config["prefix"]), value="`Pour pouvoir rejoindre le serveur Discord.`", inline=False)
            embed4.add_field(name="🗒️ {}confidentiality".format(config["prefix"]), value="`Connaître la politique de confidentialité.`", inline=False)
            embed4.add_field(name="👌 {}site".format(config["prefix"]), value="`Le site officiel de Le_Bot`", inline=False)
            embed4.add_field(name="❓ {}how_work".format(config["prefix"]), value="`Comment fonctionne la nouvelle commande 'help'.`", inline=False)
            embed4.add_field(name="🔗 {}github".format(config["prefix"]), value="`Le_Bot sur GitHub.`", inline=False)
            await ctx.reply(embed=embed4)
            embed5 = discord.Embed(title="⏏️ Nouveaux mots :", color=0xffab33, description="""`
🟡 Feur            🟡 RAM    
🟡 Paypal          🟡 GPU   
🟡 Nyan Cat        🟡 CPU   
`""")
            await ctx.reply(embed=embed5)
        
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
            embed7 = discord.Embed(title="🤌 Le site web officiel de Le_Bot", color=0xffab33, url="https://le-bot.cf")
            embed7.add_field(name="Le lien du site officiel :", value="https://le-bot.cf")
            await ctx.reply(embed=embed7)

        bot.run(config["token"])

    except:
        main()
main()
