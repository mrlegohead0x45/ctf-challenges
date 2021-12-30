import flask
import base64

app = flask.Flask(__name__)

@app.route("/")
def index():
	data = flask.request.args.get("data") 

	if data is None:
		with open("image.jpg.b64", "r") as file:	
			return flask.render_template("index.html", image=file.read())

	
app.run("0.0.0.0", 8000)
