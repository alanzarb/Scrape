import logzero
from logzero import logger

# Setup rotating logfile with 3 rotations, each with a maximum filesize of 1MB:
"""was 1e6, not just 90"""
logzero.logfile("tmp\\rotating-logfile.log", maxBytes=10000, backupCount=3)

# Log messages
for n in range(1):
    #logger.setLevel("DEBUG")
    logger.debug(
        f"This log message goes to the console and the logfile")
    logger.info(
        f"This log message goes to the console and the logfile")
    logger.warning(
        f"This log message goes to the console and the logfile")
    logger.error(
        f"This log message goes to the console and the logfile")
    # logger.exception(f"This log message goes to the console and the logfile")