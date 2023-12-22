from discord import Embed, Interaction, User, app_commands

from handlers.api import Kawaii

kawaii = Kawaii()


class Action(app_commands.Group):
    pass


action = Action(description="For when you want to do something")


@action.command()
async def bite(interaction: Interaction, user: User, reason: str = ""):
    """Bites a user"""
    embed = Embed().set_image(url=kawaii.get_gif("bite"))
    if user.bot:
        embed.description = (
            f":shark: Ouch! {interaction.user.mention} just bit a bot. "
            f"Do you normally try to bite things that don't physically exist?"
        )
    elif user.name != interaction.user.mention:
        embed.description = f":shark: Ouch! {interaction.user.mention} just bit {user.mention} {reason}!"
    if user.name == interaction.user.mention:
        embed.description = (
            f'{interaction.user.mention} just bit themself! ' f'They took the phrase "you are what you eat" too literally'
        )
    await interaction.response.send_message(embed=embed)


@action.command()
async def kiss(interaction: Interaction, user: User, reason: str = ""):
    """kisses a user"""
    embed = Embed().set_image(url=kawaii.get_gif("kiss"))
    if user.bot:
        embed.description = f":kissing_heart: {interaction.user.mention} kissed a bot. No wonder they can't get a date"
    elif user.name != interaction.user.mention:
        embed.description = f":kissing_heart: Aww {interaction.user.mention} just kissed {user.mention} {reason}!"
    else:
        embed.description = (
            f":kissing_heart: {interaction.user.mention} just kissed themself. " f"This shows just how lonely they are!"
        )
    await interaction.response.send_message(embed=embed)


@action.command()
async def kill(interaction: Interaction, user: User, reason: str = ""):
    """kills a user"""
    embed = Embed().set_image(url=kawaii.get_gif("kill"))
    if user.bot:
        embed.description = (
            f":dagger:  {interaction.user.mention} killed a bot. " f"This won't prevent apocalypse by machines though"
        )
    elif user.name != interaction.user.mention:
        embed.description = f":dagger:  Oh no! {interaction.user.mention} just killed {user.mention} {reason}!"
    else:
        embed.description = f":dagger: {interaction.user.mention} just killed themself. R.I.P."
    await interaction.response.send_message(embed=embed)


@action.command()
async def hug(interaction: Interaction, user: User, reason: str = ""):
    """hugs a user"""
    embed = Embed().set_image(url=kawaii.get_gif("hug"))
    if user.bot:
        embed.description = f":hugging: {interaction.user.mention} hugged a bot. That's how lonely they are!"
    elif user.name != interaction.user.mention:
        embed.description = f":hugging: So cute! {interaction.user.mention} just hugged {user.mention} {reason}!"
    else:
        embed.description = (
            f":hugging:  {interaction.user.mention} just hugged themself. Clearly nobody loves them, not even a bot."
        )
    await interaction.response.send_message(embed=embed)


@action.command()
async def lick(interaction: Interaction, user: User, reason: str = ""):
    """licks a user"""
    embed = Embed().set_image(url=kawaii.get_gif("lick"))
    if user.bot:
        embed.description = f":tongue: EWWW! {interaction.user.mention} just licked a bot! Disgusting!"
    elif user.name != interaction.user.mention:
        embed.description = f":tongue: OMG! {interaction.user.mention} just licked {user.mention} {reason}!"
    else:
        embed.description = f":tongue: {interaction.user.mention} just licked themself... They must be a cat"
    await interaction.response.send_message(embed=embed)


@action.command()
async def poke(interaction: Interaction, user: User, reason: str = ""):
    """Pokes a user"""
    embed = Embed().set_image(url=kawaii.get_gif("poke"))
    if user.bot:
        embed.description = f":point_right: {interaction.user.mention} just poked a bot. Why would you?"
    elif user.name != interaction.user.mention:
        embed.description = f":point_right: {interaction.user.mention} just poked {user.mention} {reason}!"
    else:
        embed.description = (
            f":point_right: {interaction.user.mention} just poked themself?" f" Did it hurt? or are they just hungry?"
        )
    await interaction.response.send_message(embed=embed)


@action.command()
async def stare(interaction: Interaction, user: User, reason: str = ""):
    """Stares at a user"""
    embed = Embed().set_image(url=kawaii.get_gif("stare"))
    if user.bot:
        embed.description = f":eyes: {interaction.user.mention} is staring at a bot. When will it do something?"
    elif user.name != interaction.user.mention:
        embed.description = f":eyes: {interaction.user.mention} is staring at {user.mention} with a serious gaze {reason}!"
    else:
        embed.description = (
            f":eyes: {interaction.user.mention} just stared at themself without a mirror. "
            f"Nobody knows how and more importantly, why?"
        )
    await interaction.response.send_message(embed=embed)


@action.command()
async def wave(interaction: Interaction, user: User, reason: str = ""):
    """wave at a user"""
    embed = Embed().set_image(url=kawaii.get_gif("wave"))
    if user.bot:
        embed.description = (
            f":wave: {interaction.user.mention} just waved at {user.name}. "
            f"Even though it's just a bot and can't wave back... Wierd!"
        )
    elif user.name != interaction.user.mention:
        embed.description = f":wave: {interaction.user.mention} just waved at {user.mention}. {reason}!"
    else:
        embed.description = f":wave: That's right {interaction.user.mention}, wave at yourself. Because nobody else will?"
    await interaction.response.send_message(embed=embed)


@action.command()
async def wink(interaction: Interaction, user: User, reason: str = ""):
    """Wink at a user"""
    embed = Embed().set_image(url=kawaii.get_gif("wink"))
    if user.bot:
        embed.description = (
            f":wink: {interaction.user.mention} is winking at a bot... " f"Well, whatever rocks your boat I guess"
        )
    elif user.name != interaction.user.mention:
        embed.description = f":wink: {interaction.user.mention} is winking at {user.mention}. {reason}!"
    else:
        embed.description = (
            f":wink: {interaction.user.mention}, just winked at themself. " f"They must really think they're sexy"
        )
    await interaction.response.send_message(embed=embed)


async def setup(bot):
    bot.tree.add_command(action)
