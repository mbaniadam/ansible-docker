from flask import Flask, request, jsonify
from datetime import datetime
import psutil


app = Flask(__name__)
@app.route('/', methods=["GET"])
def get_metrics():
    date_time = datetime.now()
    current_time = date_time.strftime("%d-%m-%Y   %H:%M:%S")
    disk_partitions = psutil.disk_partitions()
    disk_info = []
    for partition in disk_partitions:
        partition_info = {
            "p_name" : partition.device,
            "p_total_size": psutil.disk_usage(partition.mountpoint).total,
            "p_free_space": psutil.disk_usage(partition.mountpoint).free
        }
        disk_info.append(partition_info)

    return '''The current date and time is: {}\n
    Disk information:\n{}
    '''.format(current_time,disk_info)


app.run(host='0.0.0.0',port=5000)