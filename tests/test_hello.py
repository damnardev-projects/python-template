import pytest
from src.hello import main


def test_main_with_custom_name():
    name = "Alice"

    result = main(name)
    assert isinstance(result, str)
    assert result == "Hello, Alice!"
