import discord
from discord import app_commands
from tec_state.src.gameState import state_game
from tec_state.src.playerState import state_player
import configparser as cp

cfg = cp.ConfigParser()
cfg.read("./../setup.cfg")
token = cfg.get('discord', 'token')
guild = discord.Object(id=int(cfg.get('discord', 'guild')))
mc_channel = int(cfg.get('discord', 'channel'))
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync(guild=guild)
    print(f"We have logged in as {client.user}.")


@tree.command(name="stats", description="This shows the statistics of the minecraft server!", guild=guild)
async def player_stats(interaction, username: str):
    await interaction.response.send_message("Your request is being processed!")
    await state_player(interaction.channel, username, client, mc_channel)


@tree.command(name="compare", description="It summarizes and compares all the information of the players!", guild=guild)
async def game_stats(interaction):
    await interaction.response.send_message("Your request is being processed!")
    await state_game(interaction.channel, client, mc_channel)


client.run(token)
