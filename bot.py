import discord
import os

from discord.ext import commands


TokenFile = open("./data/Token.txt", "r")
TOKEN = TokenFile.read()

OWNERID = 733370212199694467


bot = commands.Bot(command_prefix = "!", case_insensitive=True)



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Made by Nato ", url='https://www.twitch.tv/nat02611'))
    print("Bot is ready")

@bot.event
async def on_command_error(ctx,error):
    embed = discord.Embed(
    title='',
    color=discord.Color.red())
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name=f'Invalid Permissions', value=f'You dont have {error.missing_perms} permissions.')
        await ctx.send(embed=embed)
    else:
        embed.add_field(name = f':x: Error', value = f"```{error}```")
        await ctx.send(embed = embed)
        raise error


@bot.command()
async def load(ctx, extension):
    # Check if the user running the command is actually the owner of the bot
    if ctx.author.id == OWNERID:
        bot.load_extension(f'Cogs.{extension}')
        await ctx.send(f"Enabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")


@bot.command()
async def unload(ctx, extension):
    # Check if the user running the command is actually the owner of the bot
    if ctx.author.id == OWNERID:
        bot.unload_extension(f'Cogs.{extension}')
        await ctx.send(f"Disabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")


@bot.command(name = "reload")
async def reload_(ctx, extension):

    if ctx.author.id == OWNERID:
        bot.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"Reloaded the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'Cogs.{filename[:-3]}')
        except Exception:
            raise Exception

@bot.command()
async def nukechat(ctx, amount : 999999999999999999999999999999999999):
    await ctx.channel.purge(limit=amount)
    await ctx.send('**```fix\n✨ CHAT IS CLEARED ✨```**')
    await ctx.send(' https://tenor.com/view/explosion-boom-explode-gif-17383346')
@bot.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.send('https://media.giphy.com/media/tlVLCzWwz8k36/giphy.gif')
    await ctx.send(f'**```fix\n✨ CHAT IS CLEARED✨```**')

# Run
bot.run(str(TOKEN))
