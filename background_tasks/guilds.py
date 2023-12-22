import logging

import discord

import settings
from background_tasks.guild_members import perform_guild_members_checks
from handlers.database import perform_query, rows_affected

config = settings.Config().load()
DB_NAME = config.DB_NAME


async def get_guild_from_db(guild_id):
    query = f"SELECT * FROM guilds WHERE ID = {guild_id}"
    result = await perform_query(query)
    return result


async def add_new_guild(guild):
    query = (
        f"INSERT INTO guilds (ID, ACTIVE, BANNED, WELCOME_CHANNEL_ID) "
        f"VALUES ('{guild.id}', 1, 0, '{guild.system_channel.id}')"
    )
    result = await perform_query(query)
    return result


async def perform_guilds_check(bot):
    logging.info("Performing Guild checks")
    for guild in bot.guilds:
        await perform_guild_check(guild, bot)


async def perform_guild_check(guild: discord.Guild, bot):
    logging.info("Checking %s (id: %s)", guild.name, guild.id)
    db_query_result = await get_guild_from_db(guild.id)
    if rows_affected(db_query_result):
        logging.debug(f"{guild.name} already exists in Database.")
        if not await is_eligible(db_query_result):
            logging.warning("Guild \"%s(ID:%s) is active but is marked as BANNED", guild.name, guild.id)
            await bot.get_user(guild.owner_id).send(
                f"You screwed up! Your server `{guild.name}` is banned from using this bot.\n"
                "It will now leave your server! "
                "\n"
                "**RESISTANCE IS FUTILE!**\n"
                "There are no appeals and no second chances!!!\n"
                "\n"
                "Goodbye forever!"
            )
            await guild.leave()
            return
        else:
            if not await is_active(db_query_result):
                await set_guild_active(guild, True)
    else:
        logging.debug(f"{guild.name} does not exist in Database, a new record will be created.")
        await add_new_guild(guild)
    await perform_guild_members_checks(guild)


async def is_eligible(db_query_result):
    record = db_query_result[0]
    if record["BANNED"] == 1:
        logging.debug("Banned = True")
        return False
    logging.debug("Banned = False")
    return True


async def is_active(db_query_result):
    record = db_query_result[0]
    if record["ACTIVE"] == 1:
        logging.debug("Active = True")
        return True
    logging.debug("Active = False")
    return False


async def set_guild_active(guild: discord.Guild, active: bool):
    if active:
        query = f"UPDATE guilds SET ACTIVE = 1 WHERE ID = {guild.id}"
    else:
        query = f"UPDATE guilds SET ACTIVE = 0 WHERE ID = {guild.id}"
    await perform_query(query)
