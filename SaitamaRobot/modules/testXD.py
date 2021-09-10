from telethon import filters
import asyncio
from SaitamaRobot import pbot as app

@app.on.message (filter.command('ppromote'))

async def Owner(Lol):

    m = await (Lol, "**PROMOTING USER..**")
    await asyncio.sleep(1)
    await m.edit("**Making My DEV...**")
    await asyncio.sleep(1)
    await m.edit("**GIVING RIGHTS**")
    await asyncio.sleep(1)
    await m.edit("**PROMOTED USER SUCCESSFULLY TO DRAGON DISASTER**")

