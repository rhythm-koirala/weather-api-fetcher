import logging 
from logging.handlers import RotatingFileHandler

def MyLogger():


    logger = logging.getLogger()
    
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        file_handler = RotatingFileHandler(
            filename= "app.log",
            mode="a",
            maxBytes= 1024*1024*10,
            backupCount=4
    )
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            " %(asctime)s || %(levelname)s || %(message)s || %(filename)s || %(lineno)d"
    )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger