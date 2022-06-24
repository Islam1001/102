#    هو انتو كلشي خامطيه من الاجانب ومن سورسات العرب البقيه
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights, MessageEntityMentionName

from sbb_b import sbb_b


async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("▾∮ لا يمكنك بدون ايدي المستخدم")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("هنالك خطأ", str(err))
    return user_obj, extra


global hawk, moth
hawk = "admin"
moth = "owner"


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@sbb_b.ar_cmd(pattern="ارفع ?(.*)")
async def gben(sbb_b):
    dc = razan = sbb_b
    i = 0
    await dc.get_sender()
    me = await sbb_b.client.get_me()
    await razan.edit("يتم رفع المستخدم في جميع المجموعات")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await sbb_b.get_chat()
    if sbb_b.is_private:
        user = sbb_b.chat
        rank = sbb_b.pattern_match.group(1)
    else:
        sbb_b.chat.title
    try:
        user, rank = await get_full_user(sbb_b)
    except:
        pass
    if me == user:
        await razan.edit(" لا استطيع رفع نفسي")
        return
    try:
        if not rank:
            rank = "ㅤㅤ"
    except:
        return await razan.edit(f"**هنالك شي خطأ**")
    if user:
        telchanel = [
            d.entity.id
            for d in await sbb_b.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        rgt = ChatAdminRights(
            add_admins=True,
            invite_users=True,
            change_info=True,
            ban_users=True,
            delete_messages=True,
            pin_messages=True,
        )
        for x in telchanel:
            try:
                await sbb_b.client(EditAdminRequest(x, user, rgt, rank))
                i += 1
                await razan.edit(f"**يتم الرفع في **: `{i}` من المجموعات")
            except:
                pass
    else:
        await razan.edit(f"**يجب عليك الرد على المستخدم اولا **")
    return await razan.edit(
        f"**المستخدم [{user.first_name}](tg://user?id={user.id})\n▾∮ تم رفعه في : {i} من المجموعات**"
    )


@sbb_b.ar_cmd(pattern="نزل ?(.*)")
async def gben(sbb_b):
    dc = razan = sbb_b
    i = 0
    await dc.get_sender()
    me = await sbb_b.client.get_me()
    await razan.edit("** يتم تنزيل الشخص من رتبة الاشراف في جميع الكروبات**")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await sbb_b.get_chat()
    if sbb_b.is_private:
        user = sbb_b.chat
        rank = sbb_b.pattern_match.group(1)
    else:
        sbb_b.chat.title
    try:
        user, rank = await get_full_user(sbb_b)
    except:
        pass
    if me == user:
        await razan.edit("لا استطيع تنزيل نفسي")
        return
    try:
        if not rank:
            rank = "ㅤㅤ"
    except:
        return await razan.edit(f"** هنالك شي خطأ**")
    if user:
        telchanel = [
            d.entity.id
            for d in await sbb_b.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        rgt = ChatAdminRights(
            add_admins=None,
            invite_users=None,
            change_info=None,
            ban_users=None,
            delete_messages=None,
            pin_messages=None,
        )
        for x in telchanel:
            try:
                await sbb_b.client(EditAdminRequest(x, user, rgt, rank))
                i += 1
                await razan.edit(f"** يتم تنزيله في **: `{i}` من المجموعات")
            except:
                pass
    else:
        await razan.edit(f"** يجب عليك الرد على المستخدم اولا **")
    return await razan.edit(
        f"**المستخدم [{user.first_name}](tg://user?id={user.id})\n▾∮ تم تنزيله في : {i} من المجموعات**"
    )
