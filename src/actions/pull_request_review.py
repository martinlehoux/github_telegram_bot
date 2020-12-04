from dataclasses import dataclass
from typing import Literal

from src.actions.base import Action
from src.models import PullRequest, Review, User
from src.utils import escape, get_username


@dataclass
class Action(Action):
    class Meta:
        enabled_actions = ["submitted"]

    action: Literal["submitted", "edited", "dismissed"]
    pull_request: PullRequest
    review: Review

    def make_message(self):
        msg = "PR [{}]({}) received a review from {}: {}".format(
            escape(self.pull_request.title),
            escape(self.pull_request.html_url),
            get_username(self.sender.login),
            escape(self.pull_request.state.lower()),
        )
        return msg
