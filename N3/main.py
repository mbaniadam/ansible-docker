from flask import Flask, request, jsonify
from datetime import datetime
import linux_metrics 
import subprocess
import json


app = Flask(__name__)
@app.route('/', methods=["GET"])
def get_metrics():
    date_time = datetime.now()
    current_time = date_time.strftime("%d-%m-%Y   %H:%M:%S")
    sub_result = subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE).communicate()[0]
    js_result = json.loads(sub_result)
    return '''The current date and time is: {}
    df -h output:\n
    {}'''.format(current_time,js_result)


@app.route('/list', methods=["GET"])
def execute_command():
    try:
        command = "df -h"
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if result.returncode == 0:
            output = result.stdout
        else:
            output = result.stderr
    except Exception as e:
        return jsonify({"error": str(e)})
    
    return jsonify({"output": output})


app.run(host='0.0.0.0',port=5000)