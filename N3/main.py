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
    
    machine_memory = psutil.virtual_memory()
    ram_info = {
        "ram_total" = machine_memory.total,
        "ram_available" = machine_memory.available,
        "ram_free" = machine_memory.free
    }
    
    cpu_info = {
        "cpu_last" = psutil.cpu_percent(interval=None),
        "cpu_avg" =  psutil.getloadavg()
    }

    js_disk_info = jsonify(disk_info)
    js_ram_info = jsonify(ram_info)
    js_cpu_info = jsonify(cpu_info)



    return '''The current date and time is: {}\n
    Disk information:\n{}\n
    Memory information:\n{}\n
    CPU information:\n{}\n
    '''.format(current_time,js_disk_info,js_ram_info,js_cpu_info)


app.run(host='0.0.0.0',port=5000)