from flask import Flask, request
from datetime import datetime
import linux_metrics 
import subprocess
import json


def run_shell_command(command):
    result = subprocess.run(command, capture_output=True)
    return result.stdout


app = Flask(__name__)
@app.route('/', methods=["GET"])
def get_metrics():
    date_time = datetime.now()
    current_time = date_time.strftime("%d-%m-%Y   %H:%M:%S")
    #sub_result = subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE).communicate()[0]
    sub_result = run_shell_command("df -h")
    js_result = json.loads(sub_result)
    return '''The current date and time is: {}
    df -h output:\n
    {}'''.format(current_time,js_result)

app.run(host='0.0.0.0',port=5000)