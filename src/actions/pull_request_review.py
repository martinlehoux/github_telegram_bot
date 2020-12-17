from dataclasses import dataclass
from typing import Literal

from src.actions.base import Action
from src.models import PullRequest, Review
from src.utils import escape, get_username


@dataclass
class Action(Action):
    class Meta:
        enabled_actions = ["submitted"]

    action: Literal["submitted", "edited", "dismissed"]
    pull_request: PullRequest
    review: Review

    def make_message(self):
        if self.review.state == "commented":
            return ""
        prefix = ""
        if self.review.state == "approved":
            prefix = "✅ "
        if self.review.state == "changes_requested":
            prefix = "❌ "
        msg = "{}PR [{}]({}) received a review for {}: {}\n{}".format(
            prefix,
            escape(self.pull_request.title),
            escape(self.pull_request.html_url),
            get_username(self.pull_request.user.login),
            escape(self.review.state.lower()),
            escape(self.review.body or ""),
        )
        return msg
