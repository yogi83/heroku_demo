from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():
    return "<hi> this is flask application </hi>"
if __name__ == "__main__":
    app.run()
