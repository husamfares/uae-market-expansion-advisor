import json


KNOWLEDGE_FILE = "knowledge/uae_market_knowledge.json"


def load_knowledge():
    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_city_data(city: str):
    data = load_knowledge()

    city = city.strip().lower()

    if city == "dubai":
        return data.get("dubai", {})
    elif city in ["abu dhabi", "abudhabi", "abu_dhabi"]:
        return data.get("abu_dhabi", {})
    else:
        return {}



def get_market_overview(city: str):
    """
    Retrieve high-level restaurant market context for a UAE city.

    Use this tool when you need:
    - general restaurant market conditions
    - demand signals
    - tourism influence on dining
    - delivery market importance

    Args:
        city (str): City name such as "Dubai" or "Abu Dhabi".

    Returns:
        dict: Market overview data extracted from the UAE market knowledge base.
    """
    city_data = get_city_data(city)
    return city_data.get("market_overview", {})



def get_strategic_notes(city: str):
    """
    Retrieve strategic insights and analyst-style notes about the restaurant
    market in a specific UAE city.

    Use this tool when you need:
    - high-level strategic observations about the market
    - expansion insights derived from reports or analysis
    - contextual notes about demand patterns or competitive pressure
    - guidance that may influence market entry strategy

    Args:
        city (str): City name such as "Dubai" or "Abu Dhabi".

    Returns:
        list: A list of strategic insights describing notable market dynamics
        that may affect restaurant expansion decisions.
    """
    city_data = get_city_data(city)
    return city_data.get("strategic_notes", [])



def get_location_clusters(city: str):
    """
    Retrieve known restaurant concentration areas for a city.

    Use this tool when recommending branch locations or analyzing
    restaurant density zones.

    Args:
        city: "Dubai" or "Abu Dhabi"

    Returns:
        list: Restaurant location clusters in the city.
    """
    city_data = get_city_data(city)
    return city_data.get("location_clusters", [])



def get_consumer_behavior(city: str):
    """
    Retrieve consumer dining and ordering behavior insights for a UAE city.

    Use this tool when you need:
    - customer ordering preferences
    - delivery vs dine-in behavior patterns
    - family dining tendencies
    - late-night or convenience-driven ordering signals

    This tool is useful when designing:
    - menu strategy
    - marketing messaging
    - restaurant format (delivery-first vs dine-in)

    Args:
        city (str): City name such as "Dubai" or "Abu Dhabi".

    Returns:
        dict: Structured information describing how customers typically
        interact with restaurants in the given city.
    """
    city_data = get_city_data(city)
    return city_data.get("consumer_behavior", {})



def get_cuisine_signals(city: str):
    """
    Retrieve signals about cuisine popularity and demand trends in a city.

    Use this tool when analyzing:
    - which cuisine categories are strong or growing
    - competitive pressure from specific food types
    - whether a restaurant concept fits local demand

    This tool is particularly useful for:
    - competitor analysis
    - menu strategy
    - concept positioning decisions

    Args:
        city (str): City name such as "Dubai" or "Abu Dhabi".

    Returns:
        dict: Data describing cuisine popularity signals or cuisine
        demand patterns in the city.
    """
    city_data = get_city_data(city)

    if "cuisine_signals" in city_data:
        return city_data.get("cuisine_signals", {})

    if "cuisine_popularity" in city_data:
        return city_data.get("cuisine_popularity", {})

    return {}



def get_marketing_signals(city: str):
    """
    Retrieve information about how restaurant customers discover
    and engage with restaurants in a UAE city.

    Use this tool when planning:
    - marketing channel strategy
    - launch campaigns
    - digital visibility strategy
    - partnerships and local promotions

    The data may include signals about:
    - social media influence
    - delivery platform importance
    - search or map-based discovery
    - local promotion effectiveness

    Args:
        city (str): City name such as "Dubai" or "Abu Dhabi".

    Returns:
        dict: Marketing behavior signals that describe how customers
        typically discover and interact with restaurants.
    """

    city_data = get_city_data(city)

    if "marketing_signals" in city_data:
        return city_data.get("marketing_signals", {})

    if "marketing_behavior" in city_data:
        return city_data.get("marketing_behavior", {})

    return {}