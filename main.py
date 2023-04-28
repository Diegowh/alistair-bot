import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord
from quotes import final_alistair_quotes as quotes

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name='quote')
async def quote(ctx):
    await ctx.send(random.choice(quotes))
    
    
@bot.event
async def on_ready():
    print(f'{bot.user.name} se ha conectado a Discord!')

@bot.event
async def on_command_error(ctx, error):
    print(f'Error en el comando: {ctx.message.content}. Error: {error}')
    

if __name__ == "__main__":
    bot.run(TOKEN)