import argparse
import os
import importlib
from utils import run_tests

def discover_test_cases(models):
    test_cases = []
    data_folder = os.path.join(os.path.dirname(__file__), "data")

    for model in models:
        model_file = os.path.join(data_folder, f"{model}.py")
        if os.path.exists(model_file):
            module = importlib.import_module(f"data.{model}")
            test_cases += getattr(module, f"test_cases")
        elif model == "all":
            continue
        else:
            print(f"Model '{model}' not found. Skipping...")

    return test_cases

def main():
    parser = argparse.ArgumentParser(description="Test the ClassifyAI app")
    parser.add_argument(
        "models",
        nargs="*",
        default=["all"],
        help="Specify the model(s) to test or 'all' to test all models (default: all)",
    )

    args = parser.parse_args()

    if "all" in args.models:
        if not input("Are you sure you want to test all models? (y/n): ").lower().startswith("y"):
            print("Aborting.")
            return
        args.models = [os.path.splitext(file)[0] for file in os.listdir("data") if file.endswith(".py")]

    test_cases = discover_test_cases(args.models)
    run_tests(test_cases)

if __name__ == "__main__":
    main()
