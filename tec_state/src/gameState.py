import re
import discord
import termtables as tt
from datetime import datetime
from tec_state.src.message import fetch_data, get_user_messages, get_data


async def state_game(channel, client, mc_channel):
    messages = await fetch_data(client, mc_channel)
    users = list(set(userms.split(" ")[1] for userms in messages
                     if ":arrow_right:" in userms
                     if ":first_place:" not in userms))
    user_stats = []

    for user in users:
        user_messages = get_user_messages(messages, user)
        death_count, join_count, medal_list = get_data(user_messages)
        texts = len([0 for message in user_messages if len(re.findall(f"{user}:", message)) == 1])
        user_stats.append([user.replace("\\", ""), join_count, death_count, len(medal_list), texts])

    user_stats.sort(key=lambda x: x[1], reverse=True)

    header = ["username", "joined", "death", "medal", "texts"]
    table = tt.to_string(user_stats, header=header, padding=(0, 1), alignment="lrrrr")
    await generate_compare_embed(channel, table)


async def generate_compare_embed(channel, test):
    now = datetime.now()
    embed = discord.Embed(title=f"Player statistics ",
                          description=f"In the following all player statistics are shown and compared with each other.",
                          color=0xff8800)
    embed.add_field(name=":crown: Game statistics", value=f"```{test}```", inline=False)
    embed.set_footer(text=f"Generated on {now.strftime('%d.%m.%Y, %H:%M:%S')} by TecState")
    await channel.send(embed=embed)
