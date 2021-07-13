import click

from src.converters import chromatic_converter, raw_converter
from src.entities import NoteEnum, NOTES_PROGRESSION
from src.parser import parser


@click.group()
@click.option(
    '-s',
    '--starting-note',
    type=click.Choice(NoteEnum.__members__),
    callback=lambda c, p, v: getattr(NoteEnum, v) if v else None,
    default='DO', help='The note that we can find on line 1'
)
def cli(starting_note: NoteEnum):
    """
    Hi!
    """
    while NOTES_PROGRESSION[0] != starting_note:
        NOTES_PROGRESSION.append(NOTES_PROGRESSION.pop(0))


@cli.command()
@click.argument('filename', type=click.File('r'))
def convert_raw(filename: click.File):
    """
    Converts input file to raw note information (note and octave)
    """
    parsed = parser.parse(filename.read())
    raw_converter.convert(parsed)


@cli.command()
@click.argument('filename', type=click.File('r'))
def convert_chromatic(filename: click.File):
    """
    Converts input file to chromatic tablature
    """
    parsed = parser.parse(filename.read())
    chromatic_converter.convert(parsed)
