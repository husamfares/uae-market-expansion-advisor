import json

DUBAI_FILE = "knowledge/dubai_market_context.json"
ABU_DHABI_FILE = "knowledge/abudhabi_summary.json"
OUTPUT_FILE = "knowledge/uae_market_knowledge.json"


def merge_knowledge():
    with open(DUBAI_FILE, "r", encoding="utf-8") as f:
        dubai_data = json.load(f)

    with open(ABU_DHABI_FILE, "r", encoding="utf-8") as f:
        abu_dhabi_data = json.load(f)

    final_data = {
        "dubai": dubai_data,
        "abu_dhabi": abu_dhabi_data
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    print(f"Done. Merged knowledge saved to {OUTPUT_FILE}")
    print("Cities included:", list(final_data.keys()))


if __name__ == "__main__":
    merge_knowledge()