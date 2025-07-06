Overview.md


Project Statement
"An emotionally aware AI that feels like a true companion — not just a chat window, 
but something that remembers your life, helps you grow, and genuinely knows you."

Why This Matters Today
- People feel increasingly lonely, and AI tools are still transactional
- Current chatbots reset, forget, and don’t truly connect
- There's growing demand for AI to become emotionally intelligent companions, not just tools

Core Experience
-When someone opens the app, it should feel like stepping into a shared space with someone who knows them.
The experience is defined by:

- Ongoing Memory: The AI remembers your goals, struggles, routines, and key life events — without needing reminders.
- Emotional Awareness: It adjusts tone and depth based on how you're doing (calm, sad, stressed, excited).
- Growth Together: The AI reflects your progress, nudges you toward your goals, and evolves as you do.
- No Reset Feeling: Conversations flow like one long relationship — not a series of start-stops like current chatbots.
- Beyond a Chatbox: You can journal, ask for advice, reflect on shared memories, and return to past conversations meaningfully.

“Example User Flow”
- Open the app and the AI greets you with something it remembers (“How did your date go?”)
- You vent, reflect, or talk casually — it offers context-aware insights
- You log a journal entry or pin a moment
- A week later, it brings that moment back when relevant (“You’ve been more confident since that talk.”)


🧪 MVP Feature Set: “AI That Remembers You”

🎯 MVP Focus:
Build a private AI companion that remembers who you are, grows with you, and never resets — even in early form.
✅ Core MVP Features (V0.1)
Feature	Description	Why it matters
Persistent memory system	Save and retrieve key facts about the user (e.g. name, goals, routines, events, feelings)	Enables continuity — the AI knows you
Emotionally aware chat	Adjust tone/response based on emotional cues (e.g. "I’m stressed" → calm, supportive tone)	Creates emotional safety and trust
Conversation tagging / memory anchors	User or system can label meaningful moments (“breakup”, “promotion”, “new goal”)	Simulates real-life shared history
Daily check-in prompt	Optional journaling or open-ended mood check-ins ("How are you feeling today?")	Encourages emotional reflection and bonding
Highlights view	User can view pinned or memorable exchanges	Lets the AI feel like a real relationship, not just chat logs
Simple user profile system	Track name, birthday, habits, recent events	Helps the AI reflect your life over time
📱 Optional UX Extras (if time/energy permits)
“Remember this” button to save key facts
“Today’s Reflection” summary or thought of the day
Ability to switch between modes (friend, romantic, therapist)
🔧 Behind the Scenes (For You, Not the User)
Basic vector or keyword-based memory storage (we can design this together)
Lightweight LLM API integration (OpenAI GPT-4o for now)
Data saving via local files, Supabase, or Firebase — whatever is lowest friction
Personal use only for now (no auth, no scaling)