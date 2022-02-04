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


@app.route('/')
def hello_world():

    global model
    df = data_frame_from_xlsx("input/AHerd.xlsx", "Aherd")
    print(df)
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
