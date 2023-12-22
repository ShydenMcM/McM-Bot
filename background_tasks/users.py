import logging

import discord

import settings
from handlers.database import perform_query, rows_affected

config = settings.Config().load()
DB_NAME = config.DB_NAME


async def get_user_from_db(member_id):
    query = f"SELECT * FROM users WHERE ID = {member_id}"
    result = await perform_query(query)
    return result


async def add_new_user(member):
    query = f"INSERT INTO users (ID, BANNED) " f"VALUES ('{member.id}', 0)"
    result = await perform_query(query)
    return result


async def is_user_banned(db_query_result):
    record = db_query_result[0]
    if record["BANNED"] == 1:
        logging.debug("Banned = True")
        return True
    logging.debug("Banned = False")
    return False


async def perform_user_check(member: discord.Member):
    logging.info("Checking user: %s (id: %s)", member.name, member.id)
    db_query_result = await get_user_from_db(member.id)
    if not rows_affected(db_query_result):
        logging.debug(f"{member.name} (id: {member.id}) does not exist in Database, a new record will be created.")
        await add_new_user(member)
    else:
        logging.debug(f"{member.name} already exists in Database.")
        if await is_user_banned(db_query_result):
            logging.warning("User \"%s(ID:%s) is BANNED", member.name, member.id)
