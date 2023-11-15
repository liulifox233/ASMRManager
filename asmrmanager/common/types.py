import uuid
from dataclasses import dataclass
from enum import Enum
from typing import NewType

RJID = NewType("RJID", int)
RJName = NewType("RJName", str)


class PRIVACY(Enum):
    PUBLIC = 2
    NON_PUBLIC = 1
    PRIVATE = 0


@dataclass
class PlayListItem:
    id: uuid.UUID
    name: str
    privacy: PRIVACY
    desc: str
    works_count: int
    latest_work_id: RJID
