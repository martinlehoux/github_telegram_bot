import json
import os
from pathlib import Path
from typing import Dict, List

from dacite import from_dict

ROOT_PATH = Path("test")
TESTS: Dict[str, List[str]] = {
    folder: os.listdir(ROOT_PATH / folder)
    for folder in os.listdir(ROOT_PATH)
    if os.path.isdir(ROOT_PATH / folder)
}
print(TESTS)


def test_issues_edited():
    action_name = "pull_request"
    data = json.load(open("test/pull_request/review_requested.json"))
    from src.actions.pull_request import Action

    action = from_dict(Action, data)
    msg = action.handle(None)
    assert msg == "action edited not supported"
