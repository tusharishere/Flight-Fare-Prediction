from src.FlightFarePrediction.pipelines.prediction_pipeline import CustomData

# Create a CustomData instance with correct parameters
custdata = CustomData(
    Airline="IndiGo",
    Source="Banglore",
    Destination="New Delhi",
    Journey_Day=24,
    Journey_Month=3,
    Journey_Weekday="Sunday", 
    Departure_Part_of_Day="Night",
    Arrival_Part_of_Day="Early Morning",
    Duration_Hour=2,
    Duration_Min=50,
    Total_Stops="non-stop"
)

# Get data as a DataFrame
data = custdata.get_data_as_dataframe()
print(data)