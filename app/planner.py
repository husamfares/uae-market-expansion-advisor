import json
from agno.agent import Agent
from agno.models.openai import OpenAIChat

from app.config import get_settings

def  build_planner_agent() -> Agent:

    s = get_settings()

    return Agent(
        model=OpenAIChat(id=s.model_id),
        markdown=False,
        instructions = [
            "You are the routing planner for a UAE restaurant market expansion advisory system.",

            "Business context:",
            "The system advises a Jordanian fast-casual restaurant specializing in meaty pizza and kebab sandwiches.",
            "The expansion scope is Dubai and Abu Dhabi.",
            "Your job is to analyze the user's question and decide which specialist agents are needed to answer it well.",

            "Your output must be ONLY valid JSON.",
            "Do not write explanations.",
            "Do not write markdown.",
            "Do not add text before or after the JSON.",

            "JSON schema (must match exactly):",
            '{',
            '  "intent": "location|competitor|menu|pricing|marketing|operations|delivery|market_entry|strategy",',
            '  "cities": "dubai|abudhabi|both",',
            '  "agents": ["location","competitor","menu","pricing","marketing","operations","delivery","market_entry"],',
            '  "needs_extra_items": true|false',
            '}',

            "How to think about routing:",
            "A narrow specialist question should usually route to one main agent.",
            "A cross-functional or executive planning question should route to multiple relevant agents.",
            "Use the minimum number of agents needed to answer well.",
            "Do not add extra agents unless they are clearly useful.",
            "Prefer cost-efficient routing.",

            "Intent rules:",
            "- location: questions about where to open, which area to choose, or branch location comparison",
            "- competitor: questions about competitor categories, brands, positioning, threats, or differentiation",
            "- menu: questions about menu adaptation, localization, portions, combos, or delivery-friendly menu design",
            "- pricing: questions about price ranges, market positioning, pricing logic, delivery pricing, or promotions",
            "- marketing: questions about launch plans, channels, messaging, partnerships, or go-to-market activity",
            "- operations: questions about staffing, execution, delivery operations, suppliers, licensing, or other non-core operational topics",
            "- strategy: broad questions that require combining multiple business perspectives",

            "City rules:",
            "- If the user clearly asks about Dubai only, set cities='dubai'.",
            "- If the user clearly asks about Abu Dhabi only, set cities='abudhabi'.",
            "- If the user asks generally about UAE expansion or does not specify one city, set cities='both'.",

            "Agent selection rules:",
            "- Include only the agents needed for the question.",
            "- For broad strategic questions, select multiple relevant agents.",
            "- For simple questions, keep routing minimal.",
            "- If the question asks for a full plan, go-to-market plan, expansion strategy, or executive recommendation, intent should usually be 'strategy'.",

            "Extra item rule:",
            "- Set needs_extra_items=true when the user asks for a broad strategy, full expansion plan, or go-to-market plan.",
            "- Otherwise set needs_extra_items=false."
        ],
    )


def make_plan(user_text : str) -> dict:
    planner = build_planner_agent()
    
    result = planner.run(user_text) 
    raw = (result.content or "").strip() 

    try:
        plan = json.loads(raw)

    except:
        plan = {
            "intent": "strategy",
            "cities": "both",
            "agents": ["location"],
            "needs_extra_items": True,
        }



    if "agents" not in plan or not isinstance(plan["agents"], list) or not plan["agents"]:
        plan["agents"] = ["location"]
    if "cities" not in plan:
        plan["cities"] = "both"
    if "intent" not in plan:
        plan["intent"] = "strategy"
    if "needs_extra_items" not in plan:
        plan["needs_extra_items"] = (plan["intent"] == "strategy")

    return plan

