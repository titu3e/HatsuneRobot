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

from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton as Ikb

from HatsuneRobot.utils.functions import get_urls_from_text as is_url


def keyboard(buttons_list, row_width: int = 2):
    """
    Buttons builder, pass buttons in a list and it will
    return pyrogram.types.IKB object
    Ex: keyboard([["click here", "https://google.com"]])
    if theres, a url, it will make url button, else callback button
    """
    buttons = InlineKeyboard(row_width=row_width)
    data = [
        (
            Ikb(text=str(i[0]), callback_data=str(i[1]))
            if not is_url(i[1])
            else Ikb(text=str(i[0]), url=str(i[1]))
        )
        for i in buttons_list
    ]
    buttons.add(*data)
    return buttons


def ikb(data: dict, row_width: int = 2):
    """
    Converts a dict to pyrogram buttons
    Ex: dict_to_keyboard({"click here": "this is callback data"})
    """
    return keyboard(data.items(), row_width=row_width)
