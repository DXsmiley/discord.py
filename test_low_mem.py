import discord
import logging
import os
import objgraph

logging.basicConfig(level = logging.INFO)

TOKEN = os.environ.get('TOKEN')

import discord
import asyncio

client = discord.Client(max_messages=100, shard_id=0, shard_count=8)

@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    # print('Servers:', ' '.join(map(str, client.servers)))
    print(len(client.servers), 'servers')
    print('------')
    objgraph.show_most_common_types()

# @client.event
# async def on_message(message):
#     print(message.content)

client.run(TOKEN)
