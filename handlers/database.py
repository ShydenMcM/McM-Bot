import asyncio
import logging

import aiomysql

import settings

config = settings.Config().load()


async def create_db_pool():
    pool = await aiomysql.create_pool(
        host=config.DB_HOST,
        port=int(config.DB_PORT),
        user=config.DB_USER,
        password=config.DB_PASS,
        db=config.DB_NAME,
        loop=asyncio.get_event_loop(),
        autocommit=True,
    )
    return pool


async def test_connection():
    logging.info("Opening Database Connection")
    result = await perform_query("SELECT * FROM users")
    if result is not None:
        logging.info("Connected to database")
    else:
        logging.error("Database connection test failed")


async def perform_query(query):
    db_pool = await create_db_pool()
    async with db_pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            logging.debug("Performing query: %s", query)
            await cur.execute(query)
            result = await cur.fetchall()
    db_pool.close()
    return result


def rows_affected(db_query_result):
    if len(db_query_result) == 0:
        return False
    return True
