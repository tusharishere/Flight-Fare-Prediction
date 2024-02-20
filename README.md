# Flight Fare Prediction

## Objective

## Dataset

## Machine Learning Pipeline

## Artifacts

#### Preprocessings steps

#### Algorithms used to find best model
1. LinearRegression
2. Lasso
3. Ridge        
4. DecisionTreeRegressor  
5. RandomForestRegressor
6. GradientBoostingRegressor 
7. XGBoostRegressor 
8. AdaBoostRegressor
9. BaggingRegressor

## Final Result

## Deployed URLs

## Project Artifacts

## MLOps

## License
This project is licensed under the Apache-2.0  License.

## Setting up the dev environment
```bash
# Create conda environment 'venv'
conda create -p ./venv python=3.9 -y

# Activate the environment
conda activate .\venv

# Upgrade pip and install required packages
python -m pip install --upgrade pip
pip install -r requirements.txt

# Install project  as package
python setup.py install