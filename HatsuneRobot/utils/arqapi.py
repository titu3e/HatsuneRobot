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

import json
import sys
from random import randint
from time import time

import aiohttp
from HatsuneRobot import aiohttpsession
from aiohttp import ClientSession

from google_trans_new import google_translator
from Python_ARQ import ARQ
from search_engine_parser import GoogleSearch

from HatsuneRobot import BOT_ID, OWNER_ID, ARQ_API_URL, ARQ_API_KEY
from HatsuneRobot import pbot

ARQ_API = "WZQUBA-PFAZQJ-OMIINH-MIVHYM-ARQ"
ARQ_API_KEY = "WZQUBA-PFAZQJ-OMIINH-MIVHYM-ARQ"
SUDOERS = OWNER_ID
ARQ_API_URL = "https://thearq.tech"

# Aiohttp Client
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

app = pbot
import socket
