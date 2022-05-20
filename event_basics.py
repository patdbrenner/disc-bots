from dotenv import load_dotenv
import os
import discord

load_dotenv()

token = os.environ.get("DISC_KEY")
intents = discord.Intents.all()
bot = discord.Client(intents = intents)

@bot.event
async def on_ready():
	print("Bot is online")

@bot.event
async def on_message(msg):
	username = msg.author.display_name
	channelname = msg.channel.name
	if msg.author == bot.user:
		return
	if msg.content == "hello":
		await msg.channel.send("Hello " + username)
	if msg.content == "who am i?":
		await msg.channel.send("You are " + username)
	if msg.content == "where am i?":
		await msg.channel.send("You are in " + channelname)

@bot.event
async def on_member_join(member):
	membername = member.display_name
	guild = member.guild
	guildname = guild.name
	dmchannel = await member.create_dm()
	await dmchannel.send(f"Welcome to {guildname}, {membername}!")


bot.run(token)