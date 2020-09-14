from telethon import events
from io import BytesIO
from PIL import Image
import asyncio
import datetime
from collections import defaultdict
import math
import os
import requests
import zipfile
import io
import random
import textwrap
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
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

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import StickersetInvalidError
from telethon.errors import MessageNotModifiedError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    InputMediaUploadedDocument,
    InputPeerNotifySettings,
    InputStickerSetID,
    InputStickerSetShortName,
    MessageMediaPhoto
)
from datetime import datetime
import requests
from userbot.utils import progress
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, CUSTOM_STICKER_PACK_NAME, CUSTOM_ANIMATED_PACK_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Who is this"
CUSTOM_STICKER_NAME =str(CUSTOM_STICKER_PACK_NAME) if CUSTOM_STICKER_PACK_NAME else "My Boss SensibleUB Volume Pack One"
CUSTOM_ANIME_PACK = str(CUSTOM_ANIMATED_PACK_NAME) if CUSTOM_ANIMATED_PACK_NAME else "My Boss Animated Pack"
FILLED_UP_DADDY = "Invalid pack selected."
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

@borg.on(admin_cmd(pattern=r"qbot(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Reply to text message```")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Making a Quote```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @QuotLyBot and try again```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.delete()   
             await bot.forward_messages(event.chat_id, response.message)

@borg.on(admin_cmd(pattern="kang ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.is_reply:
        await event.edit("Reply to a photo to add to my personal sticker pack.")
        return
    reply_message = await event.get_reply_message()
    sticker_emoji = "💎"
    input_str = event.pattern_match.group(1)
    if input_str:
        sticker_emoji = input_str

    user = await bot.get_me()
    if not user.username:
        user.username = user.id
    pack = 1
    userid = event.from_id
    #packname = f"SensibleUB PACK"
    #packshortname = f"FRIDAY_{userid}_ns"  # format: Uni_Borg_userid
    if userid == 709723121:
        packname = f"Ceo's Packk 🎭"
        packshortname = "ceowhitehatcracks_pack_UB"
    else:
        packname = f"{user.username}'s {pack}"
        packshortname = f"Sensible_Userbot_{userid}_Pack"
    await event.edit("`Thats A Nice Sticker ! I Am Taking It In My Pack`")

    is_a_s = is_it_animated_sticker(reply_message)
    file_ext_ns_ion = "@Sensible_Userbot.png"
    file = await borg.download_file(reply_message.media)
    uploaded_sticker = None
    if is_a_s:
        file_ext_ns_ion = "AnimatedSticker.tgs"
        uploaded_sticker = await borg.upload_file(file, file_name=file_ext_ns_ion)
        if userid == 709723121:
            packname = f"Ceo's Packk 🎭"
            packshortname = "ceowhitehatcracks_pack_UB"
        else:
            packname = f"{user.username}'s {pack}"
            packshortname = f"@Sensible_Userbot_{userid}" # format: Uni_Borg_userid
    elif not is_message_image(reply_message):
        await event.edit("Invalid message type")
        return
    else:
        with BytesIO(file) as mem_file, BytesIO() as sticker:
            resize_image(mem_file, sticker)
            sticker.seek(0)
            uploaded_sticker = await borg.upload_file(sticker, file_name=file_ext_ns_ion)

    await event.edit("Packing To Your Pack ! Please Wait!")

    async with borg.conversation("@Stickers") as bot_conv:
        now = datetime.datetime.now()
        dt = now + datetime.timedelta(minutes=1)
        if not await stickerset_exists(bot_conv, packshortname):
            await event.edit("`Creating a new pack!`")
            await silently_send_message(bot_conv, "/cancel")
            if is_a_s:
                response = await silently_send_message(bot_conv, "/newanimated")
            else:
                response = await silently_send_message(bot_conv, "/newpack")
            if "Yay!" not in response.text:
                await event.edit(f"**Error**! @Stickers replied: {response.text}")
                return
            response = await silently_send_message(bot_conv, packname)
            if not response.text.startswith("Alright!"):
                await event.edit(f"**Error**! @Stickers replied: {response.text}")
                return
            w = await bot_conv.send_file(
                file=uploaded_sticker,
                allow_cache=False,
                force_document=True
            )
            response = await bot_conv.get_response()
            if "Sorry" in response.text:
                await event.edit(f"**Error**! @Stickers replied: {response.text}")
                return
            await silently_send_message(bot_conv, sticker_emoji)
            await silently_send_message(bot_conv, "/publish")
            response = await silently_send_message(bot_conv, f"<{packname}>")
            await silently_send_message(bot_conv, "/skip")
            response = await silently_send_message(bot_conv, packshortname)
            if response.text == "Sorry, this short name is already taken.":
                await event.edit(f"**Error**! @Stickers replied: {response.text}")
                return
        else:
            await silently_send_message(bot_conv, "/cancel")
            await silently_send_message(bot_conv, "/addsticker")
            await silently_send_message(bot_conv, packshortname)
            await bot_conv.send_file(
                file=uploaded_sticker,
                allow_cache=False,
                force_document=True
            )
            response = await bot_conv.get_response()
            if response.text == FILLED_UP_DADDY:
                while response.text == FILLED_UP_DADDY:
                    pack += 1
                    prevv = int(pack) - 1
                    packname = f"{user.username}'s {pack}"
                    packshortname = f"Vol_{pack}_with_{user.username}"
                    #if userid == 948408212:
                       # packname = f"{user.username}'s {pack}"
                       # packshortname = "Vol._{pack}_FRIDAY_ke_locker_me"
                   # else:
                       # packname = f"Vol._{pack}_FRIDAY{userid}"
                        #packshortname = f"Vol._{pack}_Friday_{userid}_ns"
                    if not await stickerset_exists(bot_conv, packshortname):
                        await event.edit("**Pack No. **" + str(prevv) + "** full! Making a new Pack, Vol. **" + str(pack))
                        if is_a_s:
                            response = await silently_send_message(bot_conv, "/newanimated")
                        else:
                            response = await silently_send_message(bot_conv, "/newpack")
                        if "Yay!" not in response.text:
                            await event.edit(f"**Error**! @Stickers replied: {response.text}")
                            return
                        response = await silently_send_message(bot_conv, packname)
                        if not response.text.startswith("Alright!"):
                            await event.edit(f"**Error**! @Stickers replied: {response.text}")
                            return
                        w = await bot_conv.send_file(
                            file=uploaded_sticker,
                            allow_cache=False,
                            force_document=True
                        )
                        response = await bot_conv.get_response()
                        if "Sorry" in response.text:
                            await event.edit(f"**Error**! @Stickers replied: {response.text}")
                            return
                        await silently_send_message(bot_conv, sticker_emoji)
                        await silently_send_message(bot_conv, "/publish")
                        response = await silently_send_message(bot_conv, f"<{packname}>")
                        await silently_send_message(bot_conv, "/skip")
                        response = await silently_send_message(bot_conv, packshortname)
                        if response.text == "Sorry, this short name is already taken.":
                            await event.edit(f"**Error**! @Stickers replied: {response.text}")
                            return
                    else:
                        await event.edit("Pack No. " + str(prevv) + " full! Switching to Vol. " + str(pack))
                        await silently_send_message(bot_conv, "/addsticker")
                        await silently_send_message(bot_conv, packshortname)                                                                            
                        await bot_conv.send_file(
                            file=uploaded_sticker,
                            allow_cache=False,
                            force_document=True
                        )
                        response = await bot_conv.get_response()
                        if "Sorry" in response.text:
                            await event.edit(f"**Error**! @Stickers replied: {response.text}")
                            return
                        await silently_send_message(bot_conv, sticker_emoji)
                        await silently_send_message(bot_conv, "/done")
            else:
                if "Sorry" in response.text:
                    await event.edit(f"**Error**! @Stickers replied: {response.text}")
                    return
                await silently_send_message(bot_conv, response)
                await silently_send_message(bot_conv, sticker_emoji)
                await silently_send_message(bot_conv, "/done")
    await event.edit(f"**Sensible Userbot Added That Sticker To My Master {DEFAULTUSER} Pack  SucessFully And Can Be Found** [Here](t.me/addstickers/{packshortname})")

@borg.on(admin_cmd(pattern="packinfo"))
async def _(event):
    if event.fwd_from:
        return
    if not event.is_reply:
        await event.edit("Reply to any sticker to get it's pack info.")
        return
    rep_msg = await event.get_reply_message()
    if not rep_msg.document:
        await event.edit("Reply to any sticker to get it's pack info.")
        return
    stickerset_attr_s = rep_msg.document.attributes
    stickerset_attr = find_instance(stickerset_attr_s, DocumentAttributeSticker)
    if not stickerset_attr.stickerset:
        await event.edit("sticker does not belong to a pack.")
        return
    get_stickerset = await borg(
        GetStickerSetRequest(
            InputStickerSetID(
                id=stickerset_attr.stickerset.id,
                access_hash=stickerset_attr.stickerset.access_hash
            )
        )
    )
    pack_emojis = []
    for document_sticker in get_stickerset.packs:
        if document_sticker.emoticon not in pack_emojis:
            pack_emojis.append(document_sticker.emoticon)
    await event.edit(f"**Sticker Title:** `{get_stickerset.set.title}\n`"
                     f"**Sticker Short Name:** `{get_stickerset.set.short_name}`\n"
                     f"**Official:** `{get_stickerset.set.official}`\n"
                     f"**Archived:** `{get_stickerset.set.archived}`\n"
                     f"**Stickers In Pack:** `{len(get_stickerset.packs)}`\n"
                     f"**Emojis In Pack:** {' '.join(pack_emojis)}")

@borg.on(admin_cmd(pattern="getsticker ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        # https://gist.github.com/udf/e4e3dbb2e831c8b580d8fddd312714f7
        if not reply_message.sticker:
            return
        sticker = reply_message.sticker
        sticker_attrib = find_instance(sticker.attributes, DocumentAttributeSticker)
        if not sticker_attrib.stickerset:
            await event.reply("This sticker is not part of a pack")
            return
        is_a_s = is_it_animated_sticker(reply_message)
        file_ext_ns_ion = "webp"
        file_caption = "https://t.me/RoseSupport/33801"
        if is_a_s:
            file_ext_ns_ion = "tgs"
            file_caption = "Forward the ZIP file to @AnimatedStickersRoBot to get lottIE JSON containing the vector information."
        sticker_set = await borg(GetStickerSetRequest(sticker_attrib.stickerset))
        pack_file = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, sticker_set.set.short_name, "pack.txt")
        if os.path.isfile(pack_file):
            os.remove(pack_file)
        # Sticker emojis are retrieved as a mapping of
        # <emoji>: <list of document ids that have this emoji>
        # So we need to build a mapping of <document id>: <list of emoji>
        # Thanks, Durov
        emojis = defaultdict(str)
        for pack in sticker_set.packs:
            for document_id in pack.documents:
                emojis[document_id] += pack.emoticon
        async def download(sticker, emojis, path, file):
            await borg.download_media(sticker, file=os.path.join(path, file))
            with open(pack_file, "a") as f:
                f.write(f"{{'image_file': '{file}','emojis':{emojis[sticker.id]}}},")
        pending_tasks = [
            asyncio.ensure_future(
                download(document, emojis, Config.TMP_DOWNLOAD_DIRECTORY + sticker_set.set.short_name, f"{i:03d}.{file_ext_ns_ion}")
            ) for i, document in enumerate(sticker_set.documents)
        ]
        await event.edit(f"Downloading {sticker_set.set.count} sticker(s) to .{Config.TMP_DOWNLOAD_DIRECTORY}{sticker_set.set.short_name}...")
        num_tasks = len(pending_tasks)
        while 1:
            done, pending_tasks = await asyncio.wait(pending_tasks, timeout=2.5,
                return_when=asyncio.FIRST_COMPLETED)
            try:
                await event.edit(
                    f"Downloaded {num_tasks - len(pending_tasks)}/{sticker_set.set.count}")
            except MessageNotModifiedError:
                pass
            if not pending_tasks:
                break
        await event.edit("Downloading to my local completed")
        # https://gist.github.com/udf/e4e3dbb2e831c8b580d8fddd312714f7
        directory_name = Config.TMP_DOWNLOAD_DIRECTORY + sticker_set.set.short_name
        zipf = zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED)
        zipdir(directory_name, zipf)
        zipf.close()
        await borg.send_file(
            event.chat_id,
            directory_name + ".zip",
            caption=file_caption,
            force_document=True,
            allow_cache=False,
            reply_to=event.message.id,
            progress_callback=progress
        )
        try:
            os.remove(directory_name + ".zip")
            os.remove(directory_name)
        except:
            pass
        await event.edit("task Completed")
        await asyncio.sleep(3)
        await event.delete()
    else:
        await event.edit("TODO: Not Implemented")

def is_it_animated_sticker(message):
    try:
        if message.media and message.media.document:
            mime_type = message.media.document.mime_type
            if "tgsticker" in mime_type:
                return True
            else:
                return False
        else:
            return False
    except:
        return False

def is_message_image(message):
    if message.media:
        if isinstance(message.media, MessageMediaPhoto):
            return True
        if message.media.document:
            if message.media.document.mime_type.split("/")[0] == "image":
                return True
        return False
    return False

async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response

async def stickerset_exists(conv, setname):
    try:
        await borg(GetStickerSetRequest(InputStickerSetShortName(setname)))
        response = await silently_send_message(conv, "/addsticker")
        if response.text == "Invalid pack selected.":
            await silently_send_message(conv, "/cancel")
            return False
        await silently_send_message(conv, "/cancel")
        return True
    except StickersetInvalidError:
        return False

def resize_image(image, save_locaton):
    im = Image.open(image)
    maxsize = (512, 512)
    if (im.width and im.height) < 512:
        size1 = im.width
        size2 = im.height
        if im.width > im.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        im = im.resize(sizenew)
    else:
        im.thumbnail(maxsize)
    im.save(save_locaton, "PNG")

def progress(current, total):
    logger.info("Uploaded: {} of {}\nCompleted {}".format(current, total, (current / total) * 100))

def find_instance(items, class_or_tuple):
    for item in items:
        if isinstance(item, class_or_tuple):
            return item
    return None

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))
           
@borg.on(admin_cmd(pattern="stcr ?(?:(.*?) \| )?(.*)", outgoing=True))
async def sticklet(event):
    R = random.randint(0,256)
    G = random.randint(0,256)
    B = random.randint(0,256)
    reply_message = event.message
    # get the input text
    # the text on which we would like to do the magic on
    font_file_name = event.pattern_match.group(1)
    if not font_file_name:
        font_file_name = ""
    sticktext = event.pattern_match.group(2)
    if not sticktext and event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        sticktext = reply_message.message
    elif not sticktext:
        await event.edit("need something, hmm")
        return
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    # delete the userbot command,
    # i don't know why this is required
    await event.delete()
    # https://docs.python.org/3/library/textwrap.html#textwrap.wrap
    sticktext = textwrap.wrap(sticktext, width=10)
    # converts back the list to a string
    sticktext = '\n'.join(sticktext)
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    FONT_FILE = await get_font_file(event.client, "@catfonts", font_file_name)
    font = ImageFont.truetype(FONT_FILE, size=fontsize)
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(((512-width)/2,(512-height)/2), sticktext, font=font, fill=(R, G, B))
    image_stream = io.BytesIO()
    image_stream.name = "@mrconfused.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)
    # finally, reply the sticker
    await event.client.send_file(event.chat_id, image_stream, caption="Created Using Sensible Userbot Userbot", reply_to=event.message.reply_to_msg_id)
    # cleanup
    try:
        os.remove(FONT_FILE)
    except:
        pass
 
@borg.on(admin_cmd(pattern="stcr ?(?:(.*?) \| )?(.*)", allow_sudo=True))
async def sticklet(event):
    R = random.randint(0,256)
    G = random.randint(0,256)
    B = random.randint(0,256)
    reply_message = event.message
    # get the input text
    # the text on which we would like to do the magic on
    font_file_name = event.pattern_match.group(1)
    if not font_file_name:
        font_file_name = ""
    sticktext = event.pattern_match.group(2)
    if not sticktext and event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        sticktext = reply_message.message
    elif not sticktext:
        await event.edit("need something, hmm")
        return
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    # delete the userbot command,
    # i don't know why this is required
    await event.delete()
    # https://docs.python.org/3/library/textwrap.html#textwrap.wrap
    sticktext = textwrap.wrap(sticktext, width=10)
    # converts back the list to a string
    sticktext = '\n'.join(sticktext)
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    FONT_FILE = await get_font_file(event.client, "@catfonts", font_file_name)
    font = ImageFont.truetype(FONT_FILE, size=fontsize)
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(((512-width)/2,(512-height)/2), sticktext, font=font, fill=(R, G, B))
    image_stream = io.BytesIO()
    image_stream.name = "@mrconfused.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)
    # finally, reply the sticker
    await event.client.send_file(event.chat_id, image_stream, caption="Created Using Sensible Userbot", reply_to=event.message.reply_to_msg_id)
    # cleanup
    try:
        os.remove(FONT_FILE)
    except:
        pass
    
async def get_font_file(client, channel_id, search_kw=""):
    # first get the font messages
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        # this might cause FLOOD WAIT,
        # if used too many times
        limit=None,
        search=search_kw
    )
    # get a random font from the list of fonts
    # https://docs.python.org/3/library/random.html#random.choice
    font_file_message = random.choice(font_file_message_s)
    # download and return the file path
    return await client.download_media(font_file_message)

