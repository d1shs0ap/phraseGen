from flask import Flask, request, jsonify, render_template
import predictor

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        req = request.form['input']
        res = predictor.predict(req)
        return render_template('submit.html', res=res)
    else:
        return render_template('submit.html')


if __name__ == "__main__":
    app.run()
