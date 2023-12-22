import logging

import discord

import settings
from background_tasks.users import perform_user_check
from handlers.database import perform_query, rows_affected

config = settings.Config().load()
DB_NAME = config.DB_NAME


async def get_guild_member_from_db(member_id, guild_id):
    query = f"SELECT * FROM guild_members WHERE ID = {member_id} AND GUILD_ID = {guild_id}"
    result = await perform_query(query)
    return result


async def add_new_guild_member(guild, member):
    query = (
        f"INSERT INTO guild_members (ID, GUILD_ID, XP, BUMPS, BOOSTER, COUNT_FAILS, LAST_ACTIVE) "
        f"VALUES ('{member.id}', '{guild.id}', 0, 0, 0, 0, NOW())"
    )
    result = await perform_query(query)
    return result


async def perform_guild_member_check(guild: discord.Guild, member: discord.Member):
    if not member.bot:
        logging.info("Checking Guild (%s) member: %s (id: %s)", guild.name, member.name, member.id)
        db_query_result = await get_guild_member_from_db(member.id, guild.id)
        if not rows_affected(db_query_result):
            logging.debug(f"{member.name} does not exist in Database, a new record will be created.")
            await add_new_guild_member(guild, member)


async def perform_guild_members_checks(guild):
    logging.info("Performing Guild members checks")
    guild_members = guild.members
    for member in guild_members:
        if not member.bot:
            await perform_user_check(member)
            await perform_guild_member_check(guild, member)
