import re
from openai import AsyncOpenAI, OpenAI

OPENAI_API_KEY = ""

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY,  
)
sync_client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def llm_call(prompt: str,  model: str = "gpt-4o-mini") -> str:
    messages = []
    messages.append({"role": "user", "content": prompt})
    chat_completion = sync_client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return chat_completion.choices[0].message.content


async def llm_call_async(prompt: str,  model: str = "gpt-4o-mini") -> str:
    messages = []
    messages.append({"role": "user", "content": prompt})
    chat_completion = await client.chat.completions.create(
        model=model,
        messages=messages,
    )
    print(model,"Done")
    
    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    test = llm_call("Hello~")
    print(test)

