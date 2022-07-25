import discord
import json
from discord import Embed
from discord.ext import commands
import time
from os import system
from discord_components import *
from colorama import Fore, init, Style
from datetime import datetime
import psutil

system("title " + "Le_Bot par Nathoune#3630")
system('mode con: cols=72 lines=23')

with open('./config.json', 'r', encoding='utf-8') as config_bot:
    config = json.load(config_bot)

with open('./liste.json', 'r', encoding='utf-8') as list_words:
    list = json.load(list_words)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix= config["prefix"], help_command=None, news_pages=None, intents = intents)

#Définition de la date de connexion
bot.launch_time = datetime.utcnow()

#Définition pour les boutons
DiscordComponents(bot)

#Définition pour Colorama
init(convert=True)

def main():
    try:
        #Affichage d'une "interface"
        print(Fore.LIGHTRED_EX + r"""
     ___       _______           ________  ________  _________   
    |\  \     |\  ___ \         |\   __  \|\   __  \|\___   ___\ 
    \ \  \    \ \   __/|        \ \  \|\ /\ \  \|\  \|___ \  \_| 
     \ \  \    \ \  \_|/__       \ \   __  \ \  \\\  \   \ \  \  
      \ \  \____\ \  \_|\ \ ______\ \  \|\  \ \  \\\  \   \ \  \ 
       \ \_______\ \_______\ ______\_\_______\ \_______\   \ \__\
        \|_______|\|_______||_______|\|_______|\|_______|    \|__|
    

                           Nathoune#3630
""")
        
        print(Fore.LIGHTBLACK_EX + """\n\n           Mise en ligne, veuiller patientez un instant.\n""")

        @bot.event
        async def on_ready():
            #Définition du statut
            activity = discord.Game(name="être inutile", type=1)
            await bot.change_presence(status=discord.Status.online, activity=activity)
            print(f"""
                            {Fore.LIGHTGREEN_EX}En ligne
\n\n      {Fore.LIGHTBLACK_EX}Lors de la fermeture de la fenêtre, le bot sera {Fore.LIGHTRED_EX}hors-ligne.""")

        @bot.event
        async def on_member_join(member):
            embed_new_member = discord.Embed(title="Salut jeune entrepeneur.", color=0xffab33)
            embed_new_member.add_field(name="""Tu as rejoins un serveur dans lequel je suis, donc attention à toi 😒. 
Non en vrai je rigole, je suis le bot qui te répond quand tu te prends des vents donc jsuis sympa un peu.
Bref, écris un petit message pour dire bonjour dans le serveur !""", value="""Le_Bot, votre bot intéracitf (https://le-bot.cf) !""")
            await member.send(embed=embed_new_member)

        @bot.event
        async def on_message(message):
            #Pour que les commandes soient prises en compte
            await bot.process_commands(message)
        
            #Réponse du bot aux mots définit
            [await message.reply(word['value']) for word in list if word['name'] == message.content.lower()]

            if bot.user.mentioned_in(message):
                embed_mention = discord.Embed(title="Salut :wave:.\nJe suis **Le_Bot**, fais `{}h` pour en savoir plus sur moi et mes commandes !".format(config["prefix"]), color=0xffab33)
                embed_mention.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await message.reply(embed=embed_mention)

            invites_discord_links = [
            ".gg",
            ".invite"
            ]

            if any(word in message.content.lower() for word in invites_discord_links):
                if message.author.guild_permissions.administrator :
                    pass
                else :
                    await message.delete()
                    embed_delete_invites = discord.Embed(title = f"Fais pas ta pub :rat:", description=f"Un certain `{message.author}` a envoyé un lien d'invitation vers un autre serveur Discord :rat:. Heureusement que je suis la pour supprimer 😒",color=0xffab33)
                    embed_delete_invites.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                    await message.channel.send(embed = embed_delete_invites)

        @bot.command()
        async def h(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/h_toggle.txt', 'r') as h_toggle_file:
                disabled_command = h_toggle_file.read().splitlines()

            now_id = str(ctx.message.guild.id)

            if now_id not in disabled_command:
                try :
                    embed_menu_help = discord.Embed(title = "🤖 Option à choisir :", description="Une fois l'option choisie, un nouveau message sera envoyé !", color=0xffab33)
                    await ctx.reply(
                        embed=embed_menu_help,
                        #Envoie du menu interactif
                        components = [
                            Select(
                                placeholder = "Choisis une option",
                                options = [
                                    SelectOption(label = "⚙️ Commandes", value = "⚙️ Commandes"),
                                    SelectOption(label = "📋 Mots", value = "📋 Mots"),
                                    SelectOption(label = "📂 Informations", value = "📂 Informations")])])

                    embed_help_page_1 = discord.Embed(title="⚙️ Commandes :\n", color=0xffab33)
                    embed_help_page_1.add_field(name="Commandes avec menus :", value="** **", inline=False)
                    embed_help_page_1.add_field(name="📃 {}h".format(config["prefix"]), value="`Envoie le menu de selection.`", inline=True)
                    embed_help_page_1.add_field(name="📑 {}news".format(config["prefix"]), value="`Affiche les nouveautés.`", inline=True)
                    embed_help_page_1.add_field(name="Commandes avec liens :", value="** **", inline=False)
                    embed_help_page_1.add_field(name="📞 {}server".format(config["prefix"]), value="`Envoie le serveur Discord du créateur de Le_Bot.`", inline=True)
                    embed_help_page_1.add_field(name="🗒️ {}privacy".format(config["prefix"]), value="`Connaître la politique de confidentialité.`", inline=True)
                    embed_help_page_1.add_field(name="👌 {}site".format(config["prefix"]), value="`Le site officiel de Le_Bot.`", inline=True)
                    embed_help_page_1.add_field(name="🔗 {}github".format(config["prefix"]), value="`Le_Bot sur GitHub.`", inline=True)
                    embed_help_page_1.add_field(name="Commandes avec statistiques :", value="** **", inline=False)
                    embed_help_page_1.add_field(name="📶 {}ping".format(config["prefix"]), value="`Tester la vitesse de réception de message.`", inline=True)
                    embed_help_page_1.add_field(name="📊 {}stats".format(config["prefix"]), value="`Toutes les statistiques relatives au bot.`", inline=True)
                    embed_help_page_1.add_field(name="Commande pour activer ou en désactiver d'autres :", value="** **", inline=False)
                    embed_help_page_1.add_field(name="⚖️ {}toggle".format(config["prefix"]), value="`Permet de désactiver ou activer les commandes. 🟠`", inline=True)
                    embed_help_page_1.add_field(name="`🟠 : Requiert les permissions administrateur.`", value="** **", inline=False)
                    embed_help_page_1.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')

                    embed_help_page_2 = discord.Embed(title="📋 Mots :", color=0xffab33,
                    description="""`🟡 Salut              🟡 Le bot est éclaté    🟡 Lol
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
🟡 Nitro              🟡 Hébergeur            🟡 France
🟡 Snapchat           🟡 Instagram            🟡 Baka`""", inline=False)
                    embed_help_page_2.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')

                    embed_help_page_3 = Embed(title="📂 Informations :", color=0xffab33)
                    embed_help_page_3.add_field(name="Le_Bot, votre bot interactif !", value="""▶️ Le_Bot répondra à certains de vos mots en ajoutant de l'humour et du dynamisme sur votre serveur !

▶️ Son code source se trouve sur GitHub, il est donc opensource ! Voici son lien : https://github.com/Nathoune-YT/le_bot. Vous pouvez l'améliorer ou simplement l'utiliser tout en suivant la procédure présente dans le README.

▶️ Voici la politique de confidentialité : https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt

▶️ Le site web officiel de Le_Bot : https://le-bot.cf (il prend un peu de temps à se charger chez certaines personnes.)

▶️ Son préfix est `{}`.

▶️ Il supprimera automatiquement les liens d'invitation vers d'autres serveurs Discord excepté pour les administrateurs.

▶️ Pour toutes questions, veuillez contacter le créateur de Le_Bot : \n`nathoune@le-bot.cf` par mail ou `Nathoune#3630` sur Discord.""".format(config["prefix"]), inline=True)
                    embed_help_page_3.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')

                    while True:
                        #En attente d'un choix
                        interaction = await bot.wait_for("select_option")
                        if interaction.values[0] == '⚙️ Commandes':
                            await interaction.send(embed= embed_help_page_1, ephemeral=False)

                        if interaction.values[0] == '📋 Mots':
                            await interaction.send(embed= embed_help_page_2, ephemeral=False)

                        if interaction.values[0] == '📂 Informations':
                            await interaction.send(embed = embed_help_page_3, ephemeral=False)

                #Pour éviter les erreurs inutiles dans la console
                except:
                    time.sleep(0.1) 

            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle h` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        async def news(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/news_toggle.txt', 'r') as news_toggle_file:
                disabled_command = news_toggle_file.read().splitlines()

            now_id = str(ctx.message.guild.id)

            if now_id not in disabled_command:
                try :
                    embed_menu_news = discord.Embed(title = "🤖 Option à choisir :", description="Une fois l'option choisie, un nouveau message sera envoyé !", color=0xffab33)
                    await ctx.reply(
                        embed=embed_menu_news,
                        #Envoie du menu interactif
                        components = [
                            Select(
                                placeholder = "Choisis une option",
                                options = [
                                    SelectOption(label = "📈 Nouvelles commandes", value = "📈 Nouvelles commandes"),
                                    SelectOption(label = "⏏️ Nouveaux mots", value = "⏏️ Nouveaux mots"),
                                    SelectOption(label = "🤟 Nouveau préfix", value = "🤟 Nouveau préfix")])])

                    embed_news_page_1 = discord.Embed(title="📈 Nouvelles commandes :", color=0xffab33)
                    embed_news_page_1.add_field(name="Commandes avec statistiques :", value="** **", inline=False)
                    embed_news_page_1.add_field(name="📶 {}ping".format(config["prefix"]), value="`Tester la vitesse de réception de message. `", inline=True)
                    embed_news_page_1.add_field(name="📊 {}stats".format(config["prefix"]), value="`Toutes les statistiques relatives au bot.`", inline=True)
                    embed_news_page_1.add_field(name="Commande pour activer ou en désactiver d'autres :", value="** **", inline=False)
                    embed_news_page_1.add_field(name="⚖️ {}toggle".format(config["prefix"]), value="`Permet de désactiver ou activer les commandes. 🟠`", inline=True)
                    embed_news_page_1.add_field(name="`🟠 : Requiert les permissions administrateur.`", value="** **")
                    embed_news_page_1.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')

                    embed_news_page_2 = discord.Embed(title="⏏️ Nouveaux mots :", color=0xffab33, description="""`🟡 Baka            🟡 Nitro
🟡 France          🟡 Hébergeur
🟡 Snaptchat       🟡 Instagram`""")
                    embed_news_page_2.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')

                    embed_news_page_3 = discord.Embed(title="🤟 Nouveau préfix !", color=0xffab33, description="Le_Bot possède un nouveau préfix, il s'agit désormais de `{}` au lieu de `!`.".format(config["prefix"]))
                    embed_news_page_3.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')

                    while True:
                        #En attente d'un choix
                        interaction = await bot.wait_for("select_option")
                        if interaction.values[0] == '📈 Nouvelles commandes':
                            await interaction.send(embed = embed_news_page_1, ephemeral=False)

                        if interaction.values[0] == '⏏️ Nouveaux mots':
                            await interaction.send(embed = embed_news_page_2, ephemeral=False)

                        if interaction.values[0] == '🤟 Nouveau préfix':
                            await interaction.send(embed = embed_news_page_3, ephemeral=False)

                #Pour éviter les erreurs inutiles dans la console
                except:
                    time.sleep(0.1)

            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle news` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        async def privacy(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/privacy_toggle.txt', 'r') as privacy_toggle_file:
                disabled_command = privacy_toggle_file.read().splitlines()

            now_id = str(ctx.message.guild.id)

            if now_id not in disabled_command:
                embed_privacy = discord.Embed(title="🧑‍⚖ La politique de confidentialité de Le_Bot", color=0xffab33, url="https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt")
                embed_privacy.add_field(name="Le lien vers la politique de confidentialité :", value="https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt")
                embed_privacy.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_privacy, components = [
                Button(label = "🧑‍⚖ Lien", style=5, url="https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt")])

            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle privacy` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        async def server(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/server_toggle.txt', 'r') as server_toggle_file:
                disabled_command = server_toggle_file.read().splitlines()

            now_id = str(ctx.message.guild.id)

            if now_id not in disabled_command:
                embed_server = discord.Embed(title="🔥 Le serveur du créateur de **Le_Bot**.", color=0xffab33, url="https://discord.gg/b6jjy5yKXV")
                embed_server.add_field(name="Le lien du serveur de Nathoune :", value="https://discord.gg/b6jjy5yKXV")
                embed_server.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_server, components = [
                Button(label = "📞 Lien", style=5, url="https://discord.gg/b6jjy5yKXV")])

            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle serveur` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        async def github(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/github_toggle.txt', 'r') as github_toggle_file:
                disabled_command = github_toggle_file.read().splitlines()

            now_id = str(ctx.message.guild.id)

            if now_id not in disabled_command:
                embed_github = discord.Embed(title="🔗 Le_Bot est opensource et son code se trouve sur GitHub !", color=0xffab33, url="https://github.com/Nathoune-YT/le_bot")
                embed_github.add_field(name="🌍 Informations", value="Le_Bot est opensource et se trouve sur GitHub (https://github.com/Nathoune-YT/le_bot). Vous pouvez simplement regarder le script, le modifier et m'envoyer une pull request pour peut-être voir vos modifications dans le code officiel de Le_Bot ou l'utiliser et le modifier tout en suivant la procédure à lire dans le README !")
                embed_github.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_github, components = [
                Button(label = "🔗 Lien", style=5, url="https://github.com/Nathoune-YT/le_bot")])

            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle github` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        async def site(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/site_toggle.txt', 'r') as site_toggle_file:
                disabled_command = site_toggle_file.read().splitlines()

            now_id = str(ctx.message.guild.id)

            if now_id not in disabled_command:
                embed_site = discord.Embed(title="🤌 Le site web officiel de Le_Bot", color=0xffab33, url="https://le-bot.cf")
                embed_site.add_field(name="Le lien du site officiel :", value="https://le-bot.cf")
                embed_site.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_site, components = [
                Button(label = "🤌 Lien", style=5, url="https://le-bot.cf")])

            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle site` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        async def ping(ctx):
            #Savoir si la commande est activée ou désactivée
            with open('./toggle/ping_toggle.txt', 'r') as ping_toggle_file:
                disabled_command = ping_toggle_file.read().splitlines()

            now_id = str(ctx.message.guild.id)

            if now_id not in disabled_command:
                embed_ping = discord.Embed(title="Donc là je dois répondre 🤔 ?", color=0xffab33)
                embed_ping.add_field(name=f"🏓 J\'ai bien reçu ton message en : `{round(bot.latency * 1000)}ms`", value=f"(je te réponds c'est le principal ok.)")
                embed_ping.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_ping)

            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle ping` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_disabled_command)

        @bot.command()
        async def stats(ctx):
            #Définition de la date en jours, heures, minutes en secondes pour l'uptime
            delta_uptime = datetime.utcnow() - bot.launch_time
            hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            days, hours = divmod(hours, 24)

            #Savoir si la commande est activée ou désactivée
            with open('./toggle/stats_toggle.txt', 'r') as stats_toggle_file:
                disabled_command = stats_toggle_file.read().splitlines()

            now_id = str(ctx.message.guild.id)

            if now_id not in disabled_command:
                embed_stats = Embed(title="📊 Statistiques", description="Voici toutes les statistiques :", color=0xffab33)
                embed_stats.add_field(name="📈 Serveurs :", value=f"`{len(bot.guilds)}`", inline = False)
                embed_stats.add_field(name="🏓 Ping :", value=f"`{round(bot.latency * 1000)}ms`", inline = False)
                embed_stats.add_field(name="⌛ Connecté depuis :", value=f"`{days}j, {hours}h, {minutes}m, {seconds}s`", inline = False)
                #Entre "<t:" et ":R>", entrez le temps en UNIX
                embed_stats.add_field(name="⏲️ Dernières modifications :", value="<t:UNIX:R>", inline = False)
                embed_stats.add_field(name="🚀 Utilisation RAM :", value=f"`{psutil.virtual_memory().percent}%`", inline = False)
                embed_stats.add_field(name="🧰 Utilisation CPU :", value=f"`{psutil.cpu_percent()}%`", inline = False)
                embed_stats.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.send(embed=embed_stats, components = [
                Button(label = "✏️ Changelog", style=5, url="https://github.com/Nathoune-YT/le_bot/commits/main")])

            else :
                embed_disabled_command = discord.Embed(title="🚫 La commande est désactivée.", description="Fais `{}toggle ping` pour la réactiver.".format(config["prefix"]), color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_disabled_command)

        @commands.has_permissions(administrator=True)
        @bot.command()
        async def toggle(ctx, command_name=None):
            if command_name == None: 
                embed_no_toggle = discord.Embed(title="Donne moi le nom de la commande à désactiver/activer comme ceci :", color=0xffab33)
                embed_no_toggle.add_field(name="`{}toggle commande`".format(config["prefix"]), value="** **")
                embed_no_toggle.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_no_toggle)
                return

            try:
                command = bot.get_command(command_name)
                
                if command.enabled :
                    now_id = str(ctx.message.guild.id)
                    with open(f"./toggle/{command_name}_toggle.txt", 'r') as check_id:
                        id_file = check_id.read().splitlines()

                    if now_id not in id_file:
                        with open(f"./toggle/{command_name}_toggle.txt", "a") as disabled_command:
                            disabled_command.write(str(f"{now_id}\n"))
                        embed_toggle_disabled = discord.Embed(title=f"❌ J'ai désactivé la commande `{command_name}`.", description="Pour la réactiver, fais `{}toggle {}`".format(config["prefix"], command_name), color=0xff0000)
                        embed_toggle_disabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await ctx.reply(embed=embed_toggle_disabled)
                        return

                    else:
                        enabled_command= open(f'./toggle/{command_name}_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        id_server = []
                        for line in enabled_command:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            id_server.append(line)
                        enabled_command.close()
                        enabled_command = open(f'./toggle/{command_name}_toggle.txt','w')
                        for line in id_server:
                            enabled_command.write(line)
                        enabled_command.close()
                        embed_toggle_enabled = discord.Embed(title=f"✅ J'ai activé la commande `{command_name}`.", description="Pour la désactiver, fais `{}toggle {}`".format(config["prefix"], command_name),color=0x00d731)
                        embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await ctx.reply(embed=embed_toggle_enabled)

            except:
                embed_wrong_toggle = discord.Embed(title=f"C'est pas une commande valide, t'es dyslexique ou quoi ?", description="Pour activer ou désactiver des commandes, fais `{}toggle commande`. Tu retrouves l'ensembles des commandes en faisant celle ci `{}h`.".format(config["prefix"], config["prefix"]),color=0xffab33)
                embed_wrong_toggle.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await ctx.reply(embed=embed_wrong_toggle)
                return

        bot.run(config["token"])

    except:
        main()
main()
