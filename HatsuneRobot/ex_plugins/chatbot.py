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

from HatsuneRobot.mongo import client as db_x

lydia = db_x["CHATBOT"]


def add_chat(chat_id):
    stark = lydia.find_one({"chat_id": chat_id})
    if stark:
        return False
    lydia.insert_one({"chat_id": chat_id})
    return True


def remove_chat(chat_id):
    stark = lydia.find_one({"chat_id": chat_id})
    if not stark:
        return False
    lydia.delete_one({"chat_id": chat_id})
    return True


def get_all_chats():
    r = list(lydia.find())
    if r:
        return r
    return False


def get_session(chat_id):
    stark = lydia.find_one({"chat_id": chat_id})
    if not stark:
        return False
    return stark
