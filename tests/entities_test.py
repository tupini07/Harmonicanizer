from src.entities import NoteEnum, NoteRep, ModifierType


def test_correctly_build_note_instances():
    equivalences = [
        ("l1", NoteEnum.DO),
        ("b1", NoteEnum.RE),
        ("l2", NoteEnum.MI),
        ("b2", NoteEnum.FA),
        ("l3", NoteEnum.SOL),
        ("b3", NoteEnum.LA),
        ("l4", NoteEnum.SI),
        ("b4", NoteEnum.DO),
    ]

    for (rep, note) in equivalences:
        instance = NoteRep(rep)
        assert instance.note_name == note, f"{rep} should be {note}. But it is {instance.note_name}"


def test_correct_octave_identified():
    equivalences = [
        ("l1", NoteEnum.DO, 0),
        ("b4", NoteEnum.DO, 1),
        ("b5", NoteEnum.MI, 1),
        ("l8", NoteEnum.DO, 2),
        ("b8", NoteEnum.RE, 2),
    ]

    for (rep, note, octave) in equivalences:
        instance = NoteRep(rep)
        assert instance.note_name == note
        assert instance.octave == octave


def test_parses_modifiers():
    equivalences = [
        ("@:l1", NoteEnum.DO, ModifierType.FLAT),
        ("b1", NoteEnum.RE, ModifierType.NONE),
        ("#:l2", NoteEnum.MI, ModifierType.SHARP),
        ("x:l2", NoteEnum.MI, ModifierType.CANCEL),
    ]

    for (rep, note, modifier) in equivalences:
        instance = NoteRep(rep)
        assert instance.note_name == note
        assert instance.local_modifier == modifier