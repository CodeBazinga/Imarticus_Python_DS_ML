from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    sep_len = float(request.form['sepal_length'])
    sep_wid = float(request.form['sepal_width'])
    pet_len = float(request.form['petal_length'])
    pet_wid = float(request.form['petal_width'])
    ypred = model.predict([[sep_len, sep_wid, pet_len, pet_wid]])[0]
    # output = ypred[0]
    return render_template('index.html', prediction_text=ypred)

if __name__ == "__main__":
    app.run()