import asyncio
import random
from colorama import Back, Fore, Style
import sys
import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from help_info import *
from auth_info import *
from auth import *
import time
import random

sd='''
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
www-data:x:82:82:Linux User,,,:/home/www-data:/sbin/nologin
nginx:x:100:101:Linux User,,,:/var/cache/nginx:/sbin/nologin
'''


client = discord.Client()
bot = commands.Bot(command_prefix='!')
#extensions = ['settings','settings']
bot.remove_command('help')
blacklisted = []
words=['koti','punai kodi','koti enke','enakku koti tevai']
nic=['where is the flag','i need flag','need flag','flag','flag.txt']


# This is intended to be able to be circumvented.
# If you do something like report a bug with the report command (OR GITHUB), e.g, >report "a bug", you might be added to the list!


# TODO: ok so I was/am an idiot and kind of forgot that I was calling the updateDb function every time ctftime current, timeleft, and countdown are called...  so I should probably fix that.

# https://github.com/Rapptz/discord.py/blob/master/examples/background_task.py

@bot.event
async def on_ready():
    print(('<' + bot.user.name) + ' Online>')
    print(f"discord.py {discord.__version__}\n")
    #await bot.change_presence(activity=discord.Game(name='<help / <report "issue"'))

@bot.event
async def on_command_error(ctx, error):
    #await ctx.send(f"There was an error, sorry!\nIf you think this should be fixed, report it with >report \"what happened\"")
    print(Style.BRIGHT + Fore.RED + f"Error occured with: {ctx.command}\n{error}\n")
    print(Style.RESET_ALL)

# Sends the github link.
@bot.command()
async def source(ctx):
    await ctx.send(src)

@bot.command()
async def help(ctx, page=None):
    if (not page) or (page == '1'):
        page = '1'
        emb = discord.Embed(description=help_page_ctf, colour=8405748)
        #emb.set_author(name='<request "x" - request a feature')
           
    #await ctx.channel.send(embed=emb)
    await ctx.author.send(embed=emb)

# Bot sends a dm to creator with the name of the user and their report.
@bot.command()
async def flag(ctx,stri):
    #byted_str = str(stri)
    
    fl="Its just a welcome challenge here is your flag ` SUpDVEZ7SVQkX0p1c3RfQF9TaW1wbGVfV2VsY29tZV9CMFR9 `"
    out1="https://imgur.com/gallery/2fFit"
    #if stri == 'welcome':
    if any((name in stri for name in words)):
       await ctx.author.send(fl)
       await ctx.author.send(out1)
    
    elif any((name in stri for name in nic)):
        await ctx.author.send("Maybe check bot icon..")
        await ctx.author.send("https://imgur.com/gallery/z4kT3rq")

    elif (stri=="cat flag"):
        await ctx.author.send("Permition denied")

    elif (stri=="cat /etc/passwd"):
        await ctx.author.send(sd)
        await ctx.author.send("https://imgur.com/gallery/FtRbN6m")
    else:
        await ctx.author.send("Try Again.. ")
        await ctx.author.send("https://imgur.com/gallery/FtRbN6m")

@bot.command()
async def author(ctx, page=None):
    if (not page) or (page == '1'):
        page = '1'
        emb = discord.Embed(description=help_page_author, colour=8405748)
        #emb.set_author(name='<request "x" - request a feature')
      
    await ctx.channel.send(embed=emb)

if __name__ == '__main__':    
    bot.run(auth_token)
  
