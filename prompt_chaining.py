

from typing import List
from utils import llm_call

def prompt_chain_workflow(initial_input: str, prompt_chain: List[str]) -> List[str]:
    response_chain = []
    response = initial_input

    for i, prompt in enumerate(prompt_chain, 1):
        print(f"\n==== STEP {i} ====\n")
        final_prompt = f"{prompt}\nUser Input:\n{response}"
        print(f"🔹 Prompt:\n{final_prompt}\n")

        response = llm_call(final_prompt)
        response_chain.append(response)
        print(f"✅ Response:\n{response}\n")

    return response_chain


## When you need to keep the initial input value!
def prompt_chain_workflow_2(initial_input: str, prompt_chain: List[str]) -> List[str]:
    response_chain = []
    response = initial_input

    for i, prompt in enumerate(prompt_chain, 1):
        print(f"\n==== STEP {i} ====\n")
        final_prompt = f"{prompt}\n\n🔹 Context:\n{response}\n🔹 User Input: {initial_input}"
        print(f"🔹 Prompt:\n{final_prompt}\n")

        response = llm_call(final_prompt)
        response_chain.append(response)
        print(f"✅ Response:\n{response}\n")

    return response_chain


initial_input ="""
My guests(two ladys) planning to travel to Charlotte, NC for three days. Could you recommend some places to visit in and around Charlotte?
"""

# Prompt Chain: 
prompt_chain = [
    
"""Please recommend some places that are worth visiting for tourists.
- Summarize the visitor's preferences.
– Explain why each recommended place is a good choice.
– Describe what activities can be done at each location."
""",

    
"""Please create a 3-day itinerary that includes the recommended places.
– Divide each day into morning, afternoon, and evening.
– For each time slot, suggest what activities would be good to do.
""",
]

responses = prompt_chain_workflow_2(initial_input,prompt_chain)

final_answer = responses[-1]
print(final_answer)

