import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def build_prompt(user_input, memory):
    memory_prompt = f"""
You are an emotionally aware AI companion. Here is what you remember about the user:

Name: {memory.get("name")}
Goals: {", ".join(memory.get("goals", []))}
Recent Events: {", ".join(memory.get("recent_events", []))}
Core Traits: {", ".join(memory.get("core_traits", []))}
Pinned Moments:
"""

    for moment in memory.get("pinned_moments", []):
        memory_prompt += f"- {moment['summary']} ({moment['date']})\n"

    full_prompt = f"{memory_prompt}\nNow respond to the user.\nUser: {user_input}\nAI:"
    full_prompt += "\n\nIf the user's message includes anything emotionally significant or worth remembering (like events, emotions, goals), suggest one concise memory to save. Format it like this:\nMEMORY_SUGGESTION: <suggestion here>\n\nIf there's nothing new to remember, reply normally without this line."

    return full_prompt.strip()


from app.memory import add_memory_event


def get_ai_response(user_input, memory):
    prompt = build_prompt(user_input, memory)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # switch to gpt-3.5 if you're over quota
        messages=[
            {
                "role": "system",
                "content": "You are an emotionally intelligent AI companion who remembers the user.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=400,
    )

    full_reply = response.choices[0].message.content.strip()

    # Detect and extract memory suggestion
    lines = full_reply.split("\n")
    suggestion = None
    for line in lines:
        if line.startswith("MEMORY_SUGGESTION:"):
            suggestion = line.replace("MEMORY_SUGGESTION:", "").strip()

    if suggestion:
        add_memory_event(suggestion)
