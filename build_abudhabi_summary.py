import json
from collections import defaultdict

INPUT_FILE = "knowledge/abudhabi_restaurants_clean.json"
OUTPUT_FILE = "knowledge/abudhabi_summary.json"


def build_summary():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    restaurants = data.get("restaurants", [])

    location_map = defaultdict(list)

    for item in restaurants:
        location = item.get("location", "").strip()

        if not location:
            continue

        location_map[location].append(item)

    location_clusters = []

    for location, items in location_map.items():
        cluster = {
            "location": location,
            "restaurant_count": len(items),
            "sample_restaurants": [x["establishment_name"] for x in items[:5]]
        }
        location_clusters.append(cluster)

    location_clusters.sort(key=lambda x: x["restaurant_count"], reverse=True)

    summary = {
        "city": "Abu Dhabi",
        "city_type": "location_market",
        "market_overview": {
            "total_restaurant_records": len(restaurants),
            "unique_locations": len(location_clusters)
        },
        "location_clusters": location_clusters[:30],
        "strategic_notes": [
            "This dataset is useful for restaurant location mapping and competitor clustering.",
            "The data is location-rich but does not include pricing, customer demand, or menu-level behavior.",
            "Repeated hotel or district names may indicate hospitality and tourism-linked restaurant clusters."
        ]
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"Done. Summary saved to {OUTPUT_FILE}")
    print(f"Total restaurant records: {len(restaurants)}")
    print(f"Unique locations: {len(location_clusters)}")


if __name__ == "__main__":
    build_summary()