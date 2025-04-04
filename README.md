# ML in Practice

![image](https://github.com/user-attachments/assets/6b478ed0-6257-43c2-9c3a-e0f760431fd7)



## Project Overview
This repository provides a practical implementation of a Machine Learning pipeline using the Titanic dataset. It includes data preprocessing, model training, evaluation, and a simple deployment using Streamlit for real-time predictions.

## Installation
To set up the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/mhemaly/ML-in-Practice.git
cd ML-in-Practice

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'

# Install dependencies
pip install -r requirements.txt
or
pip install streamlit pandas scikit-learn joblib
```

## Usage
Run the Streamlit application with the following command:

```bash
python main.py
```

This will launch a web interface where users can input passenger details and receive a survival prediction.

## Project Structure
```

ML_in_practice/
├── Notebooks/                                            # Jupyter notebooks for data analysis and model development
│   ├── Titanic ML Model Pipline v1_user inpus.ipynb      # Notebook for initial pipeline
│   ├── Titanic ML Model Pipline v2_Streamlit.ipynb       # Notebook for initial pipeline with advanced deployment
│
├── __pycache__/                                          # Compiled Python files
│   ├── utils.cpython-38.pyc                              # Compiled utils.py
│   └── model.cpython-38.pyc                              # Compiled model.py
│
├── model/                                                # Directory containing trained model files
│   ├── titanic_model.pkl                                 # Trained machine learning model
│   └── scaler.pkl                                        # Scaler for feature normalization
│
├── src/                                                  # Source code for data processing and model training
│   ├── __init__.py                                       # Initialization file for src package
│   ├── utils.py                                          # Code for data cleaning and preprocessing
│
├── README.md                                             # Project documentation
├── main.py                                               # Streamlit application for user interaction
└── requirements.txt                                      # List of required packages


```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contact
For any questions or suggestions, please open an issue on the repository or reach out to [eng.mhemaly@gmail.com].

