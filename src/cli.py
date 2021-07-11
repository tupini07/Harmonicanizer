import click

from src import chromatic_converter
from src.parser import parser


@click.group()
def cli():
    """
    Hi!
    """
    pass


@cli.command()
@click.argument('filename', type=click.File('r'))
def convert_chromatic(filename: click.File):
    """
    Converts input file to chromatic tablature
    """
    parsed = parser.parse(filename.read())
    chromatic_converter.convert(parsed)
