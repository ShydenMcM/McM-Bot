from discord import Message

from handlers.api import Tenor

tenor = Tenor()


async def process_owo(message: Message):
    if message.content == '' or message.content is None:
        print("Embed from OwO detected")
        with open("./owo/incoming_embeds.txt", "ab") as f:
            f.write(str(message.embeds.pop().to_dict()).encode("utf-8") + "\n".encode("utf-8"))
        await process_owo_embed(message)
    else:
        print("Message from OwO detected")
        with open("./owo/incoming_messages.txt", "ab") as f:
            f.write(message.content.encode("utf-8") + "\n".encode("utf-8"))
        await process_owo_message(message)
    f.close()


async def process_owo_embed(message: Message):
    return


async def process_owo_message(message: Message):
    if "** sacrificed **" in message.content:
        await message.reply(tenor.search_gif("murderer"))
