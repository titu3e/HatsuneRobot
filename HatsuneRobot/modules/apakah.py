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

import random
from HatsuneRobot.events import register
from HatsuneRobot import telethn

APAKAH_STRING = [
    "Iya",
    "Tidak",
    "Mungkin",
    "Mungkin Tidak",
    "Bisa jadi",
    "Mungkin Tidak",
    "Tidak Mungkin",
    "YNTKTS",
    "Pala bapak kau pecah",
    "Apa iya?",
    "Tanya aja sama mamak kau tu pler",
]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply("Berikan saya pertanyaan 😐")
        return
    await event.reply(random.choice(APAKAH_STRING))
