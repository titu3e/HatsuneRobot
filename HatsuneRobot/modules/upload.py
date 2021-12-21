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

import asyncio
import datetime
import os
import time
import traceback

import aiohttp
from telethon import events

from HatsuneRobot import telethn as bot
from HatsuneRobot.modules.urluploader import download_file
from HatsuneRobot.utils.uputils import humanbytes, progress

DOWNLOADPATH = "Downloads/"


def get_date_in_two_weeks():
    """
    get maximum date of storage for file
    :return: date in two weeks
    """
    today = datetime.datetime.today()
    date_in_two_weeks = today + datetime.timedelta(days=14)
    return date_in_two_weeks.date()


async def send_to_transfersh_async(file):

    size = os.path.getsize(file)
    size_of_file = humanbytes(size)
    final_date = get_date_in_two_weeks()
    file_name = os.path.basename(file)

    print("\nUploading file: {} (size of the file: {})".format(file_name, size_of_file))
    url = "https://transfer.sh/"

    with open(file, "rb") as f:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data={str(file): f}) as response:
                download_link = await response.text()

    print(
        "Link to download file(will be saved till {}):\n{}".format(
            final_date, download_link
        )
    )
    return download_link, final_date, size_of_file


async def send_to_tmp_async(file):
    url = "https://tmp.ninja/api.php?d=upload-tool"

    with open(file, "rb") as f:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data={"file": f}) as response:
                download_link = await response.text()

    return download_link


@bot.on(events.NewMessage(pattern="/transfersh"))
async def tsh(event):
    if event.reply_to_msg_id:
        start = time.time()
        url = await event.get_reply_message()
        ilk = await event.respond("Downloading...")
        try:
            file_path = await url.download_media(
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, ilk, start, "Downloading...")
                )
            )
        except Exception as e:
            traceback.print_exc()
            print(e)
            await event.respond(f"Downloading Failed\n\n**Error:** {e}")

        await ilk.delete()

        try:
            orta = await event.respond("Uploading to TransferSh...")
            download_link, final_date, size = await send_to_transfersh_async(file_path)

            str(time.time() - start)
            await orta.edit(
                f"File Successfully Uploaded to TransferSh.\n\nLink 👉 {download_link}\nExpired Date 👉 {final_date}\n\nUploaded by *AsunaRobot*"
            )
        except Exception as e:
            traceback.print_exc()
            print(e)
            await event.respond(f"Uploading Failed\n\n**Error:** {e}")

    raise events.StopPropagation


@bot.on(events.NewMessage(pattern="/tmpninja"))
async def tmp(event):
    if event.reply_to_msg_id:
        start = time.time()
        url = await event.get_reply_message()
        ilk = await event.respond("Downloading...")
        try:
            file_path = await url.download_media(
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, ilk, start, "Downloading...")
                )
            )
        except Exception as e:
            traceback.print_exc()
            print(e)
            await event.respond(f"Downloading Failed\n\n**Error:** {e}")

        await ilk.delete()

        try:
            orta = await event.respond("Uploading to TmpNinja...")
            download_link = await send_to_tmp_async(file_path)

            str(time.time() - start)
            await orta.edit(
                f"File Successfully Uploaded to TmpNinja.\n\nLink 👉 {download_link}\n\nUploaded by *AsunaRobot*"
            )
        except Exception as e:
            traceback.print_exc()
            print(e)
            await event.respond(f"Uploading Failed\n\n**Error:** {e}")

    raise events.StopPropagation


@bot.on(events.NewMessage(pattern="/up"))
async def up(event):
    if event.reply_to_msg_id:
        start = time.time()
        url = await event.get_reply_message()
        ilk = await event.respond("Downloading...")

        try:
            filename = os.path.join(DOWNLOADPATH, os.path.basename(url.text))
            await download_file(url.text, filename, ilk, start, bot)
        except Exception as e:
            print(e)
            await event.respond(f"Downloading Failed\n\n**Error:** {e}")

        await ilk.delete()

        try:
            orta = await event.respond("Uploading to Telegram...")

            dosya = await bot.upload_file(
                filename,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, orta, start, "Uploading to Telegram...")
                ),
            )

            str(time.time() - start)
            await bot.send_file(
                event.chat.id,
                dosya,
                force_document=True,
                caption=f"Uploaded By *AsunaRobot*",
            )
        except Exception as e:
            traceback.print_exc()

            print(e)
            await event.respond(f"Uploading Failed\n\n**Error:** {e}")

        await orta.delete()

    raise events.StopPropagation


def main():
    if not os.path.isdir(DOWNLOADPATH):
        os.mkdir(DOWNLOADPATH)


if __name__ == "__main__":
    main()
