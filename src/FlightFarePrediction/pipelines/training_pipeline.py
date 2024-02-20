import os
import sys
from src.FlightFarePrediction.logger import logging
from src.FlightFarePrediction.exception import customexception
import pandas as pd


from src.FlightFarePrediction.components.data_ingestion import DataIngestion
from src.FlightFarePrediction.components.data_transformation import DataTransformation
from src.FlightFarePrediction.components.model_trainer import ModelTrainer
from src.FlightFarePrediction.components.model_evaluation import ModelEvaluation


# Data Ingestion Pipeline
obj = DataIngestion()
train_data_path, test_data_path = obj.initiate_data_ingestion()

# Data Transformation Pipeline
data_transformation = DataTransformation()
train_arr, test_arr = data_transformation.initialize_data_transformation(train_data_path,test_data_path)

# Model Trainer Pipeline
model_trainer_obj = ModelTrainer()
model_trainer_obj.initiate_model_training(train_arr,test_arr)

# Model Evaluation Pipeline
model_eval_obj = ModelEvaluation()
model_eval_obj.initiate_model_evaluation(train_arr,test_arr)