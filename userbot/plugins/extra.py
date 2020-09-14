from telethon import events, functions
from datetime import datetime
import asyncio, io, random, speedtest, emoji, urbandict, types
from googletrans import Translator
from uniborg.util import admin_cmd
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
from userbot import CMD_HELP, bot
from subprocess import PIPE
from subprocess import run as runapp
import pybase64
from userbot.events import register, errors_handler

normiefont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
weebyfont = ['卂', '乃', '匚', '刀', '乇', '下', '厶', '卄', '工', '丁', '长', '乚', '从', '𠘨', '口', '尸', '㔿', '尺', '丂', '丅', '凵',
             'リ', '山', '乂', '丫', '乙']

import emoji
from googletrans import Translator
from userbot.utils import admin_cmd


@borg.on(admin_cmd("tr ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "id"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.edit("`.tr LanguageCode` as reply to a message")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        output_str = """
         Source **( {} )**
Translate ke **( {} )**

Hasil : {}""".format(
            translated.src,
            lan,
            after_tr_text
        )
        await event.edit(output_str)
    except Exception as exc:
        await event.edit(str(exc))
        
    
@borg.on(admin_cmd("ud (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("processing...")
    str = event.pattern_match.group(1)
    try:
        mean = urbandict.define(str)
        if len(mean) > 0:
            await event.edit(
                'Text: **' +
                str +
                '**\n\nMeaning: **' +
                mean[0]['def'] +
                '**\n\n' +
                'Example: \n__' +
                mean[0]['example'] +
                '__'
            )
        else:
            await event.edit("No result found for **" + str + "**")
    except:
        await event.edit("No result found for **" + str + "**")


@borg.on(admin_cmd(pattern="weeb ?(.*)"))
async def weebify(event):

    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What I am Supposed to Weebify U Dumb`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)

@borg.on(admin_cmd("speed ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    as_text = True
    as_document = False
    if input_str == "image":
        as_document = False
    elif input_str == "file":
        as_document = True
    elif input_str == "text":
        as_text = True
    await event.edit("`Calculating my internet speed. Please wait!`")
    start = datetime.now()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        reply_msg_id = event.reply_to_msg_id
    try:
        response = s.results.share()
        speedtest_image = response
        if as_text:
            await event.edit("""`SpeedTest completed in {} seconds`

`Download: {}`
`Upload: {}`
`Ping: {}`
`Internet Service Provider: {}`
`ISP Rating: {}`""".format(ms, convert_from_bytes(download_speed), convert_from_bytes(upload_speed), ping_time, i_s_p, i_s_p_rating))
        else:
            await borg.send_file(
                event.chat_id,
                speedtest_image,
                caption="**SpeedTest** completed in {} seconds".format(ms),
                force_document=as_document,
                reply_to=reply_msg_id,
                allow_cache=False
            )
            await event.delete()
    except Exception as exc:
        await event.edit("""**SpeedTest** completed in {} seconds
Download: {}
Upload: {}
Ping: {}

__With the Following ERRORs__
{}""".format(ms, convert_from_bytes(download_speed), convert_from_bytes(upload_speed), ping_time, str(exc)))


def convert_from_bytes(size):
    power = 2**10
    n = 0
    units = {
        0: "",
        1: "kilobytes",
        2: "megabytes",
        3: "gigabytes",
        4: "terabytes"
    }
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"


@borg.on(admin_cmd(pattern="mashup ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@vixtbot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=285336877))
              await event.client.send_message(chat, "{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Unblock @vixtbot")
              return
          if response.text.startswith("I can't find that"):
             await event.edit("sorry i can't find it")
          else: 
             await event.delete()
             await borg.send_file(event.chat_id, response.message, reply_to=reply_to_id)

@borg.on(admin_cmd(pattern="mash ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@vixtbot"
    await event.delete()
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=285336877))
              await event.client.send_message(chat, "{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Unblock @vixtbot")
              return
          if response.text.startswith("I can't find that"):
             await event.reply("sorry i can't find it")
          else: 
             await event.delete()
             await borg.send_file(event.chat_id, response.message, reply_to=reply_to_id)
 
 
@borg.on(admin_cmd("listmyusernames"))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f" ✔ {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)
    
@borg.on(admin_cmd("json"))
async def _(event):
    if event.fwd_from:
        return
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    if len(the_real_message) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(the_real_message)) as out_file:
            out_file.name = "json.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                reply_to=reply_to_id
            )
            await event.delete()
    else:
        await event.edit("`{}`".format(the_real_message))


@register(outgoing=True, pattern="^.hash (.*)")
@errors_handler
async def gethash(hash_q):
    """ For .hash command, find the md5, sha1, sha256, sha512 of the string. """
    hashtxt_ = hash_q.pattern_match.group(1)
    hashtxt = open("hashdis.txt", "w+")
    hashtxt.write(hashtxt_)
    hashtxt.close()
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = ("Text: `" + hashtxt_ + "`\nMD5: `" + md5 + "`SHA1: `" + sha1 +
           "`SHA256: `" + sha256 + "`SHA512: `" + sha512[:-1] + "`")
    if len(ans) > 4096:
        hashfile = open("hashes.txt", "w+")
        hashfile.write(ans)
        hashfile.close()
        await hash_q.client.send_file(
            hash_q.chat_id,
            "hashes.txt",
            reply_to=hash_q.id,
            caption="`It's too big, sending a text file instead. `")
        runapp(["rm", "hashes.txt"], stdout=PIPE)
    else:
        await hash_q.reply(ans)


@register(outgoing=True, pattern="^.hbase (en|de) (.*)")
@errors_handler
async def endecrypt(query):
    """ For .base64 command, find the base64 encoding of the given string. """
    if query.pattern_match.group(1) == "en":
        lething = str(
            pybase64.b64encode(bytes(query.pattern_match.group(2),
                                     "utf-8")))[2:]
        await query.reply("Shhh! It's Encoded: `" + lething[:-1] + "`")
    else:
        lething = str(
            pybase64.b64decode(bytes(query.pattern_match.group(2), "utf-8"),
                               validate=True))[2:]
        await query.reply("Decoded: `" + lething[:-1] + "`")


CMD_HELP.update({"base64": "Find the base64 encoding of the given string"})

CMD_HELP.update({
    "hash":
    "Find the md5, sha1, sha256, sha512 of the string when written into a txt file."
})
CMD_HELP.update({"mashup": "`.mashup` <text> :\
      \n**USAGE:** Send you the related video message of given text . "
}) 










