import asyncio
import random
from colorama import Back, Fore, Style
import sys
import os
import discord
from discord.ext import commands
from help_info import *
from auth_info import *
from auth import *
import time
import random

client = discord.Client()

@client.event
async def on_ready():
    print(('<' + client.user.name) + ' Online>')
    print(f"discord.py {discord.__version__}\n")

@client.event
async def on_command_error(ctx, error):
    print(Style.BRIGHT + Fore.RED + f"Error occured with: {ctx.command}\n{error}\n")
    print(Style.RESET_ALL)

@client.event
async def on_message(message):
    if not isinstance(message.channel,discord.DMChannel):
        return
    # Ignore messages made by the client
    if(message.author == client.user):
        return

    FLAG = "`IJCTF{0p3n3d_d3_bru1jn_v4ul75}`"
    LEVEL_MESSAGE = ["Time to test your lock picking skills", "First lock opened! Hurry up and open the next one before the gaurds show up", "Second Lock Opened! Dang your a professional. Third lock now...", "Third lock open, now you have to be fast.", "Fourth lock open. Come on just two more...", "Last one..."]
    ALPHABET = ["01", "456", "56789", "1234", "012589", "01"]
    LENGTH = [7, 6, 4, 5, 4, 11]

    def check(m):
        return m.author == message.author

    response = message.content
    if(response == 'start'):
        level = 0
        while(level < 7):
            if(level == 6):
                await message.author.send(FLAG)
                return
            await message.author.send(LEVEL_MESSAGE[level])
            keypad = ' '.join(['[ ' + c + ' ]' for c in ALPHABET[level]])
            prompt = '```' + 'I AM'.center(len(keypad)) + '\n\n' + ('_ ' * LENGTH[level]).center(len(keypad)) + '\n\n' + 'LOCKED'.center(len(keypad)) + '\n\n' + keypad + '```'
            await message.author.send(prompt)
            pin = ''.join([random.choice(ALPHABET[level]) for _ in range(LENGTH[level])])
            try:
                response = (await client.wait_for('message',check=check, timeout=10)).content
            except:
                await message.author.send("Too Slow")
                return
            if(pin in response):
                level += 1
            else:
                await message.author.send("Wrong Pin")
                await asyncio.sleep(5)
                return

if __name__ == '__main__':
    client.run(auth_token)
