import logzero
from logzero import logger

# Setup rotating logfile with 3 rotations, each with a maximum filesize of 1MB:
"""was 1e6, not just 90"""
logzero.logfile("tmp\\rotating-logfile.log", maxBytes=10000, backupCount=3)    

# Log messages
for n in range(12):
    #logger.setLevel("DEBUG")
    logger.debug(f"Number {n} This log message goes to the console and the logfile")
    logger.info(f"Number {n} This log message goes to the console and the logfile")
    logger.warn(f"Number {n} This log message goes to the console and the logfile")
    logger.error(f"Number {n} This log message goes to the console and the logfile")
    # logger.exception(f"Number {n} This log message goes to the console and the logfile")