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

from io import BytesIO
from os import path, remove
from time import time

import img2pdf
from PIL import Image
from pyrogram import filters
from pyrogram.types import Message

from HatsuneRobot import pbot as app
from HatsuneRobot.utils.errors import capture_err
from HatsuneRobot.services.sections import section


async def convert(
    main_message: Message,
    reply_messages,
    status_message: Message,
    start_time: float,
):
    m = status_message

    documents = []

    for message in reply_messages:
        if not message.document:
            return await m.edit("Not document, ABORTED!")

        if message.document.mime_type.split("/")[0] != "image":
            return await m.edit("Invalid mime type!")

        if message.document.file_size > 5000000:
            return await m.edit("Size too large, ABORTED!")
        documents.append(await message.download())

    for img_path in documents:
        img = Image.open(img_path).convert("RGB")
        img.save(img_path, "JPEG", quality=100)

    pdf = BytesIO(img2pdf.convert(documents))
    pdf.name = "NaoRobot.pdf"

    if len(main_message.command) >= 2:
        pdf.name = main_message.text.split(None, 1)[1]

    elapsed = round(time() - start_time, 2)

    await main_message.reply_document(
        document=pdf,
        caption=section(
            "IMG2PDF",
            body={
                "Title": pdf.name,
                "Size": f"{pdf.__sizeof__() / (10**6)}MB",
                "Pages": len(documents),
                "Took": f"{elapsed}s",
            },
        ),
    )

    await m.delete()
    pdf.close()
    for file in documents:
        if path.exists(file):
            remove(file)


@app.on_message(filters.command("pdf"))
@capture_err
async def img_to_pdf(_, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply(
            "Reply to an image (as document) or group of images."
        )

    m = await message.reply_text("Converting..")
    start_time = time()

    if reply.media_group_id:
        messages = await app.get_media_group(
            message.chat.id,
            reply.message_id,
        )
        return await convert(message, messages, m, start_time)

    return await convert(message, [reply], m, start_time)
