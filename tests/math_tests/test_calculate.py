"""Tests for the calculate function in the BEMDAS_algo_v3 module."""

from math_core.BEMDAS_algo_v3 import bracketify, calculate
import pytest

test_cases = [
    "69+(8-2)^7.2/log(4^2,3)",
    "69+((21/3)^8.2)/(3*cos(45))",
    "sqrt(-3)+2",
    "sqrt(-3)^2+2"
]

test_case_answers = [
    1011019.7587870818,
    4010561.15577573576008115984875933669150617719169796630,
    2+1.7320508075689j,
    -1,
]

def test_all_cases():

    for i in range(0, len(test_cases)):
        br_tc, var_type = bracketify(test_cases[i])
        ans = calculate(br_tc, 0)

        assert complex(ans) == pytest.approx(test_case_answers[i])