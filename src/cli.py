import click
import chromatic_converter

@click.group()
def cli():
    """
    Hi!
    """
    pass


@cli.command()
def convert_chromatic():
    """
    Converts input file to chromatic tablature
    """
    # chromatic_converter.convert()
    pass