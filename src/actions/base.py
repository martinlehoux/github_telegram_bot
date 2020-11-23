from dataclasses import dataclass
from os import getenv
from typing import List, Union

import telegram
from src.models import Repository, User


@dataclass
class Action:
    class Meta:
        enabled_actions: List[str]

    action: str
    sender: User
    repository: Repository
    # organization: None

    def make_message(self) -> str:
        raise NotImplementedError()

    def handle(self, bot: Union[telegram.Bot, None]) -> str:
        if self.action in self.Meta.enabled_actions:
            msg = self.make_message()
            if bot is not None:
                bot.send_message(
                    chat_id=getenv("TELEGRAM_CHAT_ID"),
                    text=msg,
                    parse_mode=telegram.ParseMode.MARKDOWN_V2,
                    disable_web_page_preview=True,
                )
            return "message sent"
        else:
            return f"action {self.action} not supported"
