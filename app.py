import flask
import base64
import pickle
import traceback

app = flask.Flask(__name__)

@app.route("/")
def index():
	data = flask.request.args.get("data")

	if data is None:
		with open("image.jpg.b64", "r") as file:
			image = file.read()
		
		return flask.render_template("index.html", image=image)

	decoded = base64.urlsafe_b64decode(data)
	unpickled = pickle.loads(decoded)

	return flask.render_template("index.html", image=unpickled)

	
app.run("0.0.0.0", 8000)
