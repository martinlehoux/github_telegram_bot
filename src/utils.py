from os import getenv
from typing import List

from src.models import Label


def make_labels(labels: List[Label]) -> str:
    labels_str = "-".join([label.name for label in labels])
    if labels_str:
        labels_str = r" \(" + labels_str + r"\)"
    return labels_str


def get_username(github_username: str) -> str:
    return escape(getenv(github_username, github_username))


def escape(string: str) -> str:
    string = string.replace("[", r"\[")
    string = string.replace("]", r"\]")
    string = string.replace("_", r"\_")
    string = string.replace("-", r"\-")
    return string
