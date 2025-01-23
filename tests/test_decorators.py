import pytest

from src.decorators import log


def test_log(capsys) -> None:
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_error(capsys):
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        return x + y

    with pytest.raises(TypeError):
        my_function(2, "3")
    captured = capsys.readouterr()
    assert f"my_function error TypeError\n" in captured.out
