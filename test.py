import json
import os
from os import getenv
from pathlib import Path
from typing import Dict, List

import telegram
from dacite import from_dict

ROOT_PATH = Path("test")
TESTS: Dict[str, List[str]] = {
    folder: os.listdir(ROOT_PATH / folder)
    for folder in os.listdir(ROOT_PATH)
    if os.path.isdir(ROOT_PATH / folder)
}
print(TESTS)


def test_issues_edited():
    from dotenv import load_dotenv

    load_dotenv()
    action_name = "pull_request"
    data = json.load(open("test/pull_request/review_requested.json"))
    from src.actions.pull_request import Action

    action = from_dict(Action, data)
    msg = action.handle(telegram.Bot(token=getenv("TELEGRAM_BOT_TOKEN") or ""))
    assert msg == "action edited not supported"
