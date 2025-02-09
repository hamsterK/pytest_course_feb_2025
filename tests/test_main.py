import pytest
from contextlib import nullcontext as does_not_raise

from app.main import Calculator


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 10.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError)),
            (5, 0, -5, pytest.raises(ZeroDivisionError)),
        ]
                            )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 3, does_not_raise()),
            (5, "-1", 4, pytest.raises(TypeError)),
        ]
                            )
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y) == res
