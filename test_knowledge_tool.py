from app.tools.knowledge_tool import (
    get_market_overview,
    get_location_clusters,
    get_strategic_notes,
)

print("Dubai market overview:")
print(get_market_overview("Dubai"))

print("\nAbu Dhabi location clusters:")
print(get_location_clusters("Abu Dhabi")[:3])

print("\nDubai strategic notes:")
print(get_strategic_notes("Dubai"))