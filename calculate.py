from time import time
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

customer_range = [1, 3]
product_range = [1, 7]
rawmat_range = [1, 4]
outsource_range = [1, 4]

age1_range = [0, 14]
age2_range = [15, 18]
age3_range = [16, 27]
age4_range = [24, 36]
age5_range = [27, 41]
age6_range = [35, 50]
age7_range = [37, 51]
age8_range = [45, 60]

milking_range = [1, 10]
milkingE_range = [4, 15]
milkingE2_range = [4, 15]
gestation_range = [1, 9]
milking2_range = [1, 10]
milking3_range = [1, 10]

time_range = [1, 36]


def read_initial_data(file_name, column_name, variable_name, ia=[-1, -1], ja=[-1, -1]):

    global model

    df = data_frame_from_xlsx("input/" + file_name, column_name)

    for row_index, row in df.iterrows():
        for column_index, value in enumerate(row):
            if (ia[0] == -1):
                model += d[variable_name] == df[column_index][row_index]
                print("SET " + variable_name + " = " +
                      str(df[column_index][row_index]))
            elif (ja[0] == -1):
                model += d[variable_name + ',' +
                           str(ia[0] + row_index)] == df[column_index][row_index]
                print("SET " + variable_name + ',' +
                      str(ia[0] + row_index) + " = " + str(df[column_index][row_index]))
            else:
                model += d[variable_name + ',' + str(ia[0] + row_index) + ',' + str(
                    ja[0] + column_index)] == df[column_index][row_index]
                print("SET " + variable_name + ',' + str(ia[0] + row_index) + ',' + str(
                    ja[0] + column_index) + " = " + str(df[column_index][row_index]))


