import pytest

from mikm.converter import conversion
from mikm.converter import UnitError


def test_right_conversion():
    assert conversion("1 km") == 0.62
    assert conversion("7 km") == 4.35
    assert conversion("14 km") == 8.7

    assert conversion("1 mi") == 1.61
    assert conversion("7 mi") == 11.27
    assert conversion("14 mi") == 22.53


def test_wrong_conversion():
    assert conversion("1 mi") != 0.62
    assert conversion("7 mi") != 4.35
    assert conversion("14 mi") != 8.7

    assert conversion("1 km") != 1.61
    assert conversion("7 km") != 11.27
    assert conversion("14 km") != 22.53


def test_TypeError():
    with pytest.raises(TypeError):
        assert conversion(1)


def test_without_unit():
    with pytest.raises(UnitError):
        assert conversion("29")
