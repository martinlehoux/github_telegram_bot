from dataclasses import dataclass
from typing import Literal

from src.actions.base import Action
from src.models import Issue
from src.utils import get_username, make_labels


@dataclass
class Action(Action):
    action: Literal["opened", "reopened", "closed", "edited"]
    issue: Issue

    def make_message(self):
        return "Issue [{}]({}){} was {} by {}".format(
            self.issue.title,
            self.issue.html_url,
            make_labels(self.issue.labels),
            self.action,
            get_username(self.sender.login),
        )
