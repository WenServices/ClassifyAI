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

class APIError(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify({"error": error.message})
    response.status_code = error.status_code
    return response

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
        raise APIError(str(e), 400)
    except Exception as e:
        raise APIError(f"Unexpected error: {str(e)}", 500)

    return jsonify(result)

# ...

@app.route("/models", methods=["GET"])
def get_all_models():
    logger.info("Get all models request received")
    try:
        model_names = logic.get_all_models()
    except Exception as e:
        raise APIError(f"Unexpected error: {str(e)}", 500)

    return jsonify(model_names)

@app.route("/models/<model_name>", methods=["GET"])
def get_model(model_name):
    logger.info(f"Get model '{model_name}' request received")
    try:
        model_content = logic.get_model(model_name)
    except FileNotFoundError as e:
        raise APIError(str(e), 404)
    except Exception as e:
        raise APIError(f"Unexpected error: {str(e)}", 500)

    return jsonify(model_content)

@app.route("/models/<model_name>", methods=["POST"])
def create_model(model_name):
    logger.info(f"Create model '{model_name}' request received")
    try:
        model_content = request.get_json()
        logic.create_or_update_model(model_name, model_content)
    except ValueError as e:
        raise APIError(str(e), 400)
    except Exception as e:
        raise APIError(f"Unexpected error: {str(e)}", 500)

    return jsonify({"message": f"Model '{model_name}' created or modified successfully."})

@app.route("/models/<model_name>", methods=["DELETE"])
def delete_model(model_name):
    logger.info(f"Delete model '{model_name}' request received")
    try:
        logic.delete_model(model_name)
    except FileNotFoundError as e:
        raise APIError(str(e), 404)
    except Exception as e:
        raise APIError(f"Unexpected error: {str(e)}", 500)

    return jsonify({"message": f"Model '{model_name}' deleted successfully."})
