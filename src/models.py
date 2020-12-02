from dataclasses import dataclass
from typing import List, Literal, Union


@dataclass
class Label:
    name: str
    color: str


@dataclass
class User:
    login: str
    html_url: str


@dataclass
class Repository:
    name: str
    owner: User
    html_url: str
    # description: str


@dataclass
class Milestone:
    html_url: str
    title: str
    description: str
    creator: User
    open_issues: int
    closed_issues: int
    state: Literal["open", "closed"]
    due_on: Union[str, None]  # TODO datetime


@dataclass
class Issue:
    html_url: str
    title: str
    user: User
    labels: List[Label]
    state: Literal["open", "closed"]
    assignee: Union[User, None]
    assignees: List[User]
    comments: int
    milestone: Union[Milestone, None]
    created_at: str
    updated_at: Union[str, None]  # TODO datetime
    closed_at: Union[str, None]  # TODO datetime
    body: str


@dataclass
class PullRequest:
    html_url: str
    state: Literal["open", "closed"]
    title: str
    user: User
    body: str
    labels: List[Label]
    milestone: Union[Milestone, None]
    created_at: str  # TODO datetime
    updated_at: Union[str, None]  # TODO datetime
    closed_at: Union[str, None]  # TODO datetime
    merged_at: Union[str, None]  # TODO datetime
    assignee: Union[User, None]
    assignees: List[User]
    requested_reviewers: List[User]


@dataclass
class Review:
    user: User
    body: Union[str, None]
    submitted_at: Union[str, None]
    state: Literal["commented", "APPROVED", "CHANGES_REQUESTED"]
    html_url: str
    pull_request: PullRequest
