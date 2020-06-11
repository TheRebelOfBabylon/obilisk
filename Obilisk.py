from math_core.Equation import Equation
from math_core.Arithmetic import Arithmetic

from typing import List, Tuple, Union

def decode(input_eqn: str) -> Tuple[Equation, str]:

    eqn = Equation(input_eqn)
    if eqn.var_type[0] == "":

        return eqn, "compute"

    elif len(eqn.var_type) > 1:

        #raise NotImplementedError("Multivariable problems are not yet supported.")
        eqn.solution.append("Multivariable problems are not yet supported.")
        return eqn, "not supported"

    else:

        return eqn, "solve"

def compute(input: Equation) -> Tuple[List[str], List[Union[int, float, complex]]]:

    ans = []
    eqn = Arithmetic(input.eqn_string)
    ans.append(eqn.calculate())

    return eqn.solution, ans