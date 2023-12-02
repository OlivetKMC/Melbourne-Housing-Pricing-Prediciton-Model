# Melbourne-Housing-Pricing-Prediciton-Model
Developed ML model predicting Melbourne housing prices with features like rooms, bathrooms, land size, car park, and location. Used Decision Tree and improved accuracy with Random Forest. Deployed with Flask, thanks to Kaggle for insights.
# Melbourne Housing Price Prediction

Welcome to the Melbourne Housing Price Prediction project! In this project, I developed a machine learning model to predict housing prices in Melbourne. Leveraging features such as the number of rooms, bathrooms, land size, car park space, building area, and location coordinates (latitude and longitude), I employed Decision Tree Regression for the initial model and later enhanced accuracy using Random Forest Regression.

## Project Overview

- **Data Source:** The dataset used for this project was obtained from Kaggle, providing a rich source of information on Melbourne housing characteristics.

- **Model Construction:**
  - *Decision Tree Regression:* Initially, I constructed the model using Decision Tree Regression.
  - *Hyperparameter Tuning:* The model underwent fine-tuning, and through hyperparameter tuning, I identified that a max leaf nodes value of 500 yielded optimal results.

- **Enhanced Accuracy:**
  - *Random Forest Regression:* To further enhance accuracy, I implemented Random Forest Regression.
  - *Performance Metrics:* The model achieved an R2 score of 73.1%, and scatter plots comparing actual prices with predicted prices demonstrated a suitable fit.

- **Deployment:**
  - *Flask Application:* The model was deployed using Flask, providing a user-friendly interface for predicting housing prices.
  - *HTML and CSS Frontend:* The deployment is complemented by an HTML and CSS frontend, offering an interactive experience for users.

## Project Structure

```plaintext
project-root/
│
├── .gitignore
├── README.md
├── LICENSE
│
├── app.py
├── static/
│   ├── style.css
│   └── ...
├── templates/
│   ├── index.html
│   └── ...
├── venv/  # Add to .gitignore
├── data/
│   ├── melbourne_housing_data.csv
│   └── ...
├── notebooks/
│   ├── data_exploration.ipynb
│   ├── model_building.ipynb
│   └── ...
```

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application:**
   ```bash
   python app.py
   ```

4. **Visit the Local Host:**
   Open your web browser and go to [http://localhost:5000](http://localhost:5000) to use the application.

## Acknowledgments

I extend my gratitude to Kaggle for providing valuable insights throughout the project. This project has been an incredible learning experience, and I hope it serves as a useful resource for anyone interested in Melbourne housing price prediction.

Feel free to explore the code, contribute, and provide feedback! Happy predicting!
