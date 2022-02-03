from pyrogram import Client, filters
from datetime import datetime


# Read the necessary data from txt files
api_id = open('config/api_id.txt', 'r').read()
api_hash = open('config/api_hash.txt', 'r').read()
from_channel = open('config/from_channel.txt', 'r').read()
to_channel = open('config/to_channel.txt', 'r').read()
session = open('config/account_name.txt', 'r').read()

# P.S. The session name is set in order not to enter the phone number, SMS, password every time
app = Client(
    session,
    api_id=api_id,
    api_hash=api_hash
)

# If a new post on donnore channel, we publish to the desired channel
@app.on_message(filters.chat(from_channel))
def new_post(client, message):
    if message.text != None:
        app.send_message(to_channel, message.text)
        print("New post published!", datetime.now().strftime("%H:%m"))


if __name__ == '__main__':
    app.run()