from quart import Quart, render_template, url_for, send_file, Request
import sys, json, aiohttp

try:
    config = json.load(open("config.json"))
except:
    print("make a config.json dum dum")
    sys.exit(0)

host = config.get("host") if config.get("host") else "127.0.0.1"
port = config.get("port") if config.get("port") else 5000
SERVER_NAME = config.get("domain_name") if config.get("domain_name") else host + ':' + str(port)
app = Quart(__name__)
app.config['SERVER_NAME'] = SERVER_NAME
using_ip = host in SERVER_NAME

#log = logging.getLogger('werkzeug')
#log.disabled = True



async def get_avy(id):
    bot_token = config.get("bot_token")
    if not bot_token:
        raise Exception("Config file missing 'bot_token'.")
    async with aiohttp.ClientSession(headers={"Authorization": f"Bot {bot_token}"}) as req:
        async with req.get(f"https://discord.com/api/users/{id}") as res:
            res.raise_for_status()
            data = await res.json()
            return f"https://images.discordapp.net/avatars/{id}/{data['avatar']}.png?size=512"

async def get_supporters():
    sponsors = list()
    async with aiohttp.ClientSession() as req:
        async with req.get("https://sponsors.trnck.dev/skullbite/sponsors") as res:
            res.raise_for_status()
            data = await res.json()
    for x in data["sponsors"]:
        sponsors.append(f"""<div class="smaller-info-box">
            <img draggable="false" src="{x["avatar"]}" />
            <div class="info-text">
                <p><b><i style="margin-right:50px;color:#b805af;">{x["handle"]}</i></span></b></p>
            </div>
        </div>""")
    return "\n".join(sponsors)
    

@app.errorhandler(404)
async def not_found(e):
    return render_template("warning.html", error="404", message="Seems like you got somewhere you shouldn't be... maybe you should <span><a href='/'>Go Home</a></span>.")

#@app.after_request
#async def after_request_func(r):
#    print(f"{r.environ['HTTP_X_FORWARDED_FOR']} - {r.full_path}")
#    return r

@app.route("/favicon.ico")
async def favicon():
    return await send_file("static/assets/favicon.ico")
    
@app.route("/")
async def index():
    return await render_template("index.html", avy=await get_avy(158750488563679232))

@app.route("/assets/<f>")
async def assets(f):
    return await send_file(f"static/assets/{f}.png")

@app.route("/projects")
async def projects():
    return await render_template("projects.html")

@app.route("/info")
async def info():
    return await render_template("info.html")

@app.route("/fundme")
async def supporters():
    return await render_template("funding.html")

@app.route("/desksword")
async def desksword():
    return await render_template("redirect.html", link="https://discord.gg/Wr3TF3sMg5", desc="join my corded disc pls")

if __name__ == '__main__':
    print("Don't run this file. Run 'wsgi.py' instead.")