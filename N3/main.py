from flask import Flask, request, jsonify
import subprocess
from datetime import datetime


app = Flask(__name__)
@app.route('/', methods=["GET"])
def get_metrics():
    date_time = datetime.now()
    current_time = date_time.strftime("%d-%m-%Y   %H:%M:%S")
    return '''The current date and time is: {}'''.format(current_time)


app.run()