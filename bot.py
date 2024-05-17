"""Bot"""

import asyncio
import logging
import discord

from discord import Guild, Message
from discord.ext import commands

import responder.owo
import settings
from background_tasks.guilds import (
    get_guild_from_db,
    is_active,
    perform_guild_check,
    perform_guilds_check,
    set_guild_active,
)

config = settings.Config().load()

if config.ENVIRONMENT == "PROD":
    discord.utils.setup_logging(level=logging.INFO, root=True)
else:
    discord.utils.setup_logging(level=logging.DEBUG, root=True)

intents: discord.Intents = discord.Intents(
    guilds=True,
    members=True,
    emojis=True,
    webhooks=True,
    presences=True,
    messages=True,
    reactions=True,
    message_content=True,
)


class Bot(commands.AutoShardedBot):
    """Prepares bot for use"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        self.loop.create_task(self.perform_checks())

    async def perform_checks(self):
        await self.wait_until_ready()
        while not self.is_closed():
            await asyncio.sleep(int(config.CHECK_INTERVAL))
            logging.info("%s seconds has elapsed, performing checks", int(config.CHECK_INTERVAL))
            await perform_guilds_check(self)


bot = Bot(
    command_prefix=commands.when_mentioned_or("mcm ", "mcm"),
    case_insensitive=True,
    intents=intents,
    status=config.Status,
    activity=discord.Activity(
        type=int(config.ACTIVITY_TYPE),  # type: ignore
        name=config.ACTIVITY_NAME,
    ),
)


@bot.event
async def on_command_error(ctx: commands.Context[Bot], error: str):
    logging.error(error)


@bot.event
async def on_ready():
    """Logging out bot information at startup"""
    logging.debug("Test DEBUG log")
    logging.warning("Test WARNING log")
    logging.error("Test ERROR log")
    logging.info("*******************************************************************")
    logging.info("%s", discord.version_info)

    for command_file in settings.HIDDEN_COMMANDS_DIR.glob("*.py"):
        if command_file.name != "__init__.py":
            command_name = command_file.name[:-3]
            print("loading hidden command: " + command_name)
            await bot.load_extension(f"hidden_commands.{command_name}")

    for command_file in settings.APPLICATION_COMMANDS_DIR.glob("*.py"):
        if command_file.name != "__init__.py":
            command_name = command_file.name[:-3]
            print("loading application command: " + command_name)
            await bot.load_extension(f"application_commands.{command_name}")
    bot.help_command = None
    await perform_guilds_check(bot)


@bot.event
async def on_member_join(member):
    logging.debug("'%s' system channel: '%s' Action: join", member.guild.name, member.guild.system_channel)
    if member.guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {member.guild.name}!'
        await member.guild.system_channel.send(to_send)


@bot.event
async def on_member_remove(member):
    logging.debug("'%s' system channel: '%s' Action: leave", member.guild.name, member.guild.system_channel)
    if member.guild.system_channel is not None:
        to_send = f'{member.mention} left the server!'
        await member.guild.system_channel.send(to_send)


@bot.event
async def on_message(message: Message):
    excluded_characters = ["http", "<", ">"]
    """Actions based on messages read"""
    message.content = message.content.lower()
    clean_message = message.clean_content.lower()
    if message.author == bot.user:
        return
    if message.author.id == 408785106942164992:
        await responder.owo.process_owo(message)

    if not any(banned_char in clean_message for banned_char in excluded_characters):
        if "69" in clean_message:
            await message.add_reaction("😏")
        if clean_message == "666":
            await message.add_reaction("😈")
        if clean_message == "420":
            await message.add_reaction("🪴")
    await bot.process_commands(message)


@bot.event
async def on_guild_join(guild: Guild):
    logging.info(f"{guild.name} has just joined")
    await perform_guild_check(guild, bot)


@bot.event
async def on_guild_remove(guild: Guild):
    logging.info(f"{guild.name} has left")
    db_query_result = await get_guild_from_db(guild.id)
    if await is_active(db_query_result):
        await set_guild_active(guild, False)


bot.run(str(config.BOT_TOKEN), root_logger=False)
