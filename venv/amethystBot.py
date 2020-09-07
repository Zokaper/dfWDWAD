import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="a.")
bot.remove_command("help")



# =======================================================================================
#Events
@bot.event
async def on_ready():
    print("bot is ready")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("ERROR: That command does not exist")


@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general', guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}, my name is Amethyst! Do [a.help] to get started'.format(guild.name))

# =======================================================================================
# Commands
@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")


@bot.command()
async def hi(ctx):
    await ctx.send("Hello!")
    

@bot.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(bot.latency * 1000)}ms")
    

@bot.command()
async def ask(ctx, *, question):
    responses = ["yes", "no"]
    await ctx.send(f"{question} \nAnswer: {random.choice(responses)}")
    

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, *, amount):
    await ctx.channel.purge(limit=int(amount) + 1)
    

@bot.command()
async def help(ctx):
    helpEmbed = discord.Embed(
        title="Amethyst Bot Help",
        description="",
        color=discord.colour.Color.orange()
    )
    helpEmbed.add_field(name="Prefix:", value="a.", inline=False)
    helpEmbed.add_field(name="Commands:", value="hi, hello, ping, ask [question]", inline=False)

    await ctx.send(embed=helpEmbed)
    

@bot.command()
@commands.has_role("Admin")
async def say(ctx, *, tosay):
    await ctx.message.delete()
    await ctx.send(tosay)
# =======================================================================================
# Error Messages
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("ERROR: Please specify the amount of messages to clear")


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ERROR: You do not have permission to use this command")


# =======================================================================================


bot.run("NzUyNDE1NTg0ODQyNDE2MTY5.X1XTng.Gh3pbFYBnNfu6lIDN_lMkbqDCpY")