var_dict = {

	"x":"y"

}

var_type="x"

string_eqn = "16+cos(0)+(3x+1)=4(3x+1)"

print(string_eqn)

string_eqn = string_eqn.replace("(3x+1)",var_dict[var_type])

print(string_eqn)

