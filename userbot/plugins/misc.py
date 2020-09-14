from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd
from telethon import events
from datetime import datetime
from telethon.utils import pack_bot_file_id
from re import findall
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from requests import get
from urllib.parse import quote_plus
from urllib.error import HTTPError
from google_images_download import google_images_download
from gsearch.googlesearch import search
from search_engine_parser import GoogleSearch
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
from userbot import bot
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import command, remove_plugin, load_module
from var import Var
from pathlib import Path
from userbot import LOAD_PLUG
import traceback
import userbot.utils

from telethon import events
from userbot import CMD_HELP, bot
from covid import Covid
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="corona(?: |$)(.*)"))
async def corona(event):
    if event.pattern_match.group(1):
        country = event.pattern_match.group(1)
    else:
        country = "World"
    covid = Covid(source="worldometers")
    data = ""
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data['confirmed'] + country_data['new_cases']
        hmm2 = country_data['deaths'] + country_data['new_deaths']
        data += f"\n⚠️Confirmed.   : `{hmm1}`"
        data += f"\n😔Active.           : `{country_data['active']}`"
        data += f"\n⚰️Deaths.          : `{hmm2}`"
        data += f"\n🤕Critical.          : `{country_data['critical']}`"
        data += f"\n😊Recovered     : `{country_data['recovered']}`"
        data += f"\n💉Total tests     : `{country_data['total_tests']}`"
        data += f"\n🥺New Cases    : `{country_data['new_cases']}`"
        data += f"\n😟New Deaths   : `{country_data['new_deaths']}`"
    else:
        data += "\nNo information yet about this country!"
    await borg.send_message(event.chat_id, "**Corona Virus Info in {}:**\n{}".format(country.capitalize(), data))
    await event.delete()

CMD_HELP.update({"coronavirus":
                 "`.covid ` <country name>\
   \n**USAGE :** Get an information about covid-19 data in the given country."
                 })

