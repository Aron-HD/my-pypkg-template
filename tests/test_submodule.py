import pytest
from pkg.subpkg.submodule import ClassName


@pytest.mark.parametrize(
    "value, expected", [
        (1, 2),
        (2, 4)
    ]
)
def test_do_something(value, expected):
    _class = ClassName
    assert _class.do_something(value) == expected
