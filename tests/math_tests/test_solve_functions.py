"""Tests for the solve_functions module in the math_core package"""

import pytest

from math_core.solve_functions import Solve_Func, rearrange, solver, find_asymptotes
from math_core.BEMDAS_algo_v3 import bracketify, grouping, stringify

test_cases_l = [
    "69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)",
    "69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)",
    "69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)^2",
#   "((3x-5)*((x-1)/(x+2))/(x+3))^8-(((x-1)/(x+2))/(x+3))^6",
]
foiled_test_cases_l = [
    "-414.0x^13.0-2691.0x^12.0-2484.0x^11.0+15939.0x^10.0+26910.0x^9.0-42849.0x^8.0-84456.0x^7.0+75141.0x^6.0+126684.0x^5.0-95220.0x^4.0-86112.0x^3.0+69552.0x^2.0+13248.0x-13248.0",
    "-414.0x^13.0-2691.0x^12.0-2484.0x^11.0+15939.0x^10.0+26910.0x^9.0-42849.0x^8.0-84456.0x^7.0+75141.0x^6.0+126684.0x^5.0-95220.0x^4.0-86112.0x^3.0+69552.0x^2.0+13248.0x-13248.0",
    "2484.0x^26.0+32292.0x^25.0+134757.0x^24.0+2484.0x^23.0-1476738.0x^22.0-2732400.0x^21.0+6100083.0x^20.0+21203424.0x^19.0-10601712.0x^18.0-86589756.0x^17.0-5212053.0x^16.0+234770292.0x^15.0+65486934.0x^14.0-461224152.0x^13.0-144985491.0x^12.0+677292408.0x^11.0+153834120.0x^10.0-734250528.0x^9.0-49292496.0x^8.0+554349312.0x^7.0-64703232.0x^6.0-258812928.0x^5.0+73605888.0x^4.0+59774976.0x^3.0-24164352.0x^2.0-5087232.0x+2543616.0",
]
# test_cases_r = [
#     "x+3",
#     "x/(x+3)",
#     "x/(x+3)",
#     "3",
# ]

def test_all_cases():

    for i in range(0,len(test_cases_l)):
        a, a_var = bracketify(test_cases_l[i])
        a, a_deg = grouping(a)

        a = Solve_Func(a, a_var[0])
        a_div = a.identify_div()
        print(a_div)

        a = a.redundant_br()
        print(a.eqn)

        a = a.multiply_br(a_div)

        a = a.redundant_div(a_div)
        print(a.eqn)

        a = a.bracket_remover()
        a_string = stringify(a.eqn)

        assert a_string == foiled_test_cases_l[i]