import discord
from discord import Embed, app_commands
from discord.ext import commands
import json
from datetime import datetime
import psutil
from os import system
from discord.ext.commands import CommandNotFound
from colorama import Fore, init
from discord.ui import Button, View, Select
from typing import Literal
import random

system("title " + "Le_Bot / Nathoune#3630")
system('mode con: cols=102 lines=30')

with open('./config.json', 'r', encoding='utf-8') as config_bot:
    config = json.load(config_bot)

with open('./liste.json', 'r', encoding='utf-8') as list_words:
    list = json.load(list_words)

with open('./fun_links.json', 'r', encoding='utf-8') as fun_links_json:
    fun_links = json.load(fun_links_json)

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
        print(Fore.LIGHTBLACK_EX + f"""\n\n                         Mise en ligne, veuiller patientez un instant.\n{Fore.RESET}""")

        class LeBot(commands.Bot):
            async def on_ready(self):
                #Syncronisation des commandes slash pour tous les serveurs
                await self.tree.sync()
                #Définition du statut
                await bot.change_presence(status=discord.Status.idle, activity = discord.Game(name="être inutile"))
                print(f"""
                                                {Fore.LIGHTGREEN_EX}En ligne
        \n\n                   {Fore.LIGHTBLACK_EX}Lors de la fermeture de la fenêtre, le bot sera {Fore.LIGHTRED_EX}hors-ligne.
        \n{Fore.LIGHTBLACK_EX}Informations (exemple : erreurs, infos discord.py): \n{Fore.RESET}""")

            async def on_message(self, message):
                #Pour que les commandes soient prises en compte
                await bot.process_commands(message)
                    
                #Réponse du bot aux mots définit
                [await message.reply(word['value']) for word in list if word['name'] == message.content.lower()]

                if message.content == f"<@{bot.user.id}>":
                    embed_mention = discord.Embed(title=f"Salut :wave:, je suis Le_Bot.", description="Fais `/help` pour en savoir plus sur moi et mes commandes !", color=0xffab33)
                    embed_mention.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                    await message.reply(embed=embed_mention)

                invites_discord_links = [".gg", ".invite"]

                if any(word in message.content.lower() for word in invites_discord_links):
                    if message.author.guild_permissions.administrator :
                        pass
                    else :
                        await message.delete()
                        embed_delete_invites = discord.Embed(title = "Fais pas ta pub :rat:", description=f"Un certain `{message.author}` a envoyé un lien d'invitation vers un autre serveur Discord :rat:. Heureusement que je suis la pour supprimer 😒", color=0xffab33)
                        embed_delete_invites.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await message.channel.send(embed = embed_delete_invites)

            async def on_member_join(self, member):
                try:
                    embed_new_member = discord.Embed(title="Salut jeune entrepeneur 🤙.", color=0xffab33)
                    embed_new_member.add_field(name="""Tu as rejoins un serveur dans lequel je suis, donc attention à toi 😒. 
Nan en vrai je suis pas méchant mdr. Je réponds à certains de tes messages (donc je t'évite des vents des fois).
Voilà ! Tu peux dire bonjour sur le serveur !""", value="Fais `/help` ou mentionne moi pour mieux me connaître.")
                    embed_new_member.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                    await member.send(embed=embed_new_member)
                except:
                    pass

            async def on_command_error(self, ctx, error):
                #Réponse pour indiqué le passage aux commandes slash
                if isinstance(error, CommandNotFound):
                    button_invite = Button(label="Réinvitation", style=discord.ButtonStyle.link, emoji="🔗", url="https://discord.com/api/oauth2/authorize?client_id=881098458482753586&permissions=26624&scope=bot%20applications.commands")
                    view_invite = View()
                    view_invite.add_item(button_invite)
                    embed_cmd_not_found = discord.Embed(title = "<:support_commands:1004319969019973642> | Je suis passé aux commandes slash !", color=0xffab33)
                    embed_cmd_not_found.add_field(name="Réinvite moi avec ce bouton ou clique sur le bouton bleu sur mon profil pour avoir accès aux commandes slash !", value="Fais ensuite `/help` pour connaître toutes les commandes.")
                    embed_cmd_not_found.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                    await ctx.reply(embed = embed_cmd_not_found, view=view_invite)

        #Définition des intents
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        bot = LeBot(command_prefix= config["prefix"], help_command=None, news_pages=None, intents = intents)

        bot.launch_time = datetime.utcnow()

        @bot.tree.command(name="help", description="Choisis une option pour mieux connaître Le_Bot.")
        async def self(interaction: discord.Interaction, option: Literal["⚙️ | Commandes", "📋 | Mots", "📂 | Informations"]=None):
            with open('./toggle/help_toggle.txt', 'r') as help_toggle_file:
                disabled_command = help_toggle_file.read().splitlines()

            now_id = str(interaction.guild.id)

            if now_id not in disabled_command:
                #Page 1
                embed_help_page_1 = discord.Embed(title="⚙️ | Commandes :\n", color=0xffab33)
                embed_help_page_1.add_field(name="Commandes avec menus :", value="** **", inline=False)
                embed_help_page_1.add_field(name="<:menu1:1003035563970003035> | /help", value="`Envoie le menu de selection.`", inline=True)
                embed_help_page_1.add_field(name="<:menu2:1003236078473461790> | /news", value="`Affiche les nouveautés.`", inline=True)
                embed_help_page_1.add_field(name="Commandes avec liens :", value="** **", inline=False)
                embed_help_page_1.add_field(name="<:discord:1003035559205286008> | /server", value="`Envoie le serveur Discord du créateur de Le_Bot.`", inline=True)
                embed_help_page_1.add_field(name="<:privacy:1003035566763409438> | /privacy", value="`Connaître la politique de confidentialité.`", inline=True)
                embed_help_page_1.add_field(name="🌐 | /site", value="`Le site officiel de Le_Bot.`", inline=True)
                embed_help_page_1.add_field(name="<:github:1003035561453432934> | /github", value="`Le_Bot sur GitHub.`", inline=True)
                embed_help_page_1.add_field(name="Commandes avec statistiques :", value="** **", inline=False)
                embed_help_page_1.add_field(name="📶 | /ping", value="`Tester la latence du bot.`", inline=True)
                embed_help_page_1.add_field(name="📊 | /stats", value="`Toutes les statistiques relatives au bot.`", inline=True)
                embed_help_page_1.add_field(name="Autres commandes :", value="** **", inline=False)
                embed_help_page_1.add_field(name="😂 | /fun", value="`Envoie une vidéo, un meme ou une blague pas drôle.`", inline=True)
                embed_help_page_1.add_field(name="<:toggle:1003035571251326976> | /toggle", value="`Permet de désactiver ou activer les commandes.` <:admin:1003035554721566740>", inline=True)
                embed_help_page_1.add_field(name="<:admin:1003035554721566740>` : Requiert les permissions administrateur.`", value="** **", inline=False)
                embed_help_page_1.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                
                #Page 2
                embed_help_page_2 = discord.Embed(title="📋 | Mots :", color=0xffab33,
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
🟡 Snapchat           🟡 Instagram            🟡 Baka`""")
                embed_help_page_2.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')

                #Page 3
                embed_help_page_3 = Embed(title="📂 | Informations :", color=0xffab33)
                embed_help_page_3.add_field(name="Le_Bot, votre bot interactif !", value="""▶️ Le_Bot répondra à certains de vos mots en ajoutant de l'humour et du dynamisme sur votre serveur !

▶️ Son code source se trouve sur GitHub, il est donc opensource ! Voici son lien : https://github.com/Nathoune-YT/le_bot. Vous pouvez l'améliorer ou simplement l'utiliser tout en suivant la procédure présente dans le README.

▶️ Voici la politique de confidentialité : https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt

▶️ Le site web officiel de Le_Bot : https://le-bot.cf (il prend un peu de temps à se charger chez certaines personnes.)

▶️ Il supprimera automatiquement les liens d'invitation vers d'autres serveurs Discord excepté pour les administrateurs.7

▶️ Le_Bot passe aux **commandes slash** !

▶️ Pour toutes questions, veuillez contacter le créateur de Le_Bot : \n`nathoune@le-bot.cf` par mail ou `Nathoune#3630` sur Discord.""", inline=True)
                embed_help_page_3.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')

                if option == "⚙️ | Commandes":
                    await interaction.response.send_message(embed=embed_help_page_1)

                elif option == "📋 | Mots":
                    await interaction.response.send_message(embed=embed_help_page_2)

                elif option == "📂 | Informations":
                    await interaction.response.send_message(embed=embed_help_page_3)

                #Définition d'un menu si aucune option est choisie
                elif option == None:
                    select_menu_help = Select(
                        placeholder="Choisis une option",
                        options=[
                            discord.SelectOption(label="Commandes", emoji="⚙️", description="Affiche les commandes."),
                            discord.SelectOption(label="Mots", emoji="📋", description="Affiche les mots."),
                            discord.SelectOption(label="Informations", emoji="📂", description="Affiche les informations.")])
                    view_menu_help = View()
                    view_menu_help.add_item(select_menu_help)

                    async def menu_help_callback(interaction):
                        if select_menu_help.values[0] == "Commandes":
                            await interaction.response.edit_message(embed=embed_help_page_1)
                        if select_menu_help.values[0] == "Mots":
                            await interaction.response.edit_message(embed=embed_help_page_2)
                        if select_menu_help.values[0] == "Informations":
                            await interaction.response.edit_message(embed=embed_help_page_3)

                    select_menu_help.callback = menu_help_callback    
                    embed_menu_help = discord.Embed(title = "<:menu1:1003035563970003035> | Option(s) à choisir :", description="Une fois l'option choisie, le message sera modifié !", color=0xffab33)
                    embed_menu_help.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                    await interaction.response.send_message(embed = embed_menu_help, view=view_menu_help)

            else :
                button_enable = Button(label="Activé", style=discord.ButtonStyle.green, emoji="✅")

                async def button_callback(interaction):
                    if interaction.permissions.administrator:
                        enabled_command= open(f'./toggle/help_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        id_server = []
                        for line in enabled_command:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            id_server.append(line)
                        enabled_command.close()
                        enabled_command = open(f'./toggle/help_toggle.txt','w')
                        for line in id_server:
                            enabled_command.write(line)
                        enabled_command.close()
                        embed_toggle_enabled = discord.Embed(title=f"<:enabled:1003234802121588796> | J'ai activé la commande `help`.", description="Pour la désactiver, fais `/toggle help`.", color=0x00d731)
                        embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await interaction.response.send_message(embed=embed_toggle_enabled)
                    else:
                        embed_not_admin = discord.Embed(title="Tu n'es pas administrateur 😐", description="La commande `/toggle` est réservée aux administrateurs. Monte encore en grade soldat.", color=0xffab33)
                        await interaction.response.send_message(embed=embed_not_admin)

                button_enable.callback = button_callback
                view_enable = View()
                view_enable.add_item(button_enable)

                embed_disabled_command = discord.Embed(title="🚫 | La commande est désactivée.", description="Fais `/toggle help` pour la réactiver ou clique sur le bouton.", color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_disabled_command, view=view_enable)

        @bot.tree.command(name="news", description="Choisis une option pour afficher les nouveautés.")
        async def self(interaction: discord.Interaction, option: Literal["📈 | Nouvelles commandes", "⏏️ | Nouveaux mots", "🚀 | Commandes slash"]=None):
            with open('./toggle/news_toggle.txt', 'r') as news_toggle_file:
                disabled_command = news_toggle_file.read().splitlines()

            now_id = str(interaction.guild.id)

            if now_id not in disabled_command:
                #Page 1
                embed_news_page_1 = discord.Embed(title="📈 | Nouvelles commandes :", color=0xffab33)
                embed_news_page_1.add_field(name="Commandes avec statistiques :", value="** **", inline=False)
                embed_news_page_1.add_field(name="📶 | /ping", value="`Tester la vitesse de réception de message. `", inline=True)
                embed_news_page_1.add_field(name="📊 | /stats", value="`Toutes les statistiques relatives au bot.`", inline=True)
                embed_news_page_1.add_field(name="Autres commandes :", value="** **", inline=False)
                embed_news_page_1.add_field(name="😂 | /fun", value="`Envoie une vidéo, un meme ou une blague pas drôle.`", inline=True)
                embed_news_page_1.add_field(name="<:toggle:1003035571251326976> | /toggle", value="`Permet de désactiver ou activer les commandes.` <:admin:1003035554721566740>", inline=True)
                embed_news_page_1.add_field(name="<:admin:1003035554721566740>` : Requiert les permissions administrateur.`", value="** **", inline=False)
                embed_news_page_1.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                
                #Page 2
                embed_news_page_2 = discord.Embed(title="⏏️ | Nouveaux mots :", color=0xffab33, description="""`🟡 Baka            🟡 Nitro
🟡 France          🟡 Hébergeur
🟡 Snaptchat       🟡 Instagram`""")
                embed_news_page_2.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')

                #Page 3
                button_invite = Button(label="Réinvitation", style=discord.ButtonStyle.link, emoji="🔗", url="https://discord.com/api/oauth2/authorize?client_id=881098458482753586&permissions=26624&scope=bot%20applications.commands")
                view_invite = View()
                view_invite.add_item(button_invite)
                embed_news_page_3 = discord.Embed(title="<:support_commands:1004319969019973642> | Commandes slash !", color=0xffab33, description="Le_Bot passe aux commandes slash ! Son préfix n'est plus `b!` mais `/`. Tu dois me réinviter pour avoir accès aux commandes slash. Tu peux utiliser le bouton en dessous ou celui en bleu sur mon profil.")
                embed_news_page_3.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')

                if option == "📈 | Nouvelles commandes":
                    await interaction.response.send_message(embed=embed_news_page_1)

                elif option == "⏏️ | Nouveaux mots":
                    await interaction.response.send_message(embed=embed_news_page_2)

                elif option == "🚀 | Commandes slash":
                    await interaction.response.send_message(embed=embed_news_page_3, view=view_invite)

                #Définition d'un menu si aucune option est choisie
                elif option == None:
                    select_menu_news = Select(
                        placeholder="Choisis une option",
                        options=[
                            discord.SelectOption(label="Nouvelles commandes", emoji="📈", description="Affiche les nouvelles commandes."),
                            discord.SelectOption(label="Nouveaux mots", emoji="⏏️", description="Affiche les nouveaux mots."),
                            discord.SelectOption(label="Commandes slash", emoji="<:support_commands:1004319969019973642>", description="Les nouvelles commandes slash.")])
                    view_menu_news = View()
                    view_menu_news.add_item(select_menu_news)

                    async def menu_news_callback(interaction):
                        if select_menu_news.values[0] == "Nouvelles commandes":
                            await interaction.response.edit_message(embed=embed_news_page_1)
                        if select_menu_news.values[0] == "Nouveaux mots":
                            await interaction.response.edit_message(embed=embed_news_page_2)
                        if select_menu_news.values[0] == "Commandes slash":
                            await interaction.response.edit_message(embed=embed_news_page_3, view=view_invite)

                    select_menu_news.callback = menu_news_callback    
                    embed_menu_news = discord.Embed(title = "<:menu2:1003236078473461790> | Option(s) à choisir :", description="Une fois l'option choisie, le message sera modifié !", color=0xffab33)
                    embed_menu_news.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                    await interaction.response.send_message(embed = embed_menu_news, view=view_menu_news)

            else :
                button_enable = Button(label="Activé", style=discord.ButtonStyle.green, emoji="✅")

                #Réponse lorsque le bouton est préssé
                async def button_callback(interaction):
                    if interaction.permissions.administrator:
                        enabled_command= open(f'./toggle/news_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        id_server = []
                        for line in enabled_command:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            id_server.append(line)
                        enabled_command.close()
                        enabled_command = open(f'./toggle/news_toggle.txt','w')
                        for line in id_server:
                            enabled_command.write(line)
                        enabled_command.close()
                        embed_toggle_enabled = discord.Embed(title=f"<:enabled:1003234802121588796> | J'ai activé la commande `news`.", description="Pour la désactiver, fais `/toggle news`.", color=0x00d731)
                        embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await interaction.response.send_message(embed=embed_toggle_enabled)
                    else:
                        embed_not_admin = discord.Embed(title="Tu n'es pas administrateur 😐", description="La commande `/toggle` est réservée aux administrateurs. Monte encore en grade soldat.", color=0xffab33)
                        await interaction.response.send_message(embed=embed_not_admin)

                button_enable.callback = button_callback
                view_enable = View()
                view_enable.add_item(button_enable)

                embed_disabled_command = discord.Embed(title="🚫 | La commande est désactivée.", description="Fais `/toggle news` pour la réactiver ou clique sur le bouton.", color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_disabled_command, view=view_enable)

        @bot.tree.command(name="privacy", description="Connaître la politique de confidentialité.")
        async def self(interaction: discord.Interaction):
            with open('./toggle/privacy_toggle.txt', 'r') as privacy_toggle_file:
                disabled_command = privacy_toggle_file.read().splitlines()

            now_id = str(interaction.guild.id)

            if now_id not in disabled_command:
                button_privacy = Button(label="Lien", style=discord.ButtonStyle.link, emoji="🔗", url="https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt")
                view_privacy = View()
                view_privacy.add_item(button_privacy)
                embed_privacy = discord.Embed(title="<:privacy:1003035566763409438> | La politique de confidentialité de Le_Bot", color=0xffab33, url="https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt")
                embed_privacy.add_field(name="Le lien vers la politique de confidentialité :", value="https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/Politique%20de%20confidentialit%C3%A9.txt")
                embed_privacy.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed = embed_privacy, view=view_privacy)

            else :
                button_enable = Button(label="Activé", style=discord.ButtonStyle.green, emoji="✅")

                #Réponse lorsque le bouton est préssé
                async def button_callback(interaction):
                    if interaction.permissions.administrator:
                        enabled_command= open(f'./toggle/privacy_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        id_server = []
                        for line in enabled_command:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            id_server.append(line)
                        enabled_command.close()
                        enabled_command = open(f'./toggle/privacy_toggle.txt','w')
                        for line in id_server:
                            enabled_command.write(line)
                        enabled_command.close()
                        embed_toggle_enabled = discord.Embed(title=f"<:enabled:1003234802121588796> | J'ai activé la commande `privacy`.", description="Pour la désactiver, fais `/toggle privacy`.", color=0x00d731)
                        embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await interaction.response.send_message(embed=embed_toggle_enabled)
                    else:
                        embed_not_admin = discord.Embed(title="Tu n'es pas administrateur 😐", description="La commande `/toggle` est réservée aux administrateurs. Monte encore en grade soldat.", color=0xffab33)
                        await interaction.response.send_message(embed=embed_not_admin)

                button_enable.callback = button_callback
                view_enable = View()
                view_enable.add_item(button_enable)

                embed_disabled_command = discord.Embed(title="🚫 | La commande est désactivée.", description="Fais `/toggle privacy` pour la réactiver ou clique sur le bouton.", color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_disabled_command, view=view_enable)

        @bot.tree.command(name="server", description="Envoie le serveur Discord du créateur de Le_Bot.")
        async def self(interaction: discord.Interaction):
            with open('./toggle/server_toggle.txt', 'r') as server_toggle_file:
                disabled_command = server_toggle_file.read().splitlines()

            now_id = str(interaction.guild.id)

            if now_id not in disabled_command:
                button_server = Button(label="Lien", style=discord.ButtonStyle.link, emoji="🔗", url="https://discord.gg/b6jjy5yKXV")
                view_server = View()
                view_server.add_item(button_server)
                embed_server = discord.Embed(title="<:discord:1003035559205286008> | Le serveur du créateur de **Le_Bot**.", color=0xffab33, url="https://discord.gg/b6jjy5yKXV")
                embed_server.add_field(name="Le lien du serveur de Nathoune :", value="https://discord.gg/b6jjy5yKXV")
                embed_server.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_server, view=view_server)

            else :
                button_enable = Button(label="Activé", style=discord.ButtonStyle.green, emoji="✅")

                #Réponse lorsque le bouton est préssé
                async def button_callback(interaction):
                    if interaction.permissions.administrator:
                        enabled_command= open(f'./toggle/server_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        id_server = []
                        for line in enabled_command:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            id_server.append(line)
                        enabled_command.close()
                        enabled_command = open(f'./toggle/server_toggle.txt','w')
                        for line in id_server:
                            enabled_command.write(line)
                        enabled_command.close()
                        embed_toggle_enabled = discord.Embed(title=f"<:enabled:1003234802121588796> | J'ai activé la commande `server`.", description="Pour la désactiver, fais `/toggle server`.", color=0x00d731)
                        embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await interaction.response.send_message(embed=embed_toggle_enabled)
                    else:
                        embed_not_admin = discord.Embed(title="Tu n'es pas administrateur 😐", description="La commande `/toggle` est réservée aux administrateurs. Monte encore en grade soldat.", color=0xffab33)
                        await interaction.response.send_message(embed=embed_not_admin)

                button_enable.callback = button_callback
                view_enable = View()
                view_enable.add_item(button_enable)

                embed_disabled_command = discord.Embed(title="🚫 | La commande est désactivée.", description="Fais `/toggle server` pour la réactiver ou clique sur le bouton.", color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_disabled_command, view=view_enable)

        @bot.tree.command(name="github", description="Le_Bot sur GitHub.")
        async def self(interaction: discord.Interaction):
            with open('./toggle/github_toggle.txt', 'r') as github_toggle_file:
                disabled_command = github_toggle_file.read().splitlines()

            now_id = str(interaction.guild.id)

            if now_id not in disabled_command:
                button_github = Button(label="Lien", style=discord.ButtonStyle.link, emoji="🔗", url="https://github.com/Nathoune-YT/le_bot")
                view_github = View()
                view_github.add_item(button_github)
                embed_github = discord.Embed(title="<:github:1003035561453432934> | Le_Bot est opensource et son code se trouve sur GitHub !", color=0xffab33, url="https://github.com/Nathoune-YT/le_bot")
                embed_github.add_field(name="🌍 | Informations", value="Le_Bot est opensource et se trouve sur GitHub (https://github.com/Nathoune-YT/le_bot). Vous pouvez simplement regarder le script, le modifier et m'envoyer une pull request pour peut-être voir vos modifications dans le code officiel de Le_Bot ou l'utiliser et le modifier tout en suivant la procédure à lire dans le README !")
                embed_github.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_github, view=view_github)

            else :
                button_enable = Button(label="Activé", style=discord.ButtonStyle.green, emoji="✅")

                #Réponse lorsque le bouton est préssé
                async def button_callback(interaction):
                    if interaction.permissions.administrator:
                        enabled_command= open(f'./toggle/github_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        id_server = []
                        for line in enabled_command:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            id_server.append(line)
                        enabled_command.close()
                        enabled_command = open(f'./toggle/github_toggle.txt','w')
                        for line in id_server:
                            enabled_command.write(line)
                        enabled_command.close()
                        embed_toggle_enabled = discord.Embed(title=f"<:enabled:1003234802121588796> | J'ai activé la commande `github`.", description="Pour la désactiver, fais `/toggle github`.", color=0x00d731)
                        embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await interaction.response.send_message(embed=embed_toggle_enabled)
                    else:
                        embed_not_admin = discord.Embed(title="Tu n'es pas administrateur 😐", description="La commande `/toggle` est réservée aux administrateurs. Monte encore en grade soldat.", color=0xffab33)
                        await interaction.response.send_message(embed=embed_not_admin)

                button_enable.callback = button_callback
                view_enable = View()
                view_enable.add_item(button_enable)

                embed_disabled_command = discord.Embed(title="🚫 | La commande est désactivée.", description="Fais `/toggle github` pour la réactiver ou clique sur le bouton.", color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_disabled_command, view=view_enable)

        @bot.tree.command(name="site", description="Le site officiel de Le_Bot.")
        async def self(interaction: discord.Interaction):
            with open('./toggle/site_toggle.txt', 'r') as site_toggle_file:
                disabled_command = site_toggle_file.read().splitlines()

            now_id = str(interaction.guild.id)

            if now_id not in disabled_command:
                button_site = Button(label="Lien", style=discord.ButtonStyle.link, emoji="🔗", url="https://le-bot.cf")
                view_site = View()
                view_site.add_item(button_site)
                embed_site = discord.Embed(title="🌐 | Le site web officiel de Le_Bot", color=0xffab33, url="https://le-bot.cf")
                embed_site.add_field(name="Le lien du site officiel :", value="https://le-bot.cf")
                embed_site.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_site, view=view_site)

            else :
                button_enable = Button(label="Activé", style=discord.ButtonStyle.green, emoji="✅")

                #Réponse lorsque le bouton est préssé
                async def button_callback(interaction):
                    if interaction.permissions.administrator:
                        enabled_command= open(f'./toggle/site_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        id_server = []
                        for line in enabled_command:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            id_server.append(line)
                        enabled_command.close()
                        enabled_command = open(f'./toggle/site_toggle.txt','w')
                        for line in id_server:
                            enabled_command.write(line)
                        enabled_command.close()
                        embed_toggle_enabled = discord.Embed(title=f"<:enabled:1003234802121588796> | J'ai activé la commande `site`.", description="Pour la désactiver, fais `/toggle site`.", color=0x00d731)
                        embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await interaction.response.send_message(embed=embed_toggle_enabled)
                    else:
                        embed_not_admin = discord.Embed(title="Tu n'es pas administrateur 😐", description="La commande `/toggle` est réservée aux administrateurs. Monte encore en grade soldat.", color=0xffab33)
                        await interaction.response.send_message(embed=embed_not_admin)

                button_enable.callback = button_callback
                view_enable = View()
                view_enable.add_item(button_enable)

                embed_disabled_command = discord.Embed(title="🚫 | La commande est désactivée.", description="Fais `/toggle site` pour la réactiver ou clique sur le bouton.", color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_disabled_command, view=view_enable)

        @bot.tree.command(name="ping", description="Tester la latence du bot.")
        async def self(interaction: discord.Interaction):
            with open('./toggle/ping_toggle.txt', 'r') as ping_toggle_file:
                disabled_command = ping_toggle_file.read().splitlines()

            now_id = str(interaction.guild.id)

            if now_id not in disabled_command:
                embed_ping = discord.Embed(title="Donc là je dois répondre 🤔 ?", color=0xffab33)
                embed_ping.add_field(name=f"🏓 | J\'ai bien reçu ton message en : `{round(bot.latency * 1000)}ms`", value=f"(je te réponds c'est le principal ok.)")
                embed_ping.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_ping)

            else :
                button_enable = Button(label="Activé", style=discord.ButtonStyle.green, emoji="✅")

                #Réponse lorsque le bouton est préssé
                async def button_callback(interaction):
                    if interaction.permissions.administrator:
                        enabled_command= open(f'./toggle/ping_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        id_server = []
                        for line in enabled_command:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            id_server.append(line)
                        enabled_command.close()
                        enabled_command = open(f'./toggle/ping_toggle.txt','w')
                        for line in id_server:
                            enabled_command.write(line)
                        enabled_command.close()
                        embed_toggle_enabled = discord.Embed(title=f"<:enabled:1003234802121588796> | J'ai activé la commande `ping`.", description="Pour la désactiver, fais `/toggle ping`.", color=0x00d731)
                        embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await interaction.response.send_message(embed=embed_toggle_enabled)
                    else:
                        embed_not_admin = discord.Embed(title="Tu n'es pas administrateur 😐", description="La commande `/toggle` est réservée aux administrateurs. Monte encore en grade soldat.", color=0xffab33)
                        await interaction.response.send_message(embed=embed_not_admin)

                button_enable.callback = button_callback
                view_enable = View()
                view_enable.add_item(button_enable)

                embed_disabled_command = discord.Embed(title="🚫 | La commande est désactivée.", description="Fais `/toggle ping` pour la réactiver ou clique sur le bouton.", color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_disabled_command, view=view_enable)

        @bot.tree.command(name="stats", description="Toutes les statistiques relatives au bot.")
        async def self(interaction: discord.Interaction):
            delta_uptime = datetime.utcnow() - bot.launch_time
            hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            days, hours = divmod(hours, 24)
            with open('./toggle/stats_toggle.txt', 'r') as stats_toggle_file:
                disabled_command = stats_toggle_file.read().splitlines()

            now_id = str(interaction.guild.id)

            if now_id not in disabled_command:
                button_changelog = Button(label="Changelog", style=discord.ButtonStyle.link, emoji="✏️", url="https://github.com/Nathoune-YT/le_bot/commits/main")
                view_changelog = View()
                view_changelog.add_item(button_changelog)

                embed_stats = Embed(title="📊 | Statistiques", description="Voici toutes les statistiques :", color=0xffab33)
                embed_stats.add_field(name="📈 | Serveurs :", value=f"`{len(bot.guilds)}`", inline = False)
                embed_stats.add_field(name="🏓 | Ping :", value=f"`{round(bot.latency * 1000)}ms`", inline = False)
                embed_stats.add_field(name="⌛ | Connecté depuis :", value=f"`{days}j, {hours}h, {minutes}m, {seconds}s`", inline = False)
                #Entre "<t:" et ":R>", entrez le temps en UNIX
                embed_stats.add_field(name="⏲️ | Dernières modifications :", value="<t:UNIX:R>", inline = False)
                embed_stats.add_field(name="<:ram:1003035568680222720> | Utilisation RAM :", value=f"`{psutil.virtual_memory().percent}%`", inline = False)
                embed_stats.add_field(name="<:cpu:1003035557011669074> | Utilisation CPU :", value=f"`{psutil.cpu_percent()}%`", inline = False)
                embed_stats.add_field(name="<:discordpy:1004395068964208650> | Framework de développement :", value="`discord.py 2.0`", inline=False)
                embed_stats.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed = embed_stats, view=view_changelog)

            else :
                button_enable = Button(label="Activé", style=discord.ButtonStyle.green, emoji="✅")

                #Réponse lorsque le bouton est préssé
                async def button_callback(interaction):
                    if interaction.permissions.administrator:
                        enabled_command= open(f'./toggle/stats_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        id_server = []
                        for line in enabled_command:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            id_server.append(line)
                        enabled_command.close()
                        enabled_command = open(f'./toggle/stats_toggle.txt','w')
                        for line in id_server:
                            enabled_command.write(line)
                        enabled_command.close()
                        embed_toggle_enabled = discord.Embed(title=f"<:enabled:1003234802121588796> | J'ai activé la commande `stats`.", description="Pour la désactiver, fais `/toggle stats`.", color=0x00d731)
                        embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await interaction.response.send_message(embed=embed_toggle_enabled)
                    else:
                        embed_not_admin = discord.Embed(title="Tu n'es pas administrateur 😐", description="La commande `/toggle` est réservée aux administrateurs. Monte encore en grade soldat.", color=0xffab33)
                        await interaction.response.send_message(embed=embed_not_admin)

                button_enable.callback = button_callback
                view_enable = View()
                view_enable.add_item(button_enable)

                embed_disabled_command = discord.Embed(title="🚫 | La commande est désactivée.", description="Fais `/toggle stats` pour la réactiver ou clique sur le bouton.", color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_disabled_command, view=view_enable)

        @app_commands.default_permissions(administrator=True)
        @bot.tree.command(name="toggle", description="Permet de désactiver ou activer les commandes.")
        async def self(interaction: discord.Interaction, commande: Literal["help", "news", "server", "privacy", "github", "ping", "stats", "fun"]):    

            now_id = str(interaction.guild.id)

            with open(f"./toggle/{commande}_toggle.txt", 'r') as check_id:
                id_file = check_id.read().splitlines()

            if now_id not in id_file:
                with open(f"./toggle/{commande}_toggle.txt", "a") as disabled_command:
                    disabled_command.write(str(f"{now_id}\n"))

                embed_toggle_disabled = discord.Embed(title=f"<:disabled:1003234799995068436> | J'ai désactivé la commande `{commande}`.", description="Pour la réactiver, fais `/toggle {}`".format(commande), color=0xff0000)
                embed_toggle_disabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_toggle_disabled)
                return

            else:
                enabled_command= open(f'./toggle/{commande}_toggle.txt','r')
                actual_id = [f'{now_id}']
                id_server = []
                for line in enabled_command:
                    for word in actual_id:
                        if word in line:
                            line = line.replace(word,'')
                    id_server.append(line)
                enabled_command.close()
                enabled_command = open(f'./toggle/{commande}_toggle.txt','w')
                for line in id_server:
                    enabled_command.write(line)
                enabled_command.close()

                embed_toggle_enabled = discord.Embed(title=f"<:enabled:1003234802121588796> | J'ai activé la commande `{commande}`.", description="Pour la désactiver, fais `/toggle {}`".format(commande), color=0x00d731)
                embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_toggle_enabled)

        @bot.tree.command(name="fun", description="Envoie une vidéo, un meme ou une blague pas drôle.")
        async def self(interaction: discord.Interaction, option: Literal["📹 | Vidéo", "💬 | Meme", "📜 | Blague"]):
            with open('./toggle/fun_toggle.txt', 'r') as fun_toggle_file:
                disabled_command = fun_toggle_file.read().splitlines()

            now_id = str(interaction.guild.id)

            if now_id not in disabled_command:

                if option == "📹 | Vidéo" :
                    await interaction.response.send_message(random.choice(fun_links["videos"]))
                if option == "💬 | Meme":
                    await interaction.response.send_message(random.choice(fun_links["memes"]))
                if option == "📜 | Blague":
                    await interaction.response.send_message(random.choice(fun_links["blagues"]))

            else :
                button_enable = Button(label="Activé", style=discord.ButtonStyle.green, emoji="✅")

                #Réponse lorsque le bouton est préssé
                async def button_callback(interaction):
                    if interaction.permissions.administrator:
                        enabled_command= open(f'./toggle/fun_toggle.txt','r')
                        actual_id = [f'{now_id}']
                        id_server = []
                        for line in enabled_command:
                            for word in actual_id:
                                if word in line:
                                    line = line.replace(word,'')
                            id_server.append(line)
                        enabled_command.close()
                        enabled_command = open(f'./toggle/fun_toggle.txt','w')
                        for line in id_server:
                            enabled_command.write(line)
                        enabled_command.close()
                        embed_toggle_enabled = discord.Embed(title=f"<:enabled:1003234802121588796> | J'ai activé la commande `fun`.", description="Pour la désactiver, fais `/toggle fun`.", color=0x00d731)
                        embed_toggle_enabled.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                        await interaction.response.send_message(embed=embed_toggle_enabled)
                    else:
                        embed_not_admin = discord.Embed(title="Tu n'es pas administrateur 😐", description="La commande `/toggle` est réservée aux administrateurs. Monte encore en grade soldat.", color=0xffab33)
                        await interaction.response.send_message(embed=embed_not_admin)

                button_enable.callback = button_callback
                view_enable = View()
                view_enable.add_item(button_enable)

                embed_disabled_command = discord.Embed(title="🚫 | La commande est désactivée.", description="Fais `/toggle fun` pour la réactiver ou clique sur le bouton.", color=0xff0000)
                embed_disabled_command.set_footer(text="Le_Bot, votre bot interactif !", icon_url='https://raw.githubusercontent.com/Nathoune-YT/le_bot/main/images/Icon.png')
                await interaction.response.send_message(embed=embed_disabled_command, view=view_enable)

        bot.run(config["token"])

    except:
        main()

main()
