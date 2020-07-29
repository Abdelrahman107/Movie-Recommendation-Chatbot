from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()


def chat(message):
    if message == "":
        return  "No message found "
    else:
        response = bot.reply("localuser", message)
    if response:
        return  response
    else:
        return "let's stick to our objective"

