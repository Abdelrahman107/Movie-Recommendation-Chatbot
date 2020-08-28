from rivescript import RiveScript 
from flask import Flask , request , render_template
import requests 
import bot
from function import getMovie


app = Flask(__name__)


@app.route("/")
def index():
    bot.bot.clear_uservars()
    return render_template("index.html")

@app.route("/get")
def chat():
    request_data = request.args.get('msg')
    request_data = request_data.capitalize()
    if request_data == "Drama" or request_data == "Comedy" or request_data == "Romance" or request_data == "Horror" or request_data == "Thriller" or request_data == "Action" or request_data == "Children" or request_data == "Adventure" or request_data == "Animation":
        movieToPrint = getMovie(request_data)
        response = bot.chat(request_data)
        return movieToPrint + "--->" + str(response)
    else:
        response = bot.chat(request_data)
        return str(response)  

if __name__ == "__main__":
    app.run(debug=True)