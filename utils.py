def build_prompt(content_type, genre, mood, difficulty):
    return f"""
You are an expert RPG game designer.

Generate ONLY a {mood} {genre} {content_type} for a turn-based RPG game.

STRICT RULES:
- Stay in fantasy RPG context
- Do NOT generate random text, emails, or unrelated content
- Follow the exact format below

FORMAT:

Title:
Objective:
Location:
Enemy:
Reward:
Twist:

OUTPUT:
"""