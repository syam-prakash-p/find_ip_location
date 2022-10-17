#!/home/syam/personal/find_ip_location/app/venv/bin/python3
import os
from flask import render_template,Flask,request
import ipaddress
import redis
import json
from os import getenv


import requests

api_url="http://ip-api.com/json/%s"


app = Flask(__name__)

def redis_connect():
    try:
        rc = redis.Redis(host=os.getenv('REDIS_HOST'),port=os.getenv('REDIS_PORT'),db=0)
        rc.ping()
        return rc
    except Exception as e:
        print(e)
        return None
rc = redis_connect()





def get_ip_data(ip):
    try:
        ip_addr=ipaddress.ip_address(ip)
        if ip_addr.is_private:
            return render_template('out.html',result=f"your ip is private: {ip}")
        else:
            if rc:
                result=rc.get(ip)
                if result is None:
                  result=requests.get(api_url%(ip))
                  data=result.json()
                  rc.set(ip,result.text)
                else:
                  data=json.loads(result)
            else:
                result=requests.get(api_url%(ip))
                data=result.json()
            return render_template("result.html",result=data)
    except Exception as e:
        print(e)
        return render_template('out.html',result=e)


@app.route("/",methods =["GET", "POST"])
def home():
    if request.method == "POST":
       ip = request.form.get("ip_addr")
       return get_ip_data(ip)
    return render_template("index.html")

@app.route("/home")
def homeN():
    return "hi"

app.run(host='0.0.0.0',debug=True)
