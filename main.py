import json

from fetcher import FetchWeatherData
from mylogger import MyLogger
from csv_writer import save_to_csv

logger = MyLogger()

def validate_latitude_logitude(latitude,longitude):
    if (-90 <= latitude <= 90) and (-180 <= longitude <= 180):
        return True
    
        
    print("-------------------------------------------------------------------------")
    print("Enter the valid value of latitude(-90 to +90) and longitude(-180 to +180).")
    print("-------------------------------------------------------------------------")
    return False
    
def weather_data_cleaner(data):
    weather_info = data["current"]
    weather_info.update({"latitude":data["latitude"],"longitude":data["longitude"]})
    return weather_info

def main():
    
    while True:
        latitude = float(input("Enter the value of latitude: "))
        longitude = float(input("Enter the value of longitude: "))
        if validate_latitude_logitude(latitude,longitude) is True:
            break

    data = FetchWeatherData(latitude,longitude)
    cleaned_weather_data = weather_data_cleaner(data)
    save_to_csv(data=cleaned_weather_data)
    print("-------------------------------------------------------------------------------------------------------")
    logger.info(cleaned_weather_data)
    print("-------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()