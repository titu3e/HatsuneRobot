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

from HatsuneRobot.modules.disable import (
    DisableAbleCommandHandler,
    DisableAbleMessageHandler,
)
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    InlineQueryHandler,
)
from telegram.ext.filters import BaseFilter
from HatsuneRobot import dispatcher as d, LOGGER
from typing import Optional, Union, List


class HatsuneHandler:
    def __init__(self, d):
        self._dispatcher = d

    def command(
        self,
        command: str,
        filters: Optional[BaseFilter] = None,
        admin_ok: bool = False,
        pass_args: bool = False,
        pass_chat_data: bool = False,
        run_async: bool = True,
        can_disable: bool = True,
        group: Optional[Union[int]] = 40,
    ):
        def _command(func):
            try:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            admin_ok=admin_ok,
                        ),
                        group,
                    )
                else:
                    self._dispatcher.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                        ),
                        group,
                    )
                LOGGER.debug(
                    f"[HatsuneCMD] Loaded handler {command} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            admin_ok=admin_ok,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                else:
                    self._dispatcher.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                LOGGER.debug(
                    f"[HatsuneCMD] Loaded handler {command} for function {func.__name__}"
                )

            return func

        return _command

    def message(
        self,
        pattern: Optional[str] = None,
        can_disable: bool = True,
        run_async: bool = True,
        group: Optional[Union[int]] = 60,
        friendly=None,
    ):
        def _message(func):
            try:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, run_async=run_async
                        ),
                        group,
                    )
                else:
                    self._dispatcher.add_handler(
                        MessageHandler(pattern, func, run_async=run_async), group
                    )
                LOGGER.debug(
                    f"[HatsuneMSG] Loaded filter pattern {pattern} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, run_async=run_async
                        )
                    )
                else:
                    self._dispatcher.add_handler(
                        MessageHandler(pattern, func, run_async=run_async)
                    )
                LOGGER.debug(
                    f"[HatsuneMSG] Loaded filter pattern {pattern} for function {func.__name__}"
                )

            return func

        return _message

    def callbackquery(self, pattern: str = None, run_async: bool = True):
        def _callbackquery(func):
            self._dispatcher.add_handler(
                CallbackQueryHandler(
                    pattern=pattern, callback=func, run_async=run_async
                )
            )
            LOGGER.debug(
                f"[HatsuneCALLBACK] Loaded callbackquery handler with pattern {pattern} for function {func.__name__}"
            )
            return func

        return _callbackquery

    def inlinequery(
        self,
        pattern: Optional[str] = None,
        run_async: bool = True,
        pass_user_data: bool = True,
        pass_chat_data: bool = True,
        chat_types: List[str] = None,
    ):
        def _inlinequery(func):
            self._dispatcher.add_handler(
                InlineQueryHandler(
                    pattern=pattern,
                    callback=func,
                    run_async=run_async,
                    pass_user_data=pass_user_data,
                    pass_chat_data=pass_chat_data,
                    chat_types=chat_types,
                )
            )
            LOGGER.debug(
                f"[HatsuneINLINE] Loaded inlinequery handler with pattern {pattern} for function {func.__name__} | PASSES USER DATA: {pass_user_data} | PASSES CHAT DATA: {pass_chat_data} | CHAT TYPES: {chat_types}"
            )
            return func

        return _inlinequery


Hatsunecmd = HatsuneHandler(d).command
Hatsunemsg = HatsuneHandler(d).message
Hatsunecallback = HatsuneHandler(d).callbackquery
Hatsuneinline = HatsuneHandler(d).inlinequery
