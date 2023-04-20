import json
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from . import logic
import logging
from types import SimpleNamespace

load_dotenv()

app = Flask(__name__)

# Define the mapping of environment variable values to logging levels
LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

# Get the logging level from the environment variable
log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=LOG_LEVELS.get(log_level, logging.INFO))
logger = logging.getLogger(__name__)

logger.info("Starting up the API")

@app.route("/classify", methods=["POST"])
def classify():
    logger.info("Classify request received")

    data_dict = request.get_json()
    if isinstance(data_dict.get('model'), dict):
        data_dict['model'] = json.dumps(data_dict['model'])

    data_object = SimpleNamespace(**data_dict)

    try:
        result = logic.classify(data_object)
    except ValueError as e:
        response = jsonify({"error": str(e)})
        response.status_code = 400
        return response
    except Exception as e:
        response = jsonify({"error": f"Unexpected error: {str(e)}"})
        response.status_code = 500
        return response

    return jsonify(result)