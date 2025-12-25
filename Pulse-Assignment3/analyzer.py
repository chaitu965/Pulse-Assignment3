import os
import json

try:
    from openai import OpenAI
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False


def rule_engine(texts):
    modules = {}

    for t in texts:
        low = t.lower()

        if "security" in low or "privacy" in low:
            modules.setdefault("Security & Privacy", {
                "Description": "Security and privacy related features.",
                "Submodules": {}
            })
            modules["Security & Privacy"]["Submodules"]["Security Settings"] = t

        elif "account" in low or "profile" in low:
            modules.setdefault("Account Management", {
                "Description": "User account and profile management.",
                "Submodules": {}
            })
            modules["Account Management"]["Submodules"]["Account Settings"] = t

        elif "plugin" in low or "extension" in low:
            modules.setdefault("Plugins", {
                "Description": "Platform extensions and plugins.",
                "Submodules": {}
            })
            modules["Plugins"]["Submodules"]["Plugin Usage"] = t

        elif "install" in low or "setup" in low:
            modules.setdefault("Getting Started", {
                "Description": "Installation and initial setup guidance.",
                "Submodules": {}
            })
            modules["Getting Started"]["Submodules"]["Installation"] = t

    return [
        {
            "module": m,
            "Description": d["Description"],
            "Submodules": d["Submodules"]
        }
        for m, d in modules.items()
    ]


def analyze(texts):
    if AI_AVAILABLE and os.getenv("OPENAI_API_KEY"):
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            content = "\n".join(texts)

            prompt = f"""
Extract software modules from the documentation below.
Return ONLY valid JSON in this format:

[
  {{
    "module": "Name",
    "Description": "Description",
    "Submodules": {{
      "Submodule": "Details"
    }}
  }}
]

CONTENT:
{content}
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )

            return json.loads(response.choices[0].message.content)

        except Exception:
            return rule_engine(texts)

    return rule_engine(texts)
