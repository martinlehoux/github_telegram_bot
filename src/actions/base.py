from dataclasses import dataclass
from os import getenv

import telegram
from src.models import Repository, User


@dataclass
class Action:
    sender: User
    repository: Repository
    # organization: None

    def make_message(self) -> str:
        raise NotImplementedError()

    def handle(self, bot: telegram.Bot):
        bot.send_message(
            chat_id=getenv("TELEGRAM_CHAT_ID"),
            text=self.make_message(),
            parse_mode=telegram.ParseMode.MARKDOWN_V2,
            disable_web_page_preview=True,
        )
