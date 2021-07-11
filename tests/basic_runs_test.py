from src.parser import parser
from src import chromatic_converter


def test_pipeline_processes_schema():
    with open('schema.hcs', 'r') as f_file:
        contents = f_file.read()

        parsed = parser.parse(contents)
        chromatic_converter.convert(parsed)
