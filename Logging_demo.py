import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A' , level=logging.DEBUG ,filename="test2.log",filemode="w")
logging.critical("This is a critical message")
logging.error("This is an error message")
logging.warning("This is an warning message")
logging.info("This is an Info message")
logging.debug("This is a debug message")



