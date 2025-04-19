# FarmEazy

The **FarmEazy** is a web-based and Android-compatible application designed to assist farmers in predicting the most suitable crops for cultivation based on current weather and soil conditions. By leveraging **Node.js** for both the front end and backend, and **Python (scikit-learn)** for machine learning processing, the system integrates data from multiple sources to provide accurate crop predictions.

## Features

- **Crop Prediction**: Uses **Multiple Linear Regression (MLR)** to predict the most producible crops based on environmental conditions.
- **Data Integration**: Combines data from official datasets, weather departments, and soil repositories.
- **User-Friendly Interface**: Accessible via a web interface and Android application.
- **Dynamic Routing**: Serves HTML, CSS, JavaScript, and image files dynamically using Node.js.
- **Machine Learning Backend**: Processes data using Python's scikit-learn library for prediction analysis.

## Project Flow

1. The user accesses the website at `http://localhost:8900`.
2. They manually select their location to feed into the regression model.
3. The system processes the input, and the user waits for a short time.
4. The application displays the crops that can be planted now, along with their corresponding images.

## Project Structure
```bash
FarmEazy/
├── code/
│ ├── mlr_algo.py # Python script for crop prediction using MLR
│ ├── test.py # Python script for testing
│ ├── metacrops.csv # Dataset for crop analysis
│ └── code/ # Additional datasets
├── public/
│ ├── index.html # Home page
│ ├── company.html # About the system
│ ├── contact.html # Contact page
│ ├── css/ # Stylesheets
│ ├── js/ # JavaScript files
│ ├── crops/ # Crop images
│ └── images/ # Other images
├── server.js # Node.js server
├── package.json # Node.js dependencies
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .vscode/ # VS Code settings
```
## Prerequisites

1. **Node.js**: Install Node.js from [Node.js Official Website](https://nodejs.org/).
2. **Python**: Install Python (3.x) from [Python Official Website](https://www.python.org/).
3. **Virtual Environment**: Set up a Python virtual environment.
4. **Dependencies**:
   - Install Node.js dependencies using `npm install`.
   - Install Python dependencies using `pip install -r requirements.txt`.

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Atharv-A2/FarmEazy.git
   cd FarmEazy
   ```

2. **Activate Virtual Environment**:

   ```bash
   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Start the Project**:

   ```bash
   node server.js
   ```

4. **Access the Application**:
   Open your browser and navigate to `http://localhost:8900` to access the web interface.
