import asyncio

from discord import Message

from handlers.api import Tenor

tenor = Tenor()


async def wait(seconds: int):
    await asyncio.sleep(seconds)


async def process_owo(message: Message):
    if (message.content == '' or message.content is None) and len(message.embeds) >= 0:
        print("Embed from OwO detected")
        await process_owo_embed(message)
        with open("./owo/incoming_embeds.txt", "ab") as f:
            f.write(str(message.embeds.pop().to_dict()).encode("utf-8") + "\n".encode("utf-8"))
    else:
        print("Message from OwO detected")
        await process_owo_message(message)
        with open("./owo/incoming_messages.txt", "ab") as f:
            f.write(message.content.encode("utf-8") + "\n".encode("utf-8"))
    f.close()


async def process_owo_embed(message: Message):
    fetched_message = None
    current_message = message
    while fetched_message != current_message:
        print("Embeds don't match")
        await wait(3)
        fetched_message = await message.fetch()
    message = fetched_message
    embed_description = message.embeds.pop().to_dict()
    print(embed_description)
    if "You lost your streak of " in embed_description.get("footer").get("text"):
        await message.reply(tenor.search_gif("fail"))
    if embed_description.get("description") is not None:
        if "You earned 1,000 <:cowoncy:416043450337853441>" in embed_description.get("description"):
            await message.reply(tenor.search_gif("applause"))


async def process_owo_message(message: Message):
    if "** sacrificed **" in message.content:
        await message.reply(tenor.search_gif("murderer"))
    if "** for a total of **" in message.content and "** sold **" in message.content:
        await message.reply(tenor.search_gif("rich"))
