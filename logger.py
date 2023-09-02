import logging

def configure_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(f'{logger_name}.log')
    file_handler.setLevel(logging.DEBUG)  # שנה את הרמה ל-DEBUG או INFO כרצונך

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
