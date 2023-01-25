import re


async def fetch_data(client, mc_channel):
    channel = await client.fetch_channel(mc_channel)
    messages = channel.history(limit=None)
    ms = []
    async for message in messages:
        if str(message.author) == "TecGame#7433":
            ms.append(message.content)
    return ms


def get_user_messages(messages, username):
    return [message for message in messages if username in message]


def get_data(messages):
    death_count = len([userms for userms in messages if ":skull:" in userms])
    join_count = len([userms for userms in messages if ":arrow_right:" in userms])
    medal_list = [re.search('\*\*(.+?)\*\*', userms).group(1) for userms in messages if ":medal:" in userms][::-1]
    return death_count, join_count, medal_list
