from src import YamlSyntax

from pydantic import BaseModel

def test_check_yaml_syntax_from_file():

    class SimpleSyntax(BaseModel):
        version:str
    

    y = YamlSyntax.from_file(SimpleSyntax, "test.yaml")

    excpect_serialized_data = SimpleSyntax(version="v1.0.1")

    assert y.serialized_data == excpect_serialized_data

