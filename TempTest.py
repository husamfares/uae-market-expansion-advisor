from app.agents.location_agent import build_location_agent
from app.agents.menu_agent import build_menu_agent
from app.agents.competitor_agent import build_competitor_agent
from app.agents.marketing_agent import build_marketing_agent
from app.agents.delivery_agent import build_delivery_agent
from app.agents.operations_agent import build_operations_agent

agent = build_operations_agent()
result = agent.run("What operating model and staffing approach should we use for our first branch in Dubai?")
print(result.content)