@borg.on(admin_cmd("rmbg ?(.*)"))
async def _(event):
    HELP_STR = "`.rmbg` as reply to a media, or give a link as an argument to this command"
    if event.fwd_from:
        return
    if Config.REM_BG_API_KEY is None:
        await event.edit("You need API token from remove.bg to use this plugin.")
        return False
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
        reply_message = await event.get_reply_message()
        # check if media message
        await event.edit("Connecting to official Sensible Userbot server and analysing that img ...")
        try:
            downloaded_file_name = await borg.download_media(
                reply_message,
                Config.TMP_DOWNLOAD_DIRECTORY
            )
        except Exception as e:
            await event.edit(str(e))
            return
        else:
            await event.edit("sending to ReMove.BG")
            output_file_name = ReTrieveFile(downloaded_file_name)
            os.remove(downloaded_file_name)
    elif input_str:
        await event.edit("sending to ReMove.BG")
        output_file_name = ReTrieveURL(input_str)
    else:
        await event.edit(HELP_STR)
        return
    contentType = output_file_name.headers.get("content-type")
    if "image" in contentType:
        with io.BytesIO(output_file_name.content) as remove_bg_image:
            remove_bg_image.name = "@Ironbots.png"
            await borg.send_file(
                event.chat_id,
                remove_bg_image,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=message_id
            )
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit("Removed dat annoying Backgroup in {} seconds, powered by @Ironbots".format(ms))
    else:
        await event.edit("ReMove.BG API returned Errors. Please report to @Ironbots\n`{}".format(output_file_name.content.decode("UTF-8")))

def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": Config.REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True
    )
    return r

def ReTrieveURL(input_url):
    headers = {
        "X-API-Key": Config.REM_BG_API_KEY,
    }
    data = {
      "image_url": input_url
    }
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        data=data,
        allow_redirects=True,
        stream=True
    )
    return r

