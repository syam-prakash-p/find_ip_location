from flask import render_template,Flask,request
import ipaddress


import requests

api_url="http://ip-api.com/json/%s"


app = Flask(__name__)

def get_ip_data(ip):
    try:
        ip_addr=ipaddress.ip_address(ip)
        if ip_addr.is_private:
            return render_template('out.html',result=f"your ip is private: {ip}")
        else:
            result=requests.get(api_url%(ip))
            return render_template("result.html",result=result.json())
    except Exception as e:
        return render_template('out.html',result=e)


@app.route("/",methods =["GET", "POST"])
def home():
    if request.method == "POST":
       ip = request.form.get("ip_addr")
       return get_ip_data(ip)
    return render_template("index.html")



app.run(host='0.0.0.0',debug=True)