from dotenv import load_dotenv
import os
import random
import discord
from discord.ext import commands

load_dotenv()

token = os.environ.get("DISC_KEY")
bot = commands.Bot(command_prefix = "!")

@bot.command()
async def ping(context):
	await context.send("pong!")

@bot.command()
async def coinflip(context, guess):
	coin = random.randint(1,2)

	options = {"1", "2"}
	if guess not in options:
		await context.send("What a bad guess...")
		return

	if coin == 1:
		if coin == int(guess):
			await context.send("Heads, you win the toss!")
		else:
			await context.send("Heads, you lose the toss!")
	if coin == 2:
		if coin == int(guess):
			await context.send("Tails, you win the toss!")
		else:
			await context.send("Tails, you lose the toss!")

@bot.command()
async def rps(context, choice):
    rps_dict = {
    	1 : "Rock",
    	2 : "Paper",
    	3 : "Scissors"
    }

    await context.send("Rock")
    await context.send("Paper")
    await context.send("Scissors")

    options = {"1", "2", "3"}

    if choice not in options:
    	await context.send("That's not a choice doofus!")
    	return
    bot_choice = random.randint(1,3)
    bot_choice = rps_dict[bot_choice]
    choice = rps_dict[int(choice)]

    # TODO Find a way to get these functions to replace the long repetitive await context.send bs below.
    # def win():
    # 	context.send(f"You chose {choice} and I chose {bot_choice}, you win!")
    # def lose():
    # 	context.send(f"You chose {choice} and I chose {bot_choice}, you lose!")

    if choice == bot_choice:
    	await context.send(f"We both chose {choice}, it's a tie!")
    elif choice == rps_dict[1]:
    	if bot_choice == rps_dict[2]:
    		await context.send(f"You chose {choice} and I chose {bot_choice}, you lose!")
    	if bot_choice == rps_dict[3]:
    		await context.send(f"You chose {choice} and I chose {bot_choice}, you win!")
    elif choice == rps_dict[2]:
    	if bot_choice == rps_dict[3]:
    		await context.send(f"You chose {choice} and I chose {bot_choice}, you lose!")
    	if bot_choice == rps_dict[1]:
    		await context.send(f"You chose {choice} and I chose {bot_choice}, you win!")
    elif choice == rps_dict[3]:
    	if bot_choice == rps_dict[1]:
    		await context.send(f"You chose {choice} and I chose {bot_choice}, you lose!")
    	if bot_choice == rps_dict[2]:
    		await context.send(f"You chose {choice} and I chose {bot_choice}, you win!")

bot.run(token)