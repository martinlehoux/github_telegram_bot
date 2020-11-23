import json
from importlib import import_module
from os import getenv
from typing import Type

import telegram
from dacite import from_dict

from src.actions.base import Action
from src.utils import Event


def handler(event, context):
    try:
        event = from_dict(Event, event)
        module = import_module(f"src.actions.{event.action_name}")
        actionClass: Type[Action] = getattr(module, "Action")
        action = from_dict(actionClass, json.loads(event.body or ""))

        bot = telegram.Bot(token=getenv("TELEGRAM_BOT_TOKEN") or "")
        action.handle(bot)
        return ""

    except (ImportError, AttributeError):
        print(f"Action {event.action_name} not supported")
        return ""


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
