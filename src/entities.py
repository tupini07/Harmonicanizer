import re
from enum import Enum
from typing import List, Union


class NoteEnum(Enum):
    DO = "Do"
    RE = "Re"
    MI = "Mi"
    FA = "Fa"
    SOL = "Sol"
    LA = "La"
    SI = "Si"


class ModifierType(Enum):
    SHARP = 1
    FLAT = 2
    # TODO: Cancel modifier is probably worthless since note will end up having NONE modifier
    CANCEL = 3
    NONE = 4


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
    local_modifier: ModifierType

    def __init__(self, note_definition: str, global_modifiers: List = []):
        note_definition = note_definition.lower()

        if ':' in note_definition:
            raw_modifier, raw_note = note_definition.split(':')
        else:
            raw_modifier, raw_note = (None, note_definition)

        # set local modifer
        if raw_modifier == 'x':
            self.local_modifier = ModifierType.CANCEL
        elif raw_modifier == '@':
            self.local_modifier = ModifierType.FLAT
        elif raw_modifier == '#':
            self.local_modifier = ModifierType.SHARP
        elif raw_modifier is None:
            self.local_modifier = ModifierType.NONE
        else:
            raise AssertionError(f'Unknown modifier: {raw_modifier}')

        # set note and octave
        position_type, position_num = re.search(
            r'(l|b)(-?\d+)', raw_note).groups()

        position_num = int(position_num)

        if position_type == "b":
            position_num = (position_num * 2) - 1
        else:
            position_num = (position_num - 1) * 2

        self.note_name = NOTES_PROGRESSION[position_num % len(
            NOTES_PROGRESSION)]
        self.octave = position_num // len(NOTES_PROGRESSION)

        # add global modifier
        for mod in global_modifiers:
            if mod.note_name == self.note_name and mod.octave == self.octave:
                if self.local_modifier == ModifierType.CANCEL:
                    self.local_modifier = ModifierType.NONE
                elif self.local_modifier != ModifierType.CANCEL and self.local_modifier != ModifierType.NONE:
                    self.local_modifier = self.local_modifier
                else:
                    self.local_modifier = mod.local_modifier
