import argparse
import os
import requests
import sys

import dotenv


dotenv.load_dotenv()

SAM_API_KEY = os.getenv("SAM_API_KEY")
SAM_ENDPOINT = "https://api.data.gov/sam/v1/registrations/"


def query_sam_api(query: str) -> list[dict]:
    url = f"{SAM_ENDPOINT}?api_key={SAM_API_KEY}?qterms={query}"
    response = requests.get(url)
    return response.json()


def main() -> int:
    parser = _config_parser()
    _ = parser.parse_args()

    return 0


def _config_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sam-parser")
    return parser


if __name__ == "__main__":
    sys.exit(main())
