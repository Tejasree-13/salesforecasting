from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the regression model
with open('model_fi.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route("/")
def f():
    return render_template("index.html")

@app.route("/inspect")
def inspect():
    return render_template("inspect.html")

@app.route("/output", methods=["GET", "POST"])
def output():
    if request.method == 'POST':
        # Extract the form data
        var1 = request.form["GENDER"]
        var2 = float(request.form["AGE"])  # Convert to float if necessary
        var3 = request.form["Cateogry"]
        var4 = float(request.form["Quantity"])  # Convert to float if necessary
        var5 = float(request.form["Price"])  # Convert to float if necessary
        var6 = request.form["Payment_Method"]
        var7 = request.form["Shopping_Mall"]

        # Convert the input data into a numpy array
        predict_data = np.array([[var1, var2, var3, var4, var5, var6, var7]])  # Reshape into 2D array

        # Use the loaded model to make predictions
        predict = model.predict(predict_data)

        # Assuming 'predict' is the output of your prediction
        # You might want to format the prediction result before passing it to the template
        predict = round(float(predict[0]), 2)  # Convert to float, round to 2 decimal places

        return render_template("output.html", predict=predict)

if __name__ == "__main__":
    app.run(debug=False)
