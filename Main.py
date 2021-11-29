import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("ready")
    async def on_message(self, message):
        print("ghost")
        if message.author.id == CLIENT ID:748631377330569254
            await message.edit(content=message.content + " ")

client = MyClient()
client.run("NzQ4NjMxMzc3MzMwNTY5MjU0.YI1zoA.MxAmlBgwbSwn9gceK9kVyqOF19s", bot=False)
