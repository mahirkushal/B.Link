from datetime import datetime

from flask import Flask, request, jsonify, render_template

TaskB = Flask(__name__)


@TaskB.route('/')
def home():
    return render_template('index.html')


@TaskB.route("/time_difference", methods=['POST'])
def time_difference():
    t_delta = '%a %d %b %Y %H:%M:%S %z'
    list = [ datetime.strptime(x,t_delta) for x in request.form.values()]
    #t1 = datetime.strptime(request.form.values(), t_delta)
    #t2 = datetime.strptime(request.form.values(), t_delta)
    diff = str(int(abs((list[0] - list[1]).total_seconds())))
    return render_template('index.html', difference=diff)
    # return jsonify({'T_Diff': t_diff})


if __name__ == "__main__":
    TaskB.run(debug=True, port=5000)
