import discord
from datetime import datetime
from tec_state.src.message import fetch_data, get_user_messages, get_data


async def state_player(channel, username, client, mc_channel):
    username = username.replace("_", "\\_")
    messages = await fetch_data(client, mc_channel)
    messages = get_user_messages(messages, username)
    death_count, join_count, medal_list = get_data(messages)
    # print(f"{username} -> Death: {death_count}, Joins: {join_count}, archivs: {len(medal_list)}")

    await generate_user_embed(channel, death_count, join_count, medal_list, username)


async def generate_user_embed(channel, death_count, join_count, medal_list, username="everybody"):
    now = datetime.now()
    medals = "\n".join(medal_list[-7:])
    embed = discord.Embed(title=f"Minecraft statistics from {username}",
                          description=f"Below you can see the most important information about {username}. The number "
                                      f"of deaths, game participations and the last seven achievements are listed.",
                          color=0xff8800)
    embed.add_field(name=":arrow_right: Join counter", value=f"{join_count}", inline=True)
    embed.add_field(name=":skull: Death counter", value=f"{death_count}", inline=True)
    embed.add_field(name=":trophy: Total achievements", value=f"{len(medal_list)}", inline=True)
    embed.add_field(name=":medal: Achievements", value=f"```{medals}```", inline=False)
    embed.set_footer(text=f"Generated on {now.strftime('%d.%m.%Y, %H:%M:%S')} by TecState")
    await channel.send(embed=embed)
