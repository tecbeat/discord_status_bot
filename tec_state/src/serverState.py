import discord
from datetime import datetime


async def server_state(channel):
    await generate_user_embed(channel)


async def generate_user_embed(channel):
    now = datetime.now()
    packs = "\n - ".join(["Deathpos", "DropHeads", "Dwg-oasisdesert", "Essentials", "Multiverse", "Terra", "Timber",
                          "Awesomedungeon", "Better-Ruined-Portals", "Custom-Caves", "Extract-me-ships",
                          "More-Village-Types", "Moss-Ruins", "Overhauled-Village", "pillager-stronghold",
                          "pirate-ships", "Sequoia-Trees", "Whimzee-s-dungeon-overhaul"])
    embed = discord.Embed(title=f"Server information",
                          description=f"The Minecraft server is to be started by means of a join attempt thereupon "
                                      f"this needs up to 4 minutes to start. If the minecraft server is started, the "
                                      f"server chat and important events are transferred to the chat in discord. ",
                          color=0xff8800)
    embed.add_field(name=":door: Server address", value=f"minecraft.tecgame.de", inline=True)
    embed.add_field(name=":video_game: Game version", value=f"1.19.2 vanilla", inline=True)
    embed.add_field(name=":game_die: World count", value=f"6", inline=False)
    embed.add_field(name=":newspaper: Plugin/Datapack list", value=f"``` - {packs}```", inline=False)
    embed.set_footer(text=f"Generated on {now.strftime('%d.%m.%Y, %H:%M:%S')} by TecState")
    await channel.response.send_message(embed=embed)
