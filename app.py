import threading
import os

from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/")
def root():
    return "Listening", 200

def run_bot():
    import bot  # noqa: F401 – this triggers bot.py's __main__ indirectly
    # Actually, we'll import cleanly:
    from bot import bot
    token = os.environ["DISCORD_TOKEN"]
    bot.run(token)

# Start the bot in a background thread
bot_thread = threading.Thread(target=run_bot, daemon=True)
bot_thread.start()

# Run the Flask health server on the port Render assigns
port = int(os.environ.get("PORT", 8080))
app.run(host="0.0.0.0", port=port)
