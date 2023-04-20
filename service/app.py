from scripts.api import app
import os

# Check if all required environment variables are set
required_env_vars = ["OPENAI_API_KEY", "MAX_INPUT_LENGTH", "MAX_CONTEXT_LENGTH"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"The following environment variables are required but not set: {', '.join(missing_vars)}")

# Set app configuration from environment variables
app.config.update({
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
    "MAX_INPUT_LENGTH": int(os.getenv("MAX_INPUT_LENGTH")),
    "MAX_CONTEXT_LENGTH": int(os.getenv("MAX_CONTEXT_LENGTH"))
})

# Start the Flask app
if __name__ == '__main__':
    # Read the port number from the .env file
    port = int(os.getenv('PORT', 5000))
    # Run the Flask app using the port number from the .env file
    app.run(host='127.0.0.1', port=port)