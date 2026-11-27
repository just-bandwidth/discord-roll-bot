import os
import threading

from flask import Flask

import bot as bot_module

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/")
def root():
    return "Bot is running", 200

def start_bot():
    token = os.environ["DISCORD_TOKEN"]
    bot_module.bot.run(token)

if __name__ == "__main__":
    t = threading.Thread(target=start_bot, daemon=True)
    t.start()

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
