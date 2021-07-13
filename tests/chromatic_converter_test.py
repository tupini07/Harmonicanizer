from src.converters.chromatic_converter import (_calc_position_for_note,
                                                _convert_note_to_chromatic, _draw_note)
from src.entities import ModifierType, NoteEnum, NoteRep


def test__draw_note():
    cases = [
        (ModifierType.SHARP, 2, True, '<-2'),
        (ModifierType.NONE, 2, False, '+2'),
        (ModifierType.NONE, 4, True, '-4'),
    ]

    for (mod, pos, draw, expected) in cases:
        assert _draw_note(mod, pos, draw) == expected


def test__calc_position_for_note():
    cases = [
        ('l1', (1, False)),
        ('b1', (1, True)),
        ('l4', (4, True)),
        ('l5', (5, True)),
        ('b5', (6, False)),
    ]

    for (rep, (expected_pos, expected_draw)) in cases:
        note = NoteRep(rep)
        pos, draw = _calc_position_for_note(note)

        assert pos == expected_pos
        assert draw == expected_draw


def test__convert_note_to_chromatic():
    prev_note = NoteRep('l1')
    prev_note.note_name = NoteEnum.FA
    prev_note.octave = 0

    next_note = NoteRep('l1')
    next_note.note_name = NoteEnum.DO
    next_note.octave = 1

    pos, rep = _convert_note_to_chromatic(next_note, prev_note, 2)
    assert pos == 4
    assert rep == '+4'

    next_note.note_name = NoteEnum.LA
    next_note.octave = 1

    pos, rep = _convert_note_to_chromatic(next_note, prev_note, 2)
    assert pos == 7
    assert rep == '-7'
