import asyncio
import os
import shlex
from os import getcwd
from os.path import basename, join
from textwrap import wrap
from typing import Optional, Tuple

from PIL import Image, ImageDraw, ImageFont
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image as catimage

MARGINS = [50, 150, 250, 350, 450]


def get_warp_length(width):
    return int((20.0 / 1024.0) * (width + 0.0))



# executing of terminal commands


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
