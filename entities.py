import re
from enum import Enum
from typing import Union


class NoteEnum(Enum):
    DO = "Do"
    RE = "Re"
    MI = "Mi"
    FA = "Fa"
    SOL = "Sol"
    LA = "La"
    SI = "Si"


NOTES_PROGRESSION = [
    NoteEnum.DO,
    NoteEnum.RE,
    NoteEnum.MI,
    NoteEnum.FA,
    NoteEnum.SOL,
    NoteEnum.LA,
    NoteEnum.SI,
]


class NoteRep:
    octave: int
    note_name: NoteEnum

    def __init__(self, note_position: str, modifier: Union[str, None] = None):
        assert len(note_position) == 2 or len(note_position) == 3

        position_type, position_num = re.search(
            r'(l|b)(-?\d+)', note_position.lower()).groups()

        position_num = int(position_num)

        if position_type == "b":
            position_num = (position_num * 2) - 1
        else:
            position_num = (position_num - 1) * 2

        self.note_name = NOTES_PROGRESSION[position_num % len(
            NOTES_PROGRESSION)]
        self.octave = position_num // len(NOTES_PROGRESSION)

