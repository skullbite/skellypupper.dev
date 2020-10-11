from flask import Flask, render_template, url_for, send_file, Request
import sys, json, requests

try:
    config = json.load(open("config.json"))
except:
    print("make a config.json dum dum")
    sys.exit(0)

host = config.get("host") if config.get("host") else "127.0.0.1"
port = config.get("port") if config.get("port") else 5000
SERVER_NAME = (config.get("domain_name") if config.get("domain_name") else host) + ':' + str(port)
app = Flask(__name__)
app.config['SERVER_NAME'] = SERVER_NAME
using_ip = host in SERVER_NAME

#log = logging.getLogger('werkzeug')
#log.disabled = True



def get_avy(id):
    bot_token = config.get("bot_token")
    if not bot_token:
        raise Exception("Config file missing 'bot_token'.")
    req = requests.get(f"https://discord.com/api/users/{id}", headers={"Authorization": f"Bot {bot_token}"})
    if req.status_code != 200:
        raise Exception(req.status_code) # TODO: replace with static image.
    return f"https://images.discordapp.net/avatars/{id}/{req.json()['avatar']}.png?size=512"

@app.errorhandler(404)
def not_found(e):
    return render_template("warning.html", error="404", message="Seems like you got somewhere you shouldn't be... maybe you should <span><a href='/'>Go Home</a></span>.")

#@app.after_request
#def after_request_func(r: Request):
#    print(f"{r.method}: {r.environ['HTTP_X_FORWARDED_FOR']} - {r.full_path}")
#    return r

@app.route("/")
def index():
    return render_template("index.html", avy=get_avy(158750488563679232))

@app.route("/assets/<f>")
def assets(f):
    return send_file(f"static/assets/{f}.png")

@app.route("/stall")
def stall():
    return render_template("warning.html", error="Stalled!", message="oops... Looks like you hit a part of the site that isn't ready yet.<br>Check back later!")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/desksword")
def desksword():
    return render_template("redirect.html", link="https://discord.gg/c4vWDdd", desc="join my corded disc pls")

if __name__ == '__main__':
    print("Don't run this file. Run 'wsgi.py' instead.")