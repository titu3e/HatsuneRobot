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

import os
import shutil

from PIL import Image, ImageOps


async def black_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-black-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                "Downloading image", quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit("Processing Image...")
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="black")
            img_with_border.save(edit_img_loc)
            await message.reply_chat_action("upload_photo")
            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text("Why did you delete that??")
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("black_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "Something went wrong!", quote=True
                )
            except Exception:
                return


async def green_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-green-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                "Downloading image", quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit("Processing Image...")
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="green")
            img_with_border.save(edit_img_loc)
            await message.reply_chat_action("upload_photo")
            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text("Why did you delete that??")
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("green_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "Something went wrong!", quote=True
                )
            except Exception:
                return


async def blue_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-blue-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                "Downloading image", quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit("Processing Image...")
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="blue")
            img_with_border.save(edit_img_loc)
            await message.reply_chat_action("upload_photo")
            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text("Why did you delete that??")
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("blue_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "Something went wrong!", quote=True
                )
            except Exception:
                return


async def red_border(client, message):
    try:
        userid = str(message.chat.id)
        if not os.path.isdir(f"./DOWNLOADS/{userid}"):
            os.makedirs(f"./DOWNLOADS/{userid}")
        download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
        edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "imaged-red-border.png"
        if not message.reply_to_message.empty:
            msg = await message.reply_to_message.reply_text(
                "Downloading image", quote=True
            )
            a = await client.download_media(
                message=message.reply_to_message, file_name=download_location
            )
            await msg.edit("Processing Image...")
            img = Image.open(a)
            img_with_border = ImageOps.expand(img, border=100, fill="red")
            img_with_border.save(edit_img_loc)
            await message.reply_chat_action("upload_photo")
            await message.reply_to_message.reply_photo(edit_img_loc, quote=True)
            await msg.delete()
        else:
            await message.reply_text("Why did you delete that??")
        try:
            shutil.rmtree(f"./DOWNLOADS/{userid}")
        except Exception:
            pass
    except Exception as e:
        print("red_border-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "Something went wrong!", quote=True
                )
            except Exception:
                return
