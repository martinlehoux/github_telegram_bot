from dataclasses import dataclass
from os import getenv
from typing import Dict, List

from src.models import Label


def make_labels(labels: List[Label]) -> str:
    labels_str = "-".join([label.name for label in labels])
    if labels_str:
        labels_str = r" \(" + labels_str + r"\)"
    return labels_str


def get_username(github_username: str) -> str:
    return getenv(github_username, github_username)


@dataclass
class Event:
    headers: Dict[str, str]
    body: str

    @property
    def action_name(self):
        return self.headers["x-github-event"]
