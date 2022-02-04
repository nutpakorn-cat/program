from flask import Flask
from flask import jsonify
from flask import request

from pulp import *

from utilities.InputHelper import *
from utilities.SizeHelper import *
from utilities.ModelHelper import *

app = Flask(__name__)

model = LpProblem('model 2', LpMaximize)

d = dict()

c_size_1 = read_range_1('c_size')[0]
i_size_1 = read_range_1('i_size')[0]
j_size_1 = read_range_1('j_size')[0]
k_size_1 = read_range_1('k_size')[0]
t_size_1 = read_range_1('t_size')[0]

S = read_input_1('S(it)')

BS = read_input_1('BS(t)')[0]

RS = read_input_1('RS(ct)')

OS = read_input_1('OS(kt)')

RC = read_input_1('RC(jt)')

BC = read_input_1('BC(kt)')

PC = read_input_1('PC(i)')[0]

Cap = read_input_1('Cap')[0][0]

MaxD = read_input_1('MaxD(it)')

MinD = read_input_1('MinD(it)')

BoxD = read_input_1('BoxD(t)')[0]

RD = read_input_1('RD(ct)')

PV = read_input_1('PV(i)')[0]
BV = read_input_1('BV')[0][0]


a_size = read_range('a_size')[0]
t_size = read_range('t_size')[0]
l_size = read_range('l_size')[0]
r_size = read_range('r_size')[0]
b_size = read_range('b_size')[0]

# parameters
MR = read_input('MR(rl)')
FR = read_input('FR')[0][0]
BR = read_input('BR')[0][0]
DR = read_input('DR')[0][0]


@app.route('/')
def hello_world():

    global model

    reg('COST')
    reg('REVENUE')
    reg('H$1$2', j_size_1, t_size_1)
    reg('V$1$2', k_size_1, t_size_1)
    reg('W$1$2', c_size_1, t_size_1)
    reg('Y$1$2', i_size_1, t_size_1)
    reg('Z$1$2', k_size_1, t_size_1)

    reg('A$1$2', a_size, t_size)
    reg('AH$1', t_size)
    reg('AM$1', t_size)
    reg('AX$1$2', a_size, t_size)
    reg('AY$1$2', a_size, t_size)

    reg('B$1$2', a_size, t_size)
    reg('BZ$1$2', a_size, t_size)
    reg('BX$1$2', a_size, t_size)
    reg('BY$1$2', a_size, t_size)

    reg('C$1$2$3', a_size, t_size, b_size)
    reg('CX$1$2$3', a_size, t_size, b_size)
    reg('CY$1$2$3', a_size, t_size, b_size)

    reg('D$1$2$3$4', a_size, t_size, r_size, l_size)
    reg('DZ$1$2$3$4', a_size, t_size, r_size, l_size)
    reg('DX$1$2$3$4', a_size, t_size, r_size, l_size)
    reg('DY$1$2$3$4', a_size, t_size, r_size, l_size)

    reg('E$1$2$3$4$5', a_size, t_size, b_size, r_size, l_size)
    reg('E$1$2$3$4', a_size, t_size, r_size, l_size)
    reg('EY$1$2$3$4$5', a_size, t_size, b_size, r_size, l_size)

    reg('H,1$1', t_size)

    reg('Herd$1', t_size)
    reg('Cattle$1', t_size)
    reg('mincap')
    reg('maxcap')

    model += d['REVENUE'] - d['COST']

    print('[SUCCESS] register variables')

    read_initial_input()

    print('[SUCCESS] read initial input')

    model.solve(PULP_CBC_CMD(timeLimit=5))
    print('[SUCCESS] solve')

    output = ''
    dynamic_result = 0.0
    print('[PENDING] output')

    for v in model.variables():
        if v.varValue == 0:
            continue

        if v.varValue is None:
            continue

        dynamic_result = dynamic_result + float(str(v.varValue))

        output += '<p style="text-align: center;margin: 0px;">' + \
            v.name + ' = ' + str(v.varValue) + '</p>'

    output += '<p style="text-align: center;margin: 0px;">Dynamic Programming = ' + \
        str(dynamic_result) + '</p>'
    print('[SUCCESS] output')

    return output


if __name__ == "__main__":

    app.run(debug=True)
