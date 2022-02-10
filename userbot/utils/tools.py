from telethon import _tl


async def create_supergroup(group_name, client, botusername, descript):
    try:
        result = await client(
            _tl.fn.channels.CreateChannel(
                title=group_name,
                about=descript,
                megagroup=True,
            )
        )
        created_chat_id = result.chats[0].id
        result = await client(
            _tl.fn.messages.ExportChatInvite(
                peer=created_chat_id,
            )
        )
        await client(
            _tl.fn.channels.InviteToChannel(
                channel=created_chat_id,
                users=[botusername],
            )
        )
    except Exception as e:
        return "error", str(e)
    if not str(created_chat_id).startswith("-100"):
        created_chat_id = int("-100" + str(created_chat_id))
    return result, created_chat_id
