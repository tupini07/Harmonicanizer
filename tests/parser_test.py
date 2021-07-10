from src.parser import parser
from textwrap import dedent
from src.entities import ModifierType, NoteEnum


def test__extract_raw_blocks():
    input = [
        '', '',
        'l1 l2 l3 l4', 'l5 l6 l7',
        '', '', '', '', '',
        'b1 b2 b3', 'b4 b5 b6'
    ]

    raw_blocks = parser._extract_raw_blocks(input)

    assert len(raw_blocks) == 2
    assert len(raw_blocks[0]) == 2
    assert len(raw_blocks[1]) == 2


def test_simple_parsing():
    content = dedent("""
    !! some title

    mods: #:l2 @:b9

    << a comment before adding more mods
    mods: @:l4

    << Then a block
    l1 l2 @:b4 l9
    #:b6 #:b2 @:l1

    << another block
    l1 l2 l3 l4
    b1 b2 b3 b4
    b1 b2 b3 b4
    b1 b2 b3 b4



    << some comment after empty lines
    """)

    parsed = parser.parse(content)
    
    assert parsed.title == "some title"
    assert len(parsed.global_modifiers) == 3
    assert len(parsed.blocks) == 2
    assert len(parsed.blocks[0].lines) == 2
    assert len(parsed.blocks[1].lines) == 4