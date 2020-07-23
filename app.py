from rivescript import RiveScript
#from flask import Flask , request
import requests
global response


#app = Flask(__name__)




bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()




while True:
    msg = input('You> ')
    if msg == 'quit':
        quit()

    reply = bot.reply("localuser", msg)
    print('Bot>', reply)





if __name__ == "__main__":
    app.run(debug=True)
    