@borg.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.ping` me or `.helpme` to check if I am online")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.ping` me or `.helpme` to check if I am online")
    # await asyncio.sleep(2)
    await event.edit("Restarted. `.ping` me or `.helpme` to check if I am online Actually It Takes 2-3 Mintues Or Depending On Speed Of Heroku To Restart")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@borg.on(admin_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Shutting Down 😭 Turn Me On From heroku If You Dont Know How To Do That Join @Sensible_userbot And Ask In Discussion")
    await borg.disconnect()


@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!\n{}".format(ms))


@borg.on(admin_cmd(pattern="ls ?(.*)"))
async def lst(event):
	if event.fwd_from:
		return
	input_str = event.pattern_match.group(1)
	if input_str:
		msg = "**Files in {} :**\n".format(input_str)
		files = os.listdir(input_str)
	else:
		msg = "**Files in Current Directory :**\n"
		files = os.listdir(os.getcwd())
	for file in files:
		msg += "`{}`\n".format(file)
	if len(msg) <= Config.MAX_MESSAGE_SIZE_LIMIT:
		await event.edit(msg)
	else:
		msg = msg.replace("`","")
		out = 'filesList.txt'
		with open(out,'w') as f:
			f.write(f)
		await borg.send_file(
				event.chat_id,
				out,
				force_document=True,
				allow_cache=False,
				caption="`Output is huge. Sending as a file...`"
		)
		await event.delete()	



def progress(current, total):
    logger.info("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))


@borg.on(admin_cmd("go (.*)"))
async def gsearch(q_event):
    """ For .google command, do a Google search. """
    match = q_event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await q_event.edit("**Search Query:**\n`" + match + "`\n\n**Results:**\n" +
                       msg,
                       link_preview=False)



@borg.on(admin_cmd("get_id"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        chat = await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(str(event.chat_id), str(r_msg.from_id), bot_api_file_id))
        else:
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`".format(str(event.chat_id), str(r_msg.from_id)))
    else:
        await event.edit("Current Chat ID: `{}`".format(str(event.chat_id)))



@borg.on(admin_cmd("get_ad?(m)in ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Admins in this Channel**: \n"
    should_mention_admins = False
    reply_message = None
    pattern_match_str = event.pattern_match.group(1)
    if "m" in pattern_match_str:
        should_mention_admins = True
        if event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
    input_str = event.pattern_match.group(2)
    to_write_chat = await event.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions_heading = "Admins in {} channel: \n".format(input_str)
        mentions = mentions_heading
        try:
            chat = await borg.get_entity(input_str)
        except Exception as e:
            await event.edit(str(e))
            return None
    try:
        async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
            if not x.deleted:
                if isinstance(x.participant, ChannelParticipantCreator):
                    mentions += "\n 🔱 [{}](tg://user?id={}) `{}`".format(x.first_name, x.id, x.id)
        mentions += "\n"
        async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
            if not x.deleted:
                if isinstance(x.participant, ChannelParticipantAdmin):
                    mentions += "\n 🥇 [{}](tg://user?id={}) `{}`".format(x.first_name, x.id, x.id)
            else:
                mentions += "\n `{}`".format(x.id)
    except Exception as e:
        mentions += " " + str(e) + "\n"
    if should_mention_admins:
        if reply_message:
            await reply_message.reply(mentions)
        else:
            await event.reply(mentions)
        await event.delete()
    else:
        await event.edit(mentions)


@command(pattern="^.extdl", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    chat = Var.PLUGIN_CHANNEL
    documentss = await borg.get_messages(chat, None , filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    await event.delete()
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(await borg.get_messages(chat, ids=mxo), "userbot/plugins/")
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            await borg.send_message(event.chat_id, "Installed Plugin `{}` successfully.".format(os.path.basename(downloaded_file_name)))
        else:
            await borg.send_message(event.chat_id, "Plugin `{}` has been pre-installed and cannot be installed.".format(os.path.basename(downloaded_file_name)))

import logging

from uniborg.util import admin_cmd

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
import asyncio
logger = logging.getLogger(__name__)



if 1 == 1:
    name = "Profile Photos"
    client = borg

    @borg.on(admin_cmd(pattern="poto ?(.*)"))
    async def potocmd(event):
        """Gets the profile photos of replied users, channels or chats"""
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
            u = True
        else:
            photos = await event.client.get_profile_photos(chat)
            u = False
        if id.strip() == "":
            if len(photos) > 0:
                await event.client.send_file(event.chat_id, photos)
                await event.delete()
            else:
                try:
                    if u is True:
                        photo = await event.client.download_profile_photo(user.sender)
                    else:
                        photo = await event.client.download_profile_photo(event.input_chat)
                    await event.delete()
                    await event.client.send_file(event.chat_id, photo)
                except a:
                    await event.edit("**This user has no photos.\nGEYYYY!**")
                    return
        else:
            try:
                id = int(id)
                if id <= 0:
                    await event.edit("```ID number Invalid!``` **Are you Comedy Me ?**")
                    return
            except:
                 await event.edit("`Are you comedy me ?`")
                 return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await event.delete()
                await event.client.send_file(event.chat_id, send_photos)
            else:
                await event.edit("```No photo found of this NIBBI. Now u Die!```")
                await asyncio.sleep(8)
                return

from asyncio import sleep
from random import choice, getrandbits, randint
import re
from re import sub
import random
from os import execl
import time
from telethon import events
from userbot import bot
from collections import deque
import requests
import sys
import os
import io
import html
import json
from PIL import ImageEnhance, ImageOps

from userbot import CMD_HELP
from userbot.events import register



EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats 
    "]+")


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, '', inputString)


@register(outgoing=True, pattern="^.waifu(?: |$)(.*)")

async def waifu(animu):
#"""Creates random anime sticker!"""

    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await animu.edit("`You haven't written any article, Waifu is going away.`")
            return
    animus = [1, 3, 7, 9, 13, 22, 34, 35, 36, 37, 43, 44, 45, 52, 53, 55]
    sticcers = await bot.inline_query(
        "stickerizerbot", f"#{random.choice(animus)}{(deEmojify(text))}")
    await sticcers[0].click(animu.chat_id,
                            reply_to=animu.reply_to_msg_id,
                            silent=True if animu.is_reply else False,
                            hide_via=True)
    await animu.delete()
    
    
    CMD_HELP.update({
    'waifu':
    ".waifu : Anime that makes your writing fun."
})
