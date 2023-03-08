import discord
import requests
import sqlite3
import json


class Help(discord.app_commands.Command):
    def __init__(self):
        super().__init__(
            name="help",
            description="View available commands.",
            callback=self.callback
        )
    async def callback(self, interaction: discord.Interaction) -> None:
        embed = (
            discord.Embed(
                title="ChekkaBot - the bestest bot out there :)",
                description=(
                    "My very well built, fast and secure bot, check it out, oh wait, only admins can!!"
                ),
                colour=discord.Colour.blue(),
            )
            .set_thumbnail(url=interaction.client.user.display_avatar.url)
            .set_footer(text="Made by McFawk.")
        )
        for command in interaction.client.tree.get_commands():
            embed.add_field(
                name=f"/{command.name}",
                value=command.description,
                inline=False,
            )
        await interaction.response.send_message(embed=embed)


class GetFlag(discord.app_commands.Command):
    def __init__(self):
        super().__init__(
            name="secret",
            description="Obtain a secret.",
            callback=self.callback
        )
    async def callback(self, interaction: discord.Interaction, password: str) -> None:
        if password and len(password)>4:
            await interaction.response.send_message("GG you got me :D, here's your secret: https://rr.noordstar.me/alphactfscret-7552af2b")
            return
        await interaction.response.send_message("Wrong password! try again", ephemeral=True)
        
         
class Stats(discord.app_commands.Command):
    def __init__(self):
        super().__init__(
            name="stats",
            description="Some stats about the bot and users.",
            callback=self.callback
        )
    async def callback(self, interaction: discord.Interaction) -> None:
        r = requests.get("https://rr.noordstar.me/data/7552af2b")
        await interaction.response.send_message(f"{r.text[234:r.text.index('</h1>')]} users have been bamboozled")

   
class AddNote(discord.app_commands.Command):
    def __init__(self):
        super().__init__(
            name="addnote",
            description="Add notes.",
            callback=self.callback
        )
    async def callback(self, interaction: discord.Interaction, title: str, data:str) -> None:
        try:
            conn = sqlite3.connect("notes.db")
            c = conn.cursor()
            c.execute("INSERT INTO notes (user, title, data) VALUES (?, ?, ?)", (interaction.user.display_name, title, data))
            id = c.lastrowid
            conn.commit()
            conn.close()
            await interaction.response.send_message(f"Note added with id={id}", ephemeral=True)
        except:
            await interaction.response.send_message("something went wrong", ephemeral=True)


class GetNote(discord.app_commands.Command):
    def __init__(self):
        super().__init__(
            name="getnote",
            description="Get notes by id.",
            callback=self.callback
        )
    async def callback(self, interaction: discord.Interaction, id: str) -> None:
        try:
            conn = sqlite3.connect("notes.db")
            c = conn.cursor()
            res = c.execute(f"select user, title, data from notes where user='{interaction.user.display_name}' and id='{id}'")
            notes = res.fetchall()
            conn.close()
            if not notes:
                await interaction.response.send_message("Note not found", ephemeral=True)
                return
            embed = discord.Embed()
            for i in notes:
                if interaction.user.display_name == i[0]:
                    embed.add_field(inline=False, name=i[1], value=i[2])
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"something went wrong: {e}", ephemeral=True)


class Poll(discord.app_commands.Command):
    def __init__(self) -> None:
        super().__init__(
            name="poll",
            description="Create a poll, add title, seperate options by , (comma)",
            callback=self.callback,
        )
    async def callback(self, interaction: discord.Interaction, title: str, options: str) -> None:
        options = [i.strip() for i in options.split(",") if len(i)>0]
        if(len(options) <2 or len(options)>10):
            await interaction.response.send_message("Number of options must be equal or under 10")
            return
        reactions = []
        embed = "something went wrong.."
        if(len(options) == 2 and (("yes" in options[0].lower() and "no" in options[1].lower()) or ("oui" in options[0].lower() and "non" in options[1].lower()))):
            embed = discord.Embed(
                title=f"{title}",
                description=(f"✅   {options[0]}\n\n❌   {options[1]}"),
                colour=discord.Colour.green()
            )
            reactions = ["✅","❌"]
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
            description = []
            for x, option in enumerate(options):
                description += '\n\n{}   {}'.format(reactions[x], option)
            embed = discord.Embed(title=title, description=''.join(description), colour=discord.Colour.green())

        message = await interaction.channel.send(embed=embed)
        await interaction.response.send_message(interaction.user.display_name+" started a poll.")
        for i in reactions[:len(options)]:
            await message.add_reaction(i)


class Joke(discord.app_commands.Command):
    def __init__(self):
        super().__init__(
            name="joke",
            description="For a joke.",
            callback=self.callback
        )
    async def callback(self, interaction: discord.Interaction) -> None:
        try:
            r = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist")
            res = json.loads(r.text)
            if res["type"] == "twopart":
                await interaction.response.send_message(f"{res['setup']}, {res['delivery']}")
            else:
                await interaction.response.send_message(f"{res['joke']}")
        except:
            await interaction.response.send_message("something went wrong", ephemeral=True)
            
            
class Socials(discord.app_commands.Command):
    def __init__(self):
        super().__init__(
            name="socials",
            description="View Alphabit's social media and online accounts.",
            callback=self.callback
        )
    async def callback(self, interaction: discord.Interaction) -> None:
        embed = (
            discord.Embed(
                title="Our social media!",
                # url="(coming soon)",
                description=(
                    "Facebook:  https://www.facebook.com/AlphaBitClub\n\n"
                    "Instagram:  https://www.instagram.com/alphabitclub\n\n"
                    "Twitter:  https://mobile.twitter.com/alphabit_club\n\n"
                    "Spotify:  https://open.spotify.com/show/6rqGfwSFXM5RqV602PIVyP?si=LthuPpqHRS-ExNUS08IM_Q\n\n"
                    "LinkedIn:  https://dz.linkedin.com/company/alphabit-club\n\n"
                ),
                colour=discord.Colour.gold(),
            )
            .set_thumbnail(url=interaction.client.user.display_avatar.url)
            .set_footer(text="Made with by McFawk")
        )
        await interaction.response.send_message(embed=embed)
