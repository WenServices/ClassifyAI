import os
import json
from . import gpt
from dotenv import load_dotenv
import logging

load_dotenv()

# Default model and token values
MAX_INPUT_LENGTH = int(os.getenv("MAX_INPUT_LENGTH"))
MAX_CONTEXT_LENGTH = int(os.getenv("MAX_CONTEXT_LENGTH"))

# Configure the logger
logger = logging.getLogger(__name__)

# Main classify function
def classify(data_object):
    validate_data_object(data_object)

    result = gpt.call_gpt(data_object)

    # If data_object has a reference_id, add it to the result
    if hasattr(data_object, 'reference_id'):
        ref_id_name = getattr(data_object, 'reference_id_name', 'reference_id')
        result[ref_id_name] = data_object.reference_id

    return result


# Validation functions
def validate_data_object(data_object):
    logger.info("Validating data object")

    validate_input(data_object)
    validate_model(data_object)

    if hasattr(data_object, 'context'):
        validate_context(data_object.context)

    logger.info("Data object is valid")


def validate_input(data_object):
    logger.info("Validating input")

    input = getattr(data_object, 'input', '')
    if not input:
        raise ValueError("'input' field must be provided and not empty")

    max_input_length = MAX_INPUT_LENGTH
    if max_input_length and len(input) > max_input_length:
        raise ValueError(f"Input length exceeds the maximum allowed length of {max_input_length}")

    logger.info("Input is valid")


def validate_model(data_object):
    logger.info("Validating model")

    model = getattr(data_object, 'model', '')
    if not model:
        raise ValueError("'model' field must be provided and not empty")

    if is_json(model):
        # Log object that's inside the model
        data_object.model = json.loads(model)

        # Check if JSON includes a model object and a model description object
        try:
            if not all(k in data_object.model for k in ('model', 'model_description')):
                raise ValueError("'model' and 'model_description' fields must be provided")

            logger.info("Model object and model description object are valid")
        except Exception as e:
            raise ValueError(f"The specified model JSON file is not valid: {str(e)}")

    else:
        logger.info("Model is a string")

        model_file = os.path.join(os.getcwd(), "models", f"{model}.json")

        # Check if model file exists
        if not os.path.exists(model_file):
            raise ValueError(f"The specified model '{model}' is not configured")

        logger.info(f"Model file: {model_file} exists")

        try:
            with open(model_file, 'r') as f:
                model_object = json.load(f)
        except Exception as e:
            raise ValueError(f"The specified model JSON file '{model_file}' is not valid: {str(e)}")

        data_object.model = model_object

    logger.info("Model is valid")


def validate_context(context):
    logger.info("Validating context")
    max_context_length = MAX_CONTEXT_LENGTH
    if max_context_length and len(context) > max_context_length:
        raise ValueError(f"Context length exceeds the maximum allowed length of {max_context_length}")
    logger.info("Context is valid")


def is_json(value):
    try:
        json.loads(value)
    except ValueError:
        return False
    return True