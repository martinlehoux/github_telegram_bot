from importlib import import_module
from os import getenv
from typing import Type

import telegram
from dacite import from_dict

from src.actions.base import Action


def handler(request):
    event = request.get_json(force=True)
    action_name = request.headers.get("x-github-event", "noop")
    try:
        module = import_module(f"src.actions.{action_name}")
        actionClass: Type[Action] = getattr(module, "Action")
        action = from_dict(actionClass, event)

        bot = telegram.Bot(token=getenv("TELEGRAM_BOT_TOKEN") or "")
        msg = action.handle(bot)
        return {"msg": msg}

    except (ImportError, AttributeError):
        print(f"Action {action_name} not supported")
        return ""


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
