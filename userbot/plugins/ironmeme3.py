"""
Available Commands:
.music"""

from telethon import events, functions, __version__
import asyncio, os, sys
from collections import deque
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"meme"))
async def meme(event):
    if event.fwd_from:
        return   
    memeVar = event.text
    sleepValue = 0.5
    memeVar = memeVar[6:] 
           
    await event.edit("i-------------"+memeVar)
    await asyncio.sleep(sleepValue)
    await event.edit("-i-----------"+memeVar+"-")
    await asyncio.sleep(sleepValue)
    await event.edit("--i---------"+memeVar+"--")
    await asyncio.sleep(sleepValue)
    await event.edit("----i------"+memeVar+"---")
    await asyncio.sleep(sleepValue)
    await event.edit("-----i----"+memeVar+"----")   
    await asyncio.sleep(sleepValue) 
    await event.edit("------i--"+memeVar+"-----")
    await asyncio.sleep(sleepValue)
    await event.edit("------i-"+memeVar+"------")
    await asyncio.sleep(sleepValue)
    await event.edit("------i"+memeVar+"-------")
    await asyncio.sleep(sleepValue)
    await event.edit("----i-"+memeVar+"--------")
    await asyncio.sleep(sleepValue)
    await event.edit("--i--"+memeVar+"---------")
    await asyncio.sleep(sleepValue)
    await event.edit("-i--"+memeVar+"----------")
    await asyncio.sleep(sleepValue)
    await event.edit("i--"+memeVar+"-----------")
    await asyncio.sleep(sleepValue)
    await event.edit("-i"+memeVar+"------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar+"-------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar)
    await asyncio.sleep(sleepValue)

"""
Bonus : Flower Boquee Generater
usage:- .flower

"""
@borg.on(admin_cmd(pattern=r"flower"))
async def meme(event):
    if event.fwd_from:
        return   
    flower =" 🌹"
    sleepValue = 1
           
    await event.edit(flower+"        ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+"       ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+"      ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+"     ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+"    ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+"   ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+"   ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+"  ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+" ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+flower)
    await asyncio.sleep(sleepValue)
        

@borg.on(admin_cmd("mf"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,27)
    #input_str = event.pattern_match.group(1)
    #if input_str == "mf":
    await event.edit("mf")
    animation_chars = [
            "\n......................................../´¯/)\n......................................,/¯../ \n...................................../..../ \n..................................../´.¯/\n..................................../´¯/\n..................................,/¯../ \n................................../..../ \n................................./´¯./\n................................/´¯./\n..............................,/¯../\n............................./..../ \n............................/´¯/\n........................../´¯./\n........................,/¯../ \n......................./..../ \n....................../´¯/\n....................,/¯../ \n.................../..../ \n............./´¯/'...'/´¯¯`·¸ \n........../'/.../..../......./¨¯\ \n........('(...´...´.... ¯~/'...') \n.........\.................'...../ \n..........''...\.......... _.·´ \n............\..............( \n..............\.............\..."
        ]

    for i in animation_ttl:         
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %27 ])

@borg.on(admin_cmd(pattern="dc"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await event.edit(result.stringify())


@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""Telethon Ironbot powered by @[Ironbots](t.me/Ironbots)""")


@borg.on(admin_cmd(pattern=r"smoon"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 32)
    await event.edit("moon")
    animation_chars = [
            "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
            "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",    
            "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
            "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
            "🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
            "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
            "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
            "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖"
        ]
        
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])



@borg.on(admin_cmd(pattern=r"tmoon"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 33)
    await event.edit("moon")
    animation_chars = [

            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖"
        ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 33])


@borg.on(admin_cmd(pattern=r"moon", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    

@borg.on(admin_cmd(pattern=r"mtn"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 19)
    await event.edit("mtn")
    animation_chars = [    
            "`Connecting To MTN NG ....`",
            "`█ ▇ ▆ ▅ ▄ ▂ ▁`",
            "`▒ ▇ ▆ ▅ ▄ ▂ ▁`",
            "`▒ ▒ ▆ ▅ ▄ ▂ ▁`",
            "`▒ ▒ ▒ ▅ ▄ ▂ ▁`",    
            "`▒ ▒ ▒ ▒ ▄ ▂ ▁`",
            "`▒ ▒ ▒ ▒ ▒ ▂ ▁`",
            "`▒ ▒ ▒ ▒ ▒ ▒ ▁`",
            "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
            "*Optimising Network...*",
            "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
            "`▁ ▒ ▒ ▒ ▒ ▒ ▒`",           
            "`▁ ▂ ▒ ▒ ▒ ▒ ▒`",
            "`▁ ▂ ▄ ▒ ▒ ▒ ▒`",
            "`▁ ▂ ▄ ▅ ▒ ▒ ▒`",
            "`▁ ▂ ▄ ▅ ▆ ▒ ▒`",
            "`▁ ▂ ▄ ▅ ▆ ▇ ▒`",
            "`▁ ▂ ▄ ▅ ▆ ▇ █`",
            "**MTN Network Boosted....**"
 ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 19])


@borg.on(admin_cmd(pattern=r"music"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0, 11)
    await event.edit("music")
    animation_chars = [
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](tg://user?id=1178524273)\n\n⠀⠀⠀⠀**Now Playing:Alan Walker - Ignite**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](tg://user?id=1178524273)\n\n⠀⠀⠀⠀**Now Playing:Alan Walker - Ignite**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](tg://user?id=1178524273)\n\n⠀⠀⠀⠀**Now Playing:Alan Walker - Ignite**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](tg://user?id=1178524273)\n\n⠀⠀⠀⠀**Now Playing:Alan Walker - Ignite**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](tg://user?id=1178524273)\n\n⠀⠀⠀⠀**Now Playing:Alan Walker - Ignite**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",    
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](tg://user?id=1178524273)\n\n⠀⠀⠀⠀**Now Playing:Alan Walker - Ignite**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](tg://user?id=1178524273)\n\n⠀⠀⠀⠀**Now Playing:Alan Walker - Ignite**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](tg://user?id=1178524273)\n\n⠀⠀⠀⠀**Now Playing:Alan Walker - Ignite**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](tg://user?id=1178524273)\n\n⠀⠀⠀⠀**Now Playing:Alan Walker - Ignite**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
            "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](tg://user?id=1178524273)\n\n⠀⠀⠀⠀**Now Playing:Alan Walker - Ignite**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n**⠀Next Song:** __I Am Sexy And I Know It.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**"
        ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])
        
        
        
        
        
