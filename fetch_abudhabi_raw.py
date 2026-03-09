import json
import requests

DATASET_ID = "3498df63-7edb-4bb6-a0d4-c0d7ba9d126a"
BASE_URL = "https://data.abudhabi/opendata/api/1/metastore/schemas/dataset/items"
OUTPUT_FILE = "knowledge/abudhabi_dataset_meta.json"


def fetch_dataset_meta():
    url = f"{BASE_URL}/{DATASET_ID}"

    print("Requesting dataset metadata from:")
    print(url)

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Done. Metadata saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    fetch_dataset_meta()