@app.route('/')
def hello_world():

    global model

    # df = data_frame_from_xlsx("input/MaxD_MinD.xlsx", "MaxD")
    # for index, row in df.iterrows():
    #     for i, value in enumerate(row):
    #         print(df[i][index])

    reg(d, 'PC$1', product_range)
    reg(d, 'PV$1', product_range)

    reg(d, 'OCap$1', outsource_range)
    reg(d, 'Boxcap$1', outsource_range)

    reg(d, 'AHerd0$1', age1_range)

    reg(d, 'BHerd0$1', age2_range)
    reg(d, 'BHerd1$1', age2_range)
    reg(d, 'BZ0$1', age2_range)
    reg(d, 'BY0$1', age2_range)
    reg(d, 'CB0$1', age2_range)

    reg(d, 'DC0$1', age3_range)

    reg(d, 'ED10$1', age5_range)

    reg(d, 'ED20$1', age7_range)

    reg(d, 'MRD1$1', milking_range)

    reg(d, 'MRE1$1', milkingE_range)

    reg(d, 'MRE2$1', milkingE2_range)

    reg(d, 'MRD2$1', milking2_range)

    reg(d, 'MRD3$1', milking3_range)

    reg(d, 'AH$1', time_range)
    reg(d, 'AM$1', time_range)
    reg(d, 'AM1$1', time_range)
    reg(d, 'AM2$1', time_range)
    reg(d, 'Herd$1', time_range)
    reg(d, 'Cattle$1', time_range)
    reg(d, 'BH$1', time_range)
    reg(d, 'milk$1', time_range)
    reg(d, 'Atotal$1', time_range)
    reg(d, 'BTotal$1', time_range)
    reg(d, 'CTotal$1', time_range)
    reg(d, 'D1Total$1', time_range)
    reg(d, 'E1Total$1', time_range)
    reg(d, 'D2Total$1', time_range)
    reg(d, 'E2Total$1', time_range)
    reg(d, 'D3Total$1', time_range)
    reg(d, 'BoxD$1', time_range)
    reg(d, 'BS$1', time_range)
    reg(d, 'Sale$1', time_range)

    reg(d, 'Y$1$2', time_range, product_range)
    reg(d, 'S$1$2', time_range, product_range)
    reg(d, 'MaxD$1$2', time_range, product_range)
    reg(d, 'MinD$1$2', time_range, product_range)

    reg(d, 'H$1$2', time_range, rawmat_range)
    reg(d, 'RC$1$2', time_range, rawmat_range)

    reg(d, 'W$1$2', time_range, customer_range)
    reg(d, 'RS$1$2', time_range, customer_range)
    reg(d, 'RD$1$2', time_range, customer_range)

    reg(d, 'V$1$2', time_range, outsource_range)
    reg(d, 'Z$1$2', time_range, outsource_range)
    reg(d, 'OS$1$2', time_range, outsource_range)
    reg(d, 'BC$1$2', time_range, outsource_range)

    reg(d, 'AHerd$1$2', age1_range, time_range)
    reg(d, 'AX$1$2', age1_range, time_range)
    reg(d, 'AY$1$2', age1_range, time_range)

    reg(d, 'BHerd$1$2', age2_range, time_range)
    reg(d, 'BX$1$2', age2_range, time_range)
    reg(d, 'BY$1$2', age2_range, time_range)
    reg(d, 'BZ$1$2', age2_range, time_range)
    reg(d, 'BZA$1$2', age2_range, time_range)
    reg(d, 'BZB$1$2', age2_range, time_range)
    reg(d, 'CB$1$2', age2_range, time_range)
    reg(d, 'DAbt$1$2', age2_range, time_range)

    reg(d, 'CHerd$1$2$3', age3_range, time_range, gestation_range)
    reg(d, 'CX$1$2$3', age3_range, time_range, gestation_range)
    reg(d, 'CY$1$2$3', age3_range, time_range, gestation_range)
    reg(d, 'BAbort$1$2$3', age3_range, time_range, gestation_range)

    reg(d, 'D1Herd$1$2$3', age4_range, time_range, milking_range)
    reg(d, 'D1X$1$2$3', age4_range, time_range, milking_range)
    reg(d, 'D1Y$1$2$3', age4_range, time_range, milking_range)
    reg(d, 'D1Z$1$2$3', age4_range, time_range, milking_range)
    reg(d, 'DE1$1$2$3', age4_range, time_range, milking_range)
    reg(d, 'E1Abort$1$2$3', age4_range, time_range, milking_range)

    reg(d, 'E1Herd$1$2$3$4', age5_range,
        time_range, milkingE_range, gestation_range)
    reg(d, 'E1X$1$2$3$4', age5_range, time_range, milkingE_range, gestation_range)
    reg(d, 'E1Y$1$2$3$4', age5_range, time_range, milkingE_range, gestation_range)
    reg(d, 'E1Abt$1$2$3$4', age5_range, time_range,
        milkingE_range, gestation_range)

    reg(d, 'D2Herd$1$2$3', age6_range, time_range, milking2_range)
    reg(d, 'D2X$1$2$3', age6_range, time_range, milking2_range)
    reg(d, 'D2Y$1$2$3', age6_range, time_range, milking2_range)
    reg(d, 'D2Z$1$2$3', age6_range, time_range, milking2_range)
    reg(d, 'DE2$1$2$3', age6_range, time_range, milking2_range)
    reg(d, 'E2Abort$1$2$3', age6_range, time_range, milking2_range)

    reg(d, 'CHerd0$1$2', age3_range, gestation_range)
    reg(d, 'BAbort0$1$2', age3_range, gestation_range)

    reg(d, 'DC$1$2', age3_range, time_range)

    reg(d, 'D1Herd0$1$2', age4_range, milking_range)
    reg(d, 'D1Z0$1$2', age4_range, milking_range)
    reg(d, 'D1Herd1$1$2', age4_range, milking_range)
    reg(d, 'DHerd0total$1$2', age4_range, milking_range)

    reg(d, 'E1Herd0$1$2$3', age5_range, milkingE_range, gestation_range)
    reg(d, 'E1Abt0$1$2$3', age5_range, milkingE_range, gestation_range)

    reg(d, 'D2Herd0$1$2', age6_range, milking2_range)
    reg(d, 'D2Z0$1$2', age6_range, milking2_range)
    reg(d, 'D2Herd1$1$2', age6_range, milking2_range)
    reg(d, 'D2Herd0total$1$2', age6_range, milking2_range)
    reg(d, 'DE20$1$2', age6_range, milking2_range)

    reg(d, 'ED1$1$2', age5_range, time_range)

    reg(d, 'E2Herd$1$2$3$4', age7_range, time_range,
        milkingE2_range, gestation_range)
    reg(d, 'E2X$1$2$3$4', age7_range, time_range,
        milkingE2_range, gestation_range)
    reg(d, 'E2Y$1$2$3$4', age7_range, time_range,
        milkingE2_range, gestation_range)
    reg(d, 'E2Abt$1$2$3$4', age7_range, time_range,
        milkingE2_range, gestation_range)

    reg(d, 'E2Herd0$1$2$3', age7_range, milkingE2_range,
        gestation_range)
    reg(d, 'E2Abt0$1$2$3', age7_range, milkingE2_range,
        gestation_range)

    reg(d, 'ED2$1$2', age7_range, time_range)

    reg(d, 'D3Herd$1$2$3', age8_range, time_range, milking2_range)
    reg(d, 'D3X$1$2$3', age8_range, time_range, milking2_range)
    reg(d, 'D3Y$1$2$3', age8_range, time_range, milking2_range)

    reg(d, 'D3Herd0$1$2', age8_range, milking2_range)
    reg(d, 'D3Herd0total$1$2', age8_range, milking2_range)

    reg(d, 'DEAbt$1$2$3', age5_range, time_range, milkingE_range)
    reg(d, 'E1AbSell$1$2$3', age5_range, time_range, milkingE_range)

    reg(d, 'DE2Abt$1$2$3', age7_range, time_range, milkingE2_range)
    reg(d, 'E2AbSell$1$2$3', age7_range, time_range, milkingE2_range)

    reg(d, 'Cap')
    reg(d, 'BV')

    reg(d, 'BR')
    reg(d, 'FR')
    reg(d, 'DR')
    reg(d, 'BAR')

    read_initial_data('Data_LP.xlsx', 'Cap', 'Cap')
    read_initial_data('Data_LP.xlsx', 'BV', 'BV')
    read_initial_data('MaxD_MinD.xlsx', 'MinD', 'MinD',
                      time_range, product_range)
    read_initial_data('MaxD_MinD.xlsx', 'MaxD', 'MaxD',
                      time_range, product_range)
    read_initial_data('MaxD_MinD.xlsx', 'Sit', 'S',
                      time_range, product_range)
    read_initial_data('MaxD_MinD.xlsx', 'PC', 'PC', product_range)
    read_initial_data('MaxD_MinD.xlsx', 'PV', 'PV', product_range)

    read_initial_data('Box.xlsx', 'BC', 'BC', time_range, outsource_range)
    read_initial_data('Box.xlsx', 'Bs', 'BS', time_range)
    read_initial_data('Box.xlsx', 'BoxD', 'BoxD', time_range)
    read_initial_data('Box.xlsx', 'OS', 'OS', time_range, outsource_range)
    read_initial_data('Box.xlsx', 'OCap', 'OCap', outsource_range)
    read_initial_data('Box.xlsx', 'boxcap', 'Boxcap', outsource_range)

    read_initial_data('Raw Milk_Product.xlsx', 'RD',
                      'RD', time_range, customer_range)
    read_initial_data('Raw Milk_Product.xlsx', 'RS',
                      'RS', time_range, customer_range)

    read_initial_data('Raw Milk_Price.xlsx', 'RC_jt',
                      'RC', time_range, rawmat_range)

    model += d['BR'] == 0.7
    model += d['FR'] == 0.5
    model += d['DR'] == 0.8
    model += d['BAR'] == 0.05

    read_initial_data('AHerd.xlsx', 'Aherd', 'AHerd0', age1_range)
    read_initial_data('BHerd.xlsx', 'Bherd', 'BHerd0', age2_range)
    read_initial_data('CHerd.xlsx', 'CHerd', 'CHerd0',
                      age3_range, gestation_range)
    read_initial_data('DHerd.xlsx', 'DHerd_l1', 'D1Herd0',
                      age4_range, milking_range)
    read_initial_data('DHerd.xlsx', 'DHerd_l2', 'D2Herd0',
                      age6_range, milking2_range)
    read_initial_data('DHerd.xlsx', 'DHerd_l3', 'D3Herd0',
                      age8_range, milking2_range)

    read_initial_data('Milk Yield per lactation.xlsx',
                      'MRD_1', 'MRD1', milking_range)
    read_initial_data('Milk Yield per lactation.xlsx',
                      'MRD_2', 'MRD2', milking2_range)
    read_initial_data('Milk Yield per lactation.xlsx',
                      'MRD_3', 'MRD3', milking3_range)
    read_initial_data('Milk Yield per lactation.xlsx',
                      'MRE_1', 'MRE1', milkingE_range)
    read_initial_data('Milk Yield per lactation.xlsx',
                      'MRE_2', 'MRE2', milkingE2_range)

    for t in full_array_range(time_range):
        model += d['AM,' + str(t)] == d['AM1,' + str(t)] + d['AM2,' + str(t)]

    model.solve(PULP_CBC_CMD(timeLimit=5))

    output = ''

    for v in model.variables():
        # if v.varValue == 0:
        #     continue

        # if v.varValue is None:
        #     continue

        output += '<p style="text-align: center;margin: 0px;">' + \
            v.name + ' = ' + str(v.varValue) + '</p>'
    print('[SUCCESS] output')

    return output
    # reg('COST')
    # print(model)

    # df = data_frame_from_xlsx("input/AHerd.xlsx", "Aherd")
    # print(df)

    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
