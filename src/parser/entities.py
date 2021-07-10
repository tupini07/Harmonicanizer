from typing import List

from src.entities import NoteRep


class Line:
    notes: List[NoteRep]

    def __init__(self, raw_line: str, global_modifiers: List[NoteRep]):
        notes = [NoteRep(element, global_modifiers)
                 for element in raw_line.split(' ')]


class Block:
    lines: List[Line]

    def __init__(self, raw_block: List[str], global_modifiers: List[NoteRep]):
        self.lines = [Line(line, global_modifiers) for line in raw_block]


class HcsFile:
    title: str
    global_modifiers: List[NoteRep]
    blocks: List[Block]

    def __init__(self, title: str, global_modifiers: List[NoteRep], blocks: List[Block]):
        self.title = title
        self.global_modifiers = global_modifiers
        self.blocks = blocks
