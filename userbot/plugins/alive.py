from math import ceil
import json
import random
import re
from telethon import events, errors, custom, functions, __version__
from userbot import CMD_LIST
import io
import asyncio, os
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, UPSTREAM_REPO_BRANCH
from userbot.utils import admin_cmd
import platform
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version, uname
from shutil import which

import psutil
from telethon import __version__, version

from userbot import CMD_HELP, StartTime, bot
from userbot.events import register


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time

@register(outgoing=True, pattern=r"^\.(?:alive|on)\s?(.)?")
async def _(alive):
    """ For .on command, check if the bot is running.  """
    uptime = await get_readable_time((time.time() - StartTime))
    IMG = Config.ALIVE_IMG
    if IMG is None:
        IMG = "https://drive.google.com/uc?id=1BWR-nhFNe8oupi-4SoySVEJWn_G6QsaL&export=download"
    Alive_caption = (
         "` ---͓̽-͓̽ ͓̽I͓̽R͓̽O͓̽N͓̽-͓̽B͓̽O͓̽T͓̽ ͓̽-͓̽-͓̽--`\n"
         "╭━━━━━━━━━━━━━━━━━━━╮\n"
        f"┣[•👤 `USER     :` {DEFAULTUSER}\n"
        f"┣▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n"
        f"┣[•🐍 `Python.  : v.{python_version()}`\n"
        f"┣[•⚙️ `Telethon : v.{version.__version__}`\n"
        f"┣[•💡 `Base on  : {UPSTREAM_REPO_BRANCH}`\n"
        f"┣[•🕒 `Uptime.  : {uptime}`\n"
        f"╰━━━━━━━━━━━━━━━━━━━╯\n"
    )
    await bot.send_file(alive.chat_id, IMG, caption=Alive_caption)
    await alive.delete()


