import discord
from discord.ext import commands
from datetime import datetime

TOKEN = 'TOKEN'
CHANNEL_ID = 'Channel ID'

class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(CHANNEL_ID)
        await channel.send('안녕 퀴노봇이야 뭘 도와줄까?')
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
