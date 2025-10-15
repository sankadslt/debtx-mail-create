"""
Test script to demonstrate logging usage
- Debug logs go to logs/debug.log
- JSON logs go to logs/json_logs.json
"""

from utils.logger import SingletonLogger

# Configure logger (only needed once at application startup)
SingletonLogger.configure()

# Get the loggers
logger = SingletonLogger.get_logger()  # Root logger for debug logs
json_logger = SingletonLogger.get_logger('jsonLogger')  # JSON logger

if __name__ == "__main__":
    print("Testing logging...")
    print("Check logs/debug.log for debug messages")
    print("Check logs/json_logs.json for JSON formatted logs\n")
    
    # Debug logs go to debug.log (all levels)
    logger.debug("Debug message for developers")
    logger.info("Info message to debug.log")
    logger.warning("Warning in debug.log")
    logger.error("Error in debug.log")
    
    print("Debug logs written to logs/debug.log\n")
    
    # JSON logs go to json_logs.json (INFO and above)
    json_logger.info("Info message")
    json_logger.warning("Warning message")
    json_logger.error("Error message")
    json_logger.critical("Critical message")
    json_logger.fatal("Fatal message")
    
    print("JSON logs written to logs/json_logs.json")
    print("\nLogging test complete!")
