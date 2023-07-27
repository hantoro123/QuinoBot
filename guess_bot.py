import discord
import random
import asyncio

TOKEN = 'TOKEN'
CHANNEL_ID = 'Channel ID'

class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(CHANNEL_ID)
        print(f"Logged in as {self.user} (ID : {self.user.id})")
        print("---------------------")
        await channel.send("봇이 channel에 입장했습니다.")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('$guess'):
            await message.channel.send("Guess a number between 1 and 10")

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()
            
            answer = random(1,10)

            try:
                guess = await self.wait_for('message',check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f"Sorry, you took too long it was {answer}.")
            
            if int(guess.content) == answer:
                await message.channel.send("You are right!")
            else:
                await message.channel.send(f"Oops. IT is actually {answer}.")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)