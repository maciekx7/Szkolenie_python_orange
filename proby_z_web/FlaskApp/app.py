from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def main():
    return "No siema"

if __name__ == "__main__":
    app.run()


def get_Vv():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    # code that uses the data you've got
    # in our case, checking if the user exists
    # and logs them in, if not redirect to sign up
    else:
# an exception
