import sys
from flask import Flask
from utility.log_handler import Logger
import traceback
from controller.controller import controller, settings

# Define app
app = Flask(__name__, template_folder="templates")

# Creating blueprint
app.register_blueprint(controller, url_prefix="")

# Logger object
logger = Logger.setup_logger()

if __name__ == "__main__":
    try:
        # Run the Flask app
        app.run(
            debug=settings['application']['debug'], 
            host=settings['application']['host'], 
            port=settings['application']['port']
        )
    except Exception as e:
        # Log any runtime errors
        logger.debug(f"Exception occurred while running the app: {traceback.format_exc()}")
