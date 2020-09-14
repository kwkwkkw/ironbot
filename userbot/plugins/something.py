''' Whatever Plugin by Noobs of Telegram i.e. @CeoWhiteHatCracks '''

from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd
import string

from telethon import events
from telethon.tl import types
from uniborg.util import admin_cmd

msg_cache = {}
import pyfiglet
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"lmoon"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕")

@borg.on(admin_cmd(pattern=r"city"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("""☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖     l               \
   🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲""")


@borg.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("🌺✨✨🌺✨🌺🌺🌺\n🌺✨✨🌺✨✨🌺✨\n🌺🌺🌺🌺✨✨🌺✨\n🌺✨✨🌺✨✨🌺✨\n🌺✨✨🌺✨🌺🌺🌺\n☁☁☁☁☁☁☁☁")

@borg.on(admin_cmd(pattern=r"cheer"))
async def cheer(event):
    if event.fwd_from:
        return
    await event.edit("💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐")

@borg.on(admin_cmd(pattern=r"getwell"))
async def getwell(event):
    if event.fwd_from:
        return
    await event.edit("🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹")

@borg.on(admin_cmd(pattern=r"sprinkle"))
async def sprinkle(event):
    if event.fwd_from:
        return
    await event.edit("✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀")


@borg.on(admin_cmd(pattern=r"fpost\s+(.*)"))
async def _(event):
    await event.delete()
    text = event.pattern_match.group(1)
    destination = await event.get_input_chat()

    for c in text.lower():
        if c not in string.ascii_lowercase:
            continue
        if c not in msg_cache:
            async for msg in borg.iter_messages(None, search=c):
                if msg.raw_text.lower() == c and msg.media is None:
                    msg_cache[c] = msg
                    break
        await borg.forward_messages(destination, msg_cache[c])


#@command(pattern="^.figlet ?(.*)", outgoing=True)
@borg.on(admin_cmd(pattern=r"figlet ?(.*)"))
async def figlet(event):
    if event.fwd_from:
        return
    CMD_FIG = {"slant": "slant", "3D": "3-d", "5line": "5lineoblique", "alpha": "alphabet", "banner": "banner3-D", "doh": "doh", "iso": "isometric1", "letter": "letters", "allig": "alligator", "dotm": "dotmatrix", "bubble": "bubble", "bulb": "bulbhead", "digi": "digital"}
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        text, cmd = input_str.split("|", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await event.edit("Please add some text to figlet")
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await event.edit("Invalid selected font.")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await event.respond("‌‌‎`{}`".format(result))
    await event.delete()







