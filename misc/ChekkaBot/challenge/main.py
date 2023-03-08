from config import TOKEN, FLAG
import discord
from commands import Help, GetFlag, Stats, AddNote, GetNote, Poll, Socials, Joke
import sqlite3


class ChekkaBot(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.members = True
        intents.reactions = True
        intents.message_content = True
        super().__init__(intents=intents, command_prefix="/")
        self.tree = discord.app_commands.CommandTree(self)
    
    async def setup_hook(self) -> None:
        self.tree.add_command(Help())
        self.tree.add_command(Joke())
        self.tree.add_command(AddNote())
        self.tree.add_command(GetNote())
        self.tree.add_command(Poll())
        self.tree.add_command(GetFlag())
        self.tree.add_command(Stats())
        self.tree.add_command(Socials())
    
    async def on_ready(self) -> None:
        await self.tree.sync()
        await self.change_presence(activity=discord.Game(name="/help"))
        print(f'{self.user} has connected to Discord!')
    
        
conn = sqlite3.connect("notes.db")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS notes")
c.execute("DROP TABLE IF EXISTS VeryS3cretTable")
c.execute("""CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            title TEXT,
            data TEXT
            )""")
c.execute("""CREATE TABLE IF NOT EXISTS VeryS3cretTable (
            user TEXT,
            fl4g TEXT
            )""")
c.execute("INSERT INTO VeryS3cretTable (user, fl4g) VALUES (?, ?)", ("McFawk", FLAG))
conn.commit()
conn.close()

if __name__ == "__main__":
    client = ChekkaBot()
    client.run(TOKEN)