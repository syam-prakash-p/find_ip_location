from flask import Flask
from flask import render_template,Flask,request
import ipaddress


import requests

api_url="http://ip-api.com/json/%s"


app = Flask(__name__)

def get_ip_data(ip):
    try:
        ip_addr=ipaddress.ip_address(ip)
        if ip_addr.is_private:
            return f"your ip is private: {ip}"
        else:
            # return f"your ip {ip}"
            result=requests.get(api_url%(ip))
            # return f"{result}"
            return render_template("result.html",result=result.json())
    except Exception as e:
        return f"error {e}"

    # requests.get(api_url % (ip))

@app.route("/",methods =["GET", "POST"])
def home():
    if request.method == "POST":
       ip = request.form.get("ip_addr")
       # return "Your IP address is "+ ip
       return get_ip_data(ip)
    return render_template("index.html")



app.run(debug=True)