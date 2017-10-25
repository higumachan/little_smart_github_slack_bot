from github_webhook import Webhook
from flask import Flask

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app)


@webhook.hook()
def on_push(data):
    print("Got push with: {0}".format(data))

if __name__ == '__main__':
    app.run()
