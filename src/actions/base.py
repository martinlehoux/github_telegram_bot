from dataclasses import dataclass
from os import getenv
from typing import List

import telegram
from src.models import Repository, User


@dataclass
class Action:
    action: str
    enabled_actions: List[str]
    sender: User
    repository: Repository
    # organization: None

    def make_message(self) -> str:
        raise NotImplementedError()

    def handle(self, bot: telegram.Bot) -> str:
        if self.action in self.enabled_actions:
            bot.send_message(
                chat_id=getenv("TELEGRAM_CHAT_ID"),
                text=self.make_message(),
                parse_mode=telegram.ParseMode.MARKDOWN_V2,
                disable_web_page_preview=True,
            )
            return "message sent"
        else:
            return f"action {self.action} not supported"
