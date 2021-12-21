"""Hatsune Robot main module"""
# Copyright (C) 2021 - 2022  ZenitsuID, <https://github.com/ZenitsuID.git>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pyrogram import filters

from HatsuneRobot import pbot as app, arq
from HatsuneRobot.utils.errors import capture_err

__mod_name__ = "Reddit"


@app.on_message(filters.command("reddit") & ~filters.edited)
@capture_err
async def reddit(_, message):
    if len(message.command) != 2:
        return await message.reply_text("/reddit needs an argument")
    subreddit = message.text.split(None, 1)[1]
    m = await message.reply_text("Searching")
    reddit = await arq.reddit(subreddit)
    if not reddit.ok:
        return await m.edit(reddit.result)
    reddit = reddit.result
    nsfw = reddit.nsfw
    sreddit = reddit.subreddit
    title = reddit.title
    image = reddit.url
    link = reddit.postLink
    if nsfw:
        return await m.edit("NSFW RESULTS COULD NOT BE SHOWN.")
    caption = f"""
**Title:** `{title}`
**Subreddit:** {sreddit}
**PostLink:** {link}"""
    try:
        await message.reply_photo(photo=image, caption=caption)
        await m.delete()
    except Exception as e:
        await m.edit(e.MESSAGE)
