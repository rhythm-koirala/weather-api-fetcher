import csv
from mylogger import MyLogger

logger = MyLogger()

def save_to_csv(data: dict):
    logger.info("Attempt to save data at weather_data.csv...")
    with open ("weather_data.csv","a",newline="") as file:
        fields_name = data.keys()
        writer = csv.DictWriter(file, fieldnames=fields_name)
        if file.tell() == 0:
            logger.info("Writing header on weather_data.csv...")
            writer.writeheader()
        logger.info("Writing data on weather_data.csv...")
        writer.writerow(data)
        logger.info("Data sucessfully written at weather_data.csv")
