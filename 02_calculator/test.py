# test.py

import pytest

def test_addition(monkeypatch, capsys):
    inputs = iter(["+", "2", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    import main  # runs the script

    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out


def test_subtraction(monkeypatch, capsys):
    inputs = iter(["-", "5", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    import importlib
    import main
    importlib.reload(main)

    captured = capsys.readouterr()
    assert "Result: 2.0" in captured.out


def test_multiplication(monkeypatch, capsys):
    inputs = iter(["*", "4", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    import importlib
    import main
    importlib.reload(main)

    captured = capsys.readouterr()
    assert "Result: 12.0" in captured.out


def test_division(monkeypatch, capsys):
    inputs = iter(["/", "10", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    import importlib
    import main
    importlib.reload(main)

    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out


def test_divide_by_zero(monkeypatch, capsys):
    inputs = iter(["/", "10", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    import importlib
    import main
    importlib.reload(main)

    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out