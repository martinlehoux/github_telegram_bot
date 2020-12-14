from os import getenv
from typing import List

from src.models import Label


def make_labels(labels: List[Label]) -> str:
    labels_str = "-".join([label.name for label in labels])
    if labels_str:
        labels_str = f" ({labels_str})"
    return labels_str


def get_username(github_username: str) -> str:
    return escape(getenv(github_username, github_username))


def escape(string: str) -> str:
    chars = "[]()_-#"
    for char in chars:
        string = string.replace(char, rf"\{char}")
    return string
