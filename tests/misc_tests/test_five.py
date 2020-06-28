from math_core.Algebra import Algebra
eqn = Algebra("69*(((x-1)/(x+2))^8-((x-1)/(x+2))^6)=x+3")
l_div, r_div = eqn.identify_div()
eqn.redundant_br()
eqn.multiply_br(l_div)
eqn.redundant_div(l_div)
eqn.bracket_remover()