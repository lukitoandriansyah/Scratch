import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Task:
    id: int
    title: str
    ramk: int
    created: datetime
    updated: datetime
    description: str | None = None
    completedStatus: bool = False


tasks = [
    Task(
        id=123,
        title="One Take",
        rank=0,
        created=datetime.now(),
        updated=datetime.now()
    ),
    Task(
        id=65,
        title="One Took",
        rank=1,
        created=datetime.now(),
        upadted=datetime.now()
    )
]
