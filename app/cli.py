from app.orchestrator import Orchestrator

def main():
    orch = Orchestrator()
    print("UAE Market Expansion Advisor (type 'quit' to exit)")

    while True:
        user_text = input("\n You: ").strip()

        if user_text.lower() in ["quit" , "exit"]:
            break

        if not user_text:
            continue

        answer = orch.answer(user_text=user_text)
        print("\nAdvisor:\n")
        print(answer)

        
if __name__ == "__main__":
    main()

        