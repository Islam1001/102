import os
import random

from PIL import Image, ImageDraw, ImageFont
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterPhotos

from sbb_b import sbb_b

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.utils import reply_id
from . import sbb_b, mention

import os
from datetime import datetime

from sbb_b import sbb_b

from . import hmention, reply_id

"""
try:
    from . import PING_PIC, PING_TEXT
except:
    pass
"""
plugin_category = "tools"

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/c01ad3e88c1895e032430.mp4"
)

JM_TXT = os.environ.get("PING_TEXT") or "𝗡𝗘𝗪 𝗦𝗧𝗬𝗟𝗘 💔"


@sbb_b.ar_cmd(pattern=". ?(.*)")

async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(
        event, "<b><i>  𝗡𝗘𝗪 𝗦𝗧𝗬𝗟𝗘 💔  </b></i>", "html"
    )
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    HSO = rek.pattern_match.group(1)
    if HSO:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code> 𝖉𝖊𝖛 ︙ @HssHH\n {HSO}"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=HSO,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "hi", "html"
        )
