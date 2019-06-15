from collections import namedtuple
import subprocess
import psutil

from flask import Flask, render_template, request, redirect, url_for, json


app = Flask(__name__)

Message = namedtuple('Message', 'input_command')
messages = []
ppid = []


@app.route("/", methods=['GET'])
def main():
    return render_template('index.html', messages=messages)


def run_command(string):
    args = string.split(" ")
    if len(args) > 0:
        if args[0] == "cls" or args[0] == "clear":
            messages.clear()
            return redirect(url_for("main"))
        process = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
        ppid.append(process.pid)
        print('run ' + str(process.pid))
        data = process.communicate()
        return data[0].decode("cp866")


def kill_process(pid):
    ppidd = pid
    if ppidd:
        try:
            p = psutil.Process(ppidd)
            p.terminate()
            p.kill()
            print('kill ' + str(pid))
        except psutil.NoSuchProcess:
            print('oops loose process')


@app.route("/add_message", methods=['POST'])
def add_message():
    command = request.form['input_command']
    result = run_command(command)
    messages.append(Message(">>> $ " + command))
    messages.append(Message(result))
    #return redirect(url_for("main"))
    return json.dumps({'mess': result, 'com': ">>> $ " + command})


@app.route("/interrupt", methods=['POST'])
def interrupt():
    kill_process(ppid[-1])
    return redirect(url_for("main"))


if __name__ == "__main__":
    app.run(debug=True)
