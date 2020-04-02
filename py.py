import discord
import os


client = discord.Client()


@client.event
async def on_ready():
  print("ready")


@client.event
async def on_message(message):
  if message.content.startswith("시아야 안녕"):
    await client.message_send(message.channel,"안녕하세요.")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
