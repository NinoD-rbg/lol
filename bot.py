import discord
from discord.ext import commands
from random import randint
from dotenv import load_dotenv
import os
import asyncio
from asyncio import sleep
import typing
from discord import User, errors
import time
#import utils.json
#from utils.document import document


load_dotenv()


client = commands.Bot(command_prefix="-")
client.remove_command('help')

async def status():
  while True:
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = f"{len(client.guilds)} servers"))
    await sleep(10)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="https://discord.gg/tTfK7XDXTv", type=3))
    await sleep(10)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Type -help for a list of commands!", type=3))
    await sleep(10)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Version 1.0.4", type=3))
    await sleep(10)

@client.event
async def on_ready():
  print("Bot connected")
  client.loop.create_task(status())

@client.command()
async def testwarn(ctx, member : discord.Member, *, reason=None):
    embed=discord.Embed(title="testWarn", description=f"{member} has been testwarned by TheFish_YouTube**#9537** for {reason} \n\nWarning **1**.")
  
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
  await ctx.send('Pong!')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await ctx.channel.purge(limit=1)
  await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await ctx.channel.purge(limit=1)
  await member.ban(reason=reason)
  await ctx.send(f"{member} banned.")

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.channel.purge(limit=1)
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}!')

            # Auto-log Settings (Edit for each command)
            Command_Type = "[S] Staff"
            Command_Name = "-unban [Member] [Reason]"
            Command_Usage = f"Unbanned {user.name}#{user.discriminator}"
            Command_Sent = f"{ctx.channel.name}"
  
            BotLogEmbed = discord.Embed(
    
              title = f"Auto-Generated Command Log: {Command_Name}",
              colour = ctx.author.color
  
            )
            BotLogEmbed.add_field(name = f"Member Name:",value = f"`{ctx.author.name}`", inline = False)
            BotLogEmbed.add_field(name = f"User ID:",value = f"`{ctx.author.id}`", inline = False)
            BotLogEmbed.add_field(name = f"Type:",value = f"`{Command_Type}`", inline = False)
            BotLogEmbed.add_field(name = f"Command:",value = f"`{Command_Name}`", inline = False)
            BotLogEmbed.add_field(name = f"Msg ID:",value = f"`{ctx.message.id}`", inline = False)
            BotLogEmbed.add_field(name = f"Usage:",value = f"`{Command_Usage}`", inline = False)
            BotLogEmbed.add_field(name = f"Sent:",value = f"`{Command_Sent}`", inline = False)
            BotLogEmbed.add_field(name = f"Channel:",value = f"`{ctx.channel.name}`", inline = False)
            BotLogEmbed.add_field(name = f"Server:",value = f"`{ctx.guild.name}`", inline = False)
            BotLogEmbed.add_field(name = f"Date & Time:",value = f"`{ctx.message.created_at}`", inline = False)
  
            BotLogsChannel1 = client.get_channel(798181003888820224)
            await BotLogsChannel1.send(embed = BotLogEmbed)

            return

@client.command(aliases=['cmds'])
async def help(ctx):
    
    print(f'{ctx.author} has used the help command')
    """Shows all the bots in the server. Perms: Member+"""
    embed = discord.Embed(
        title = 'Commands',
        description = 'A list of all commands for the bot.',
        colour = discord.Colour.dark_purple()
        )

    embed.set_footer(text=f'For additional support join the Bot Server. https://discord.gg/tTfK7XDXTv')
    embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/lined-help/48/a-07-512.png')
    embed.set_author(name='Value')
    


    embed.add_field(name=f'-helpcommands', value='Bot direct messages you the commands list', inline=False)
    embed.add_field(name=f'-clear', value='Clears the amount of messages as said.', inline=True)
    embed.add_field(name=f'-unban', value='Unbans the member specified. Must included discriminator. (ex: idk#0000)', inline=True)
    embed.add_field(name=f'-ban', value='Bans the specified member for a specified reason. (if no reason is said, it is auto put as None.)', inline=True)
    embed.add_field(name=f'-sm', value='Bot direct messages you the commands list', inline=True)
    embed.add_field(name=f'-shutdownbot', value='Shutdowns the bot for the specified reason.', inline=True)
    embed.add_field(name=f'-userinfo', value='Checks userinfo for the specified user.', inline=True)
    embed.add_field(name=f'-kick', value='Kicks the user specified for the specified reason. (if no reason is said, it is auto put as None.)', inline=True)
    embed.add_field(name=f'-whatsnew', value='Shows a list of what is new in the bot version update.', inline=True)
    embed.add_field(name=f'-version', value='Checks the version of which the bot is updated on.', inline=True)
    embed.add_field(name=f'-invite', value='Shows the invite link to the main server/support server. (self promotion! :O)', inline=True)
    embed.add_field(name=f'-testban', value='Tests if the ban command works or not. (I recommend to test it on an alt or different before banning.)', inline=True)
    embed.add_field(name=f'-tban', value='tempbans the specified user for the specified reason. (if no reason is said, it is auto put as None.)', inline=True)
    embed.add_field(name=f'-ping', value='Tests the bot to see if the bot works and is online.', inline=True)
    embed.add_field(name=f'-prefix', value='Shows the prefix of the bots commands.', inline=True)

    await ctx.author.send(embed = embed)

    cmdembed = discord.Embed(

        title = "You've Got Mail!",
        colour = discord.Colour.dark_purple()
        
        )
    cmdembed.add_field(name = "I have sent the commands to your direct messages to avoid chat spam.", value = "For more support with questions you may have, join the official server: https://discord.gg/tTfK7XDXTv")

