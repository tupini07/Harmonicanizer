from src.entities import ModifierType, NoteEnum, NoteRep


def test_correctly_build_note_instances():
    cases = [
        ("l1", NoteEnum.DO),
        ("b1", NoteEnum.RE),
        ("l2", NoteEnum.MI),
        ("b2", NoteEnum.FA),
        ("l3", NoteEnum.SOL),
        ("b3", NoteEnum.LA),
        ("l4", NoteEnum.SI),

        ("b4", NoteEnum.DO),
        ("l5", NoteEnum.RE),
        ("b5", NoteEnum.MI),
        ("l6", NoteEnum.FA),
        ("b6", NoteEnum.SOL),
        ("l7", NoteEnum.LA),
        ("b7", NoteEnum.SI),

        ("l8", NoteEnum.DO),
        ("b8", NoteEnum.RE),
        ("l9", NoteEnum.MI),
        ("b9", NoteEnum.FA),
        ("l10", NoteEnum.SOL),
        ("b10", NoteEnum.LA),
        ("l11", NoteEnum.SI),
        ("b11", NoteEnum.DO),
    ]

    for (rep, note) in cases:
        instance = NoteRep(rep)
        assert instance.note_name == note, f"{rep} should be {note}. But it is {instance.note_name}"


def test_correct_octave_identified():
    cases = [
        ("l1", NoteEnum.DO, 0),
        ("b4", NoteEnum.DO, 1),
        ("b5", NoteEnum.MI, 1),
        ("l8", NoteEnum.DO, 2),
        ("b8", NoteEnum.RE, 2),
    ]

    for (rep, note, octave) in cases:
        instance = NoteRep(rep)
        assert instance.note_name == note
        assert instance.octave == octave


def test_parses_modifiers():
    cases = [
        ("@:l1", NoteEnum.DO, ModifierType.FLAT),
        ("b1", NoteEnum.RE, ModifierType.NONE),
        ("#:l2", NoteEnum.MI, ModifierType.SHARP),
        ("x:l2", NoteEnum.MI, ModifierType.CANCEL),
    ]

    for (rep, note, modifier) in cases:
        instance = NoteRep(rep)
        assert instance.note_name == note
        assert instance.local_modifier == modifier


def test_parse_with_global_modifiers():
    global_mods = [NoteRep(x) for x in ["@:l1", "#:b4"]]
    cases = [
        ('l1', ModifierType.FLAT),
        ('x:l1', ModifierType.NONE),
        ('b2', ModifierType.NONE),
        ('b4', ModifierType.SHARP),
        ('@:b4', ModifierType.FLAT)
    ]

    for (rep, modifier) in cases:
        instance = NoteRep(rep, global_mods)
        assert instance.local_modifier == modifier
