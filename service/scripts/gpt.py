import os
import json
import regex as re
import openai
from dotenv import load_dotenv
import logging

load_dotenv()

# Default model and token values
MODEL = os.getenv("MODEL")
MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure the logger
logger = logging.getLogger(__name__)

# Main call_gpt function
def call_gpt(data_object):
    openai.api_key = OPENAI_API_KEY

    prompt_template = read_prompt_template()

    filled_prompt = fill_prompt_template(prompt_template, data_object)
    logger.debug("Filled prompt: " + filled_prompt)

    logger.info("Calling GPT")
    # Try 5 times to get a valid JSON object
    for _ in range(5):
        response = openai.Completion.create(
            engine=MODEL,
            prompt=filled_prompt,
            max_tokens=MAX_TOKENS,
            n=1,
            stop=None,
            temperature=0.0,
        )

        response_text = response.choices[0].text.strip()

        logger.debug("Response text: " + response_text)

        response_json = find_valid_json(response_text)
        if response_json:
            return response_json

    raise ValueError("Data could not be classified by OpenAI GPT 3.5")


def read_prompt_template():
    logger.info("Reading prompt template")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_file_path = os.path.join(script_dir, "prompt.txt")

    with open(prompt_file_path, "r") as f:
        return f.read()


def fill_prompt_template(prompt_template, data_object):
    logger.info("Filling prompt template")

    model = data_object.model
    model_json = json.dumps(model.get('model'))
    model_description_json = json.dumps(model.get('model_description'))
    input = data_object.input
    context = getattr(data_object, 'context', '')

    try:
        prompt_template = prompt_template.replace("{model}", model_json)
        prompt_template = prompt_template.replace("{model_description}", model_description_json)
        prompt_template = prompt_template.replace("{input}", input)
        prompt_template = prompt_template.replace("{context}", context)

    except Exception as e:
        raise e

    return prompt_template


def find_valid_json(response):
    logger.info("Finding valid JSON from GPT response")

    json_pattern = r"\{(?:[^{}]|(?R))*\}"
    json_matches = re.finditer(json_pattern, response)

    for match in json_matches:
        try:
            response_json = json.loads(match.group())
            return response_json
        except json.JSONDecodeError:
            pass

    return None