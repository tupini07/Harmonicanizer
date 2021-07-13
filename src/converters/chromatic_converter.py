import re

from src.entities import NOTES_PROGRESSION, ModifierType, NoteEnum, NoteRep
from src.parser.entities import HcsFile

_HARMONICA_NOTES = {
    1: {
        NoteEnum.DO: 1,
        NoteEnum.RE: 1,
        NoteEnum.MI: 2,
        NoteEnum.FA: 2,
        NoteEnum.SOL: 3,
        NoteEnum.LA: 3,
        NoteEnum.SI: 4,
    },
    2: {
        NoteEnum.DO: 5,
        NoteEnum.RE: 5,
        NoteEnum.MI: 6,
        NoteEnum.FA: 6,
        NoteEnum.SOL: 7,
        NoteEnum.LA: 7,
        NoteEnum.SI: 8,
    },
    3: {
        NoteEnum.DO: 9,
        NoteEnum.RE: 9,
        NoteEnum.MI: 10,
        NoteEnum.FA: 10,
        NoteEnum.SOL: 11,
        NoteEnum.LA: 11,
        NoteEnum.SI: 12,
    },
}


def _calc_position_for_note(note: NoteRep) -> (int, bool):
    # octave_start_pos = max(1, note.octave * 5)
    # calcd_new_pos = octave_start_pos + \
    #     (NOTES_PROGRESSION.index(note.note_name) // 2)

    is_draw = (NOTES_PROGRESSION.index(note.note_name)+1) % 2 == 0
    if note.note_name == NoteEnum.SI:
        is_draw = True

    return _HARMONICA_NOTES[note.octave+1][note.note_name], is_draw


def _draw_note(modifier: ModifierType, position: int, draw: bool) -> str:
    assert modifier == ModifierType.NONE or modifier == ModifierType.SHARP, 'Cannot render a chromatic note that has FLAT modifier'

    modifier = '<' if modifier == ModifierType.SHARP else ''
    draw = '-' if draw else '+'
    return f'{modifier}{draw}{position}'


def _convert_note_to_chromatic(current_note: NoteRep, previous_note: NoteRep, last_position_hole: int) -> (str, int):
    # Chromatic harmonica doesn't support FLAT notes, so we need to standardize to SHARP
    # luckily, a FLAT note is the same as the SHARP of the previous note
    if current_note.local_modifier == ModifierType.FLAT:
        current_note.local_modifier = ModifierType.SHARP

        current_note_index = NOTES_PROGRESSION.index(current_note.note_name)
        if current_note_index == 0:
            current_note.octave -= 0

        current_note.note_name = NOTES_PROGRESSION[(
            current_note_index-1) % len(NOTES_PROGRESSION)]

    new_note_pos, new_note_draw = _calc_position_for_note(current_note)

    # if Do, then check which Do we want to write down
    # Since it might be the Do at the end/beginning of the current octave (ideally yes)
    if current_note.note_name == NoteEnum.DO:
        old_note_pos, _ = _calc_position_for_note(previous_note)

        difference = new_note_pos - old_note_pos
        octave_difference = current_note.octave - previous_note.octave

        if abs(octave_difference) <= 1:
            if difference > 0:
                new_note_pos -= 1

    return new_note_pos, _draw_note(current_note.local_modifier, new_note_pos, new_note_draw)


def _iter_convert(inpt: HcsFile) -> str:
    last_note = NoteRep('l1')
    last_position_hole = 1

    all_notes = []
    for block in inpt.blocks:

        notes_for_block = []
        for line in block.lines:

            notes_for_lines = []
            for note in line.notes:

                last_position_hole, rep = _convert_note_to_chromatic(
                    note, last_note, last_position_hole
                )

                notes_for_lines.append(rep)

            if len(notes_for_lines) > 0:
                notes_for_block.append(notes_for_lines)

        if len(notes_for_block) > 0:
            all_notes.append(notes_for_block)

    return all_notes


def convert(inpt: HcsFile):
    """
    Takes the input HcsFile and does all the conversion pipline for outputing chromatic
    harmonica notes. 

    This method will print the notes directly to the console.
    """
    print()
    print(inpt.title)

    all_block_notes = _iter_convert(inpt)

    for block_notes in all_block_notes:
        print()
        for line_notes in block_notes:
            print('  '.join(line_notes))

    print()
