from math_core.BEMDAS_algo_v3 import main

import pytest

test_cases = [
    "69+((21/3)^8.2)/(3*cos(45))",
    "sqrt(-3)+2",
    "3x^2+6x-78=x^2+5",
    "x^2+y^2=9",
]

test_case_answers = [
    4010561.1557757357,
    2+1.7320508075689j,
    [-8.114378278, 5.114378278],
    ValueError,
]

#def test_cases_on_main():
   # for i, j in zip(test_cases, test_case_answers):
        #assert complex(main(i)[1][0]).real == j

@pytest.mark.parametrize("tc, err", [(test_cases[3], ValueError)])
def test_multivar_problems(tc, err):
    """This test ensures that ValueError is raised if a multivariable problem is given to main."""
    with pytest.raises(err):
        main(tc)