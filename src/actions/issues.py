from dataclasses import dataclass
from typing import Literal

from src.actions.base import Action
from src.models import Issue
from src.utils import escape, get_username, make_labels


@dataclass
class Action(Action):
    class Meta:
        enabled_actions = ["opened", "reopened", "closed"]

    action: Literal["opened", "reopened", "closed", "edited", "labeled"]
    issue: Issue

    def make_message(self):
        return "Issue [{}]({}){} was {} by {}".format(
            escape(self.issue.title),
            escape(self.issue.html_url),
            make_labels(self.issue.labels),
            escape(self.action),
            get_username(self.sender.login),
        )
