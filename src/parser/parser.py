from typing import List

from src.entities import NoteRep
from src.parser.entities import Block, HcsFile


def _extract_raw_blocks(lines: List[str]) -> List[List[str]]:
    """
    Gets a list of raw lines where every element is either a newline character
    or a line of notes and returns a list of groups, where every group is a
    block of notes.
    """
    current_block = []
    all_blocks = [current_block]

    for line in lines:
        line = line.strip()
        if line == '':
            if len(current_block) > 0:
                current_block = []
                all_blocks.append(current_block)
        else:
            current_block.append(line)

    # If last block is empty then remove it from results
    if len(current_block) == 0:
        all_blocks = all_blocks[:-1]

    return all_blocks


def parse(content: str) -> HcsFile:
    """
    Parses the contents of a _Harmonicanizer Notation_ file.
    """
    lines = content.split("\n")

    # Extract title
    title = [l for l in lines if l.startswith("!!")]
    l_title = len(title)

    # Throw error if there is more than one title
    if l_title > 1:
        raise AssertionError(
            f'There can only be one title. There were {l_title} titles provided as input')

    title = '' if l_title == 0 else title[0]
    title = '!!'.join(title.split('!!')[1:]).strip()

    # Remove comments
    lines = [l for l in lines if not l.startswith(
        "<<") and not l.startswith("!!")]

    # Get mods and join them
    mod_lines = [l for l in lines if l.startswith("mods:")]
    mods = set(' '.join(mod_lines).split(' '))
    mods.remove('mods:')
    mods = [NoteRep(raw_mod) for raw_mod in mods]

    lines = [l for l in lines if not l.startswith('mods:')]

    # Separate in blocks. All remaining lines are either newlines or note lines
    raw_blocks = _extract_raw_blocks(lines)
    blocks = [Block(group, mods) for group in raw_blocks]

    return HcsFile(title, mods, blocks)
