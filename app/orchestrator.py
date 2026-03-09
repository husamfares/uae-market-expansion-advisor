from app.planner import make_plan
from app.config import get_settings
from openai import OpenAI
from app.agents.location_agent import build_location_agent
from app.agents.competitor_agent import build_competitor_agent
from app.agents.menu_agent import build_menu_agent
from app.agents.pricing_agent import build_pricing_agent
from app.agents.marketing_agent import build_marketing_agent
from app.agents.delivery_agent import build_delivery_agent
from app.agents.operations_agent import build_operations_agent
from app.agents.market_entry_agent import build_market_entry_agent
from app.validator import DeterministicValidator


class Orchestrator:
    """
    Entry point controller.
    - gets a plan from planner
    - executes specialist agents
    - synthesizes one executive response
    """ 

    def __init__(self): 
        s = get_settings()
        self.client = OpenAI(api_key=s.openai_key)
        self.model_id = s.model_id
        self.validator = DeterministicValidator()


        self.agents = {
            "location": build_location_agent(),
            "competitor": build_competitor_agent(),
            "menu": build_menu_agent(),
            "pricing": build_pricing_agent(),
            "marketing": build_marketing_agent(),
            "delivery": build_delivery_agent(),
            "operations": build_operations_agent(),
            "market_entry": build_market_entry_agent(),

        }

    

    def answer(self , user_text: str ) -> str:
        plan = make_plan(user_text)

        city_scope = plan.get("cities", "both")
        agent_names = plan.get("agents", ["location"]) 

        results = {}

        for name in agent_names:
            agent = self.agents.get(name)

            if not agent:
                continue

            user_prompt = self._build_agent_prompt(agent_name=name , user_text=user_text , city_scope=city_scope)

            run = agent.run(user_prompt)

            results[name] = (run.content or "").strip()
        

        final_answer = self._synthesize(user_text=user_text , plan=plan , results=results)


        validation = self.validator.validate(final_answer, plan)

        if not validation.is_valid:
            error_text = "\n".join([f"- {e}" for e in validation.errors])

            final_answer = (
                final_answer
                + "\n\n"
                + "Validation Notes\n"
                + error_text
            )
            
        return final_answer



    def _build_agent_prompt(self , agent_name:str , user_text: str , city_scope):

        city_instruction = "Answer for BOTH Dubai and Abu Dhabi."
        
        if city_scope == "dubai":
            city_instruction = "Answer ONLY for Dubai."

        elif city_scope == "abudhabi":
            city_instruction = "Answer ONLY for Abu Dhabi."


        return(
            f"{city_instruction}\n"
            f"Restaurant concept: Jordanian brand focused on meaty pizza and kebab sandwiches.\n"
            f"User question: {user_text}\n"
            f"Your role: {agent_name} specialist.\n"
            f"Output must be structured and executive-friendly."
        )
    

    def _synthesize(self, user_text: str, plan: dict, results: dict) -> str:
        intent = plan.get("intent" , "strategy")
        cities = plan.get("cities" , "both")

        specialist_text = self._format_results(results=results)

        prompt = f"""
            You are the final executive synthesis layer for a UAE restaurant market expansion advisory system.

            Business context:
            You are advising a Jordanian fast-casual restaurant specializing in meaty pizza and kebab sandwiches.
            The business is evaluating expansion into Dubai and Abu Dhabi.

            Your job:
            Use the specialist analyses below to produce one clear, executive-ready final answer to the user's question.
            Your job is not to repeat every specialist section, but to combine them into a useful business recommendation.

            User question:
            {user_text}

            Planner output:
            - intent: {intent}
            - cities: {cities}

            Specialist analyses:
            {specialist_text}

            How to think:
            - Answer the user's exact question first.
            - Combine overlapping insights instead of repeating them.
            - Highlight the most decision-relevant points.
            - Preserve important tradeoffs and tensions between specialist views.
            - If specialist outputs imply a clear recommendation, state it directly.
            - If specialist outputs are incomplete or uncertain, state assumptions clearly.
            - Do not invent new facts, numbers, or claims that are not supported by the specialist analyses.

            What a strong final answer should do:
            - summarize the main strategic takeaway
            - surface the most important findings
            - make a practical recommendation
            - explain major risks or tradeoffs
            - identify what additional data would improve the decision

            Preferred output structure:
            1. Executive Summary
            2. Key Findings
            3. Final Recommendation
            4. Risks and Tradeoffs
            5. Next Data Needed
            6. Assumptions (only if needed)

            Style rules:
            - Write in executive-friendly language.
            - Be clear, practical, and commercially aware.
            - Avoid repetition.
            - Avoid generic filler.
            - Keep the answer structured and easy to scan.
            """

        response = self.client.responses.create( 
                model=self.model_id,
                input=prompt
        )

        return response.output_text
    


    def _format_results(self , results: dict) -> str:
        lines = []

        for name, content in results.items():
            lines.append(f"{name.upper()} ANALYSIS:")
            lines.append(content if content else "(No Output)")
            lines.append("")

        return "\n".join(lines)

