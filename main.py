import aiohttp
import discord
from discord.ext import commands

my_token = 'Token_Here'
client_id = 'Client_ID_Here'
bot_activity = "Playstation"

class MyBot(commands.Bot):
    
    def __init__(self):
        super().__init__(command_prefix = '$', intents = discord.Intents.all(), application_id = client_id) 
    
    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        self.synced = False

        # COGS
        await self.load_extension("cogs.playstation.resigner")
        # await self.load_extension(cogs.folder.filename)
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await bot.tree.sync()
            self.synced = True
            await self.change_presence(activity=discord.Game(name=bot_activity))

        print(f'{self.user} has connected to Discord!')

bot = MyBot()
bot.run(my_token)