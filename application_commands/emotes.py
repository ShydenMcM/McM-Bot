from discord import Embed, Interaction, app_commands

from handlers.api import Kawaii

kawaii = Kawaii()


class Emote(app_commands.Group):
    pass


emote = Emote(description="A way to display your emotions")


@emote.command()
async def alarm(interaction: Interaction):
    """Wakey wakey"""
    embed = Embed().set_image(url=kawaii.get_gif("alarm"))
    embed.description = f":alarm_clock: {interaction.user.mention} it's time for school!"
    await interaction.response.send_message(embed=embed)


@emote.command()
async def amazed(interaction: Interaction):
    """It's Truly Amazing"""
    embed = Embed().set_image(url=kawaii.get_gif("amazing"))
    embed.description = f":exploding_head: {interaction.user.mention} Is so amazed!"
    await interaction.response.send_message(embed=embed)


@emote.command()
async def mad(interaction: Interaction):
    """You mad bro?"""
    embed = Embed().set_image(url=kawaii.get_gif("mad"))
    embed.description = f":face_with_symbols_over_mouth: {interaction.user.mention} Is so pissed!"
    await interaction.response.send_message(embed=embed)


@emote.command()
async def happy(interaction: Interaction):
    """When you're happy, and you truly want to show it"""
    embed = Embed().set_image(url=kawaii.get_gif("happy", excludes=[6]))
    embed.description = f":smile: {interaction.user.mention} is so happy! Don't you **DARE** ruin their mood!"
    await interaction.response.send_message(embed=embed)


@emote.command()
async def lonely(interaction: Interaction):
    """Nobody loves you"""
    embed = Embed().set_image(url=kawaii.get_gif("lonely"))
    embed.description = f":sob: {interaction.user.mention} is so lonely! Won't you give them a hug?"
    await interaction.response.send_message(embed=embed)


@emote.command()
async def shrug(interaction: Interaction):
    """When you really just don't care"""
    embed = Embed().set_image(url=kawaii.get_gif("shrug"))
    embed.description = f":person_shrugging: {interaction.user.mention} is unsure or just doesn't really care."
    await interaction.response.send_message(embed=embed)


@emote.command()
async def smug(interaction: Interaction):
    """You are feeling quite smug"""
    embed = Embed().set_image(url=kawaii.get_gif("smug"))
    embed.description = f":smirk: {interaction.user.mention} is looking so smug right now!"
    await interaction.response.send_message(embed=embed)


async def setup(bot):
    bot.tree.add_command(emote)
