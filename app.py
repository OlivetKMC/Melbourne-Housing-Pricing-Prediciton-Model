from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Loading the Random Forest Regressor model using pickle
with open('venv/melbourne housing pricing prediction model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # To Retrieve input features from the form
        features = [float(request.form[f]) for f in ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude', 'Car', 'BuildingArea']]

        # Convert the input features to a NumPy array
        input_features = np.array([features])

        # Make prediction using the model
        prediction = model.predict(input_features)

        # Display the prediction on the page
        return render_template('index.html', prediction=f'{float(prediction):,.2f}')

    #Initial rendering
    return render_template('index.html', prediction='No prediction yet')


if __name__ == '__main__':
    app.run(debug=True)
