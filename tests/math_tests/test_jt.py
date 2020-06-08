"""Tests for the jenkins_traub module of the math_core package"""

from math_core import jenkins_traub
import pytest

test_cases=[
[1,0,0,0,0,0,0,0,0,0,0,0,-1],
[1,-2,3,-4,5,-6,7],
]

test_case_answers = [
    [1.0000000+0.0000000j, -1.0000000+0.0000000j, 0.0000000-1.0000000j, 0.0000000+1.0000000j, -0.8660254-0.5000000j, 0.8660254+0.5000000j, -0.5000000-0.8660254j, 0.5000000+0.8660254j, 0.5000000-0.8660254j, -0.5000000+0.8660254j, 0.8660254-0.5000000j, -0.8660254+0.5000000j],
    [-0.7103789-1.106845j, -0.7103789+1.106845j, 0.4025091-1.341667j, 0.4025091+1.341667j, 1.307870-0.5932947j, 1.307870+0.5932947j],
]

def test_higher_power_poly():

    for k, l in zip(test_cases, test_case_answers):

        ans = jenkins_traub.real_poly(k,len(k)-1)
        #print("For test case "+str(k)+" answers are: ", ans)
        chk = [False] * len(ans)
        for i in range(0,len(ans)):
            for n in l:
                #print(str(ans[i])+" == "+str(n)+" = "+str(ans[i] == pytest.approx(n)), chk)
                if ans[i] == pytest.approx(n):
                    chk[i] = True
                    break
                elif ans[i] == pytest.approx(n, rel=1e-5):
                    chk[i] = True
                    break

        print(chk)
        for i in chk:
            if not i:
                raise Exception("Jenkins Traub did not calculate the right answers...")
