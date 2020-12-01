from dataclasses import dataclass
from typing import Literal

from src.actions.base import Action
from src.models import PullRequest
from src.utils import escape, get_username, make_labels


@dataclass
class Action(Action):
    class Meta:
        enabled_actions = ["opened", "review_requested"]

    action: Literal[
        "opened",
        "closed",
        "review_requested",
        "labeled",
        "assigned",
        "synchronize",
        "edited",
    ]
    pull_request: PullRequest
    number: int
    # changes: None

    def make_message(self):
        msg = "PR [{}]({}){} was {} by {}".format(
            escape(self.pull_request.title),
            escape(self.pull_request.html_url),
            escape(make_labels(self.pull_request.labels)),
            escape(self.action),
            get_username(self.sender.login),
        )
        if self.action == "review_requested":
            msg += "\nReviewers requested: "
            msg += ", ".join(
                [
                    get_username(user.login)
                    for user in self.pull_request.requested_reviewers
                ]
            )
        return msg