@client.command(aliases=['p'])
async def prefix(ctx):
    
    print(f'{ctx.author} has used the prefix command')
    """Shows all the bots in the server. Perms: Member+"""
    embed = discord.Embed(
        title = 'Prefix',
        description = 'A prefix for the bot.',
        colour = discord.Colour.dark_purple()
        )

    embed.set_footer(text=f'For additional support join the Bot Server. https://discord.gg/tTfK7XDXTv')
    embed.set_author(name='Value')



    embed.add_field(name=f'1', value='-', inline=False)

    await ctx.author.send(embed = embed)

@client.command()
async def pong(ctx):
  await ctx.send('Ping!')

@client.command()
async def tban(ctx, user:discord.User, duration: int):
    await ctx.guild.ban(user)
    await asyncio.sleep(duration)
    await ctx.guild.unban(user)

@client.command()
async def testban(ctx, member : discord.Member, *, reason=('Spam')):
  await ctx.channel.purge(limit=1)
  await ctx.send(f"User {member} was test banned.")

@client.command()
async def version(ctx):
  await ctx.send('Value is on version 1.0.5, coded with discord.py.\nType `-whatsnew` for more info.')

@client.command()
async def sm(ctx, seconds: int):
    await ctx.channel.purge(limit=1)
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

@client.command()
async def hello(ctx):
  await ctx.send("Hello!")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=1)
    await ctx.channel.purge(limit=amount)

@client.command()
async def whatsnew(ctx):
  await ctx.send('Version 1.0.5 new hotfix!\nImproved bot sometimes going offline\nBug where unban would not work\n`Version 1.0.5, 1.20.2021`')

@client.command()
async def update(ctx):
  await ctx.channel.purge(limit=1)
  await ctx.send('Updated to version 1.0.5 succesfully.')
  
@client.command()
async def invite(ctx):
 await ctx.channel.purge(limit=1)
 await ctx.send('Support Server: https://discord.gg/tTfK7XDXTv')

@client.command(aliases=['info'])
async def userinfo(ctx, *, member: discord.Member = None):
    print(f'{ctx.author} has used the userinfo command')
    member = ctx.author if not member else member


    roles = [role for role in member.roles]


    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info: {member}")
    embed.set_thumbnail(url=member.avatar_url)
    
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Member Name (Server):", value=member.display_name)
    embed.add_field(name="Account created on:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p GMT/BST"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p GMT/BST"))

    embed.add_field(name=f"Roles: ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Highest role:", value=member.top_role.mention)

    embed.add_field(name="Member is a bot?", value=member.bot)

    await ctx.send(embed=embed)

@client.command(aliases=['shutdown'])
@commands.is_owner()
async def shutdownbot(ctx, *, reason = "N/A"):
    deleted = await ctx.message.channel.purge(limit=1)
    
    """Shuts down down the bot. Perms: Developer"""
    embed2 = discord.Embed(
        title = 'Bot Shutting Down',
        colour = discord.Colour.red()
        )
    embed2.add_field(name="Shutting down...", value = f'Reason: {reason}')
    embed2.set_thumbnail(url = "https://maxcdn.icons8.com/Share/icon/ultraviolet/computer_hardware/shutdown1600.png")

    FirstEmbed = await ctx.send(embed = embed2)

    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Shutting Down...'))
    
    time.sleep(5)
    
    await client.change_presence(status=discord.Status.offline, activity=discord.Game('Offline'))
    await FirstEmbed.message.channel.purge()

@client.command(aliases=['Echo','e','E'])
async def echo(ctx, *, message):
  deleted = await ctx.message.channel.purge(limit=1)
  await ctx.message.channel.send(f'{message}')

  


client.run(os.getenv("DISCORD_TOKEN"))