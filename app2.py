from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return "<h1> This a an example</h1><p>And the examples continues here!</p>"

if __name__ == '__main__':
	app.run()