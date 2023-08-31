from flask import Flask, request, jsonify
from datetime import datetime
import psutil


app = Flask(__name__)
@app.route('/', methods=["GET"])
def get_metrics():
    date_time = datetime.now()
    current_time = date_time.strftime("%d-%m-%Y   %H:%M:%S")
    d_partitions = psutil.disk_partitions()
    for partition in d_partitions:
        print(partition)
        partition_info = {}

    


    return '''The current date and time is: {}\n
    Disk info:\n{}\n
    '''.format(current_time,d_partitions)


app.run(host='0.0.0.0',port=5000)