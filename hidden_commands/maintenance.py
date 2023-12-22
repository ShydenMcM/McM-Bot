from discord.ext import commands


@commands.group()
async def maintenance(ctx: commands.Context):
    if ctx.invoked_subcommand is None:
        await ctx.reply("You must supply a command to run")


@maintenance.command(hidden=True)
@commands.is_owner()
async def sync(ctx: commands.Context):
    """Syncs slash commands to Discord
    Can only be run by the bot owner"""
    await ctx.bot.tree.sync()
    await ctx.send(f"{ctx.author.display_name} Synced Commands")


async def setup(bot):
    bot.add_command(sync)
