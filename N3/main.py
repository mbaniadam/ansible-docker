from flask import Flask, request, jsonify
from datetime import datetime
import linux_metrics 
import subprocess

app = Flask(__name__)
@app.route('/', methods=["GET"])
def get_metrics():
    date_time = datetime.now()
    current_time = date_time.strftime("%d-%m-%Y   %H:%M:%S")
    res_ls_disk = jsonify(subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE).communicate())[0]

    return '''The current date and time is: {}'''.format(current_time,res_ls_disk)

app.run(host='0.0.0.0',port=5000)