from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def dummy_api():
    return jsonify({'Movie':'Avengers',
                    'ID':'1'},{'id':2, 'name':'Transformer'})


if __name__ =="__main__":
    app.run()

