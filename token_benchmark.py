from openai import OpenAI
import json

# -----------------------------------------
# Setup
# -----------------------------------------
client = OpenAI(api_key="YOUR_API_KEY")

# -----------------------------------------
# Test Data (Bigger Prompt)
# -----------------------------------------
json_data = {
    "name": "Pawneet Singh",
    "age": 32,
    "role": "Staff Software Engineer",
    "skills": ["Python", "System Design", "Distributed Systems", "AI"],
    "experience_years": 9,
    "location": "India",
    "projects": [
        {
            "project_name": "LuminSkin AI",
            "description": "AI powered skincare routine generator.",
            "tech": ["OpenAI", "Groq LPU", "NextJS"]
        }
    ]
}

toon_data = """
name Pawneet Singh
age 32
role Staff Software Engineer
skills Python, System Design, Distributed Systems, AI
experience_years 9
location India

project:
  project_name LuminSkin AI
  description AI powered skincare routine generator.
  tech OpenAI | Groq LPU | NextJS
"""

vsc_data = "Pawneet Singh,32,Staff Software Engineer,Python|System Design|Distributed Systems|AI,9,India,LuminSkin AI,AI powered skincare routine generator.,OpenAI;Groq LPU;NextJS"

# -----------------------------------------
# Benchmark Function
# -----------------------------------------
def benchmark_format(label, content):
    response = client.responses.create(
        model="gpt-4o-mini",  # Change model if needed
        input=f"Summarise the following profile data accurately:\n{content}"
    )

    usage = response.usage

    print(f"\n--- {label} ---")
    print("Input tokens:", usage.input_tokens)
    print("Output tokens:", usage.output_tokens)
    print("Total tokens:", usage.total_tokens)

    return usage.total_tokens

# -----------------------------------------
# Run Benchmarks
# -----------------------------------------
json_total = benchmark_format("JSON", json.dumps(json_data, indent=2))
toon_total = benchmark_format("TOON", toon_data.strip())
vsc_total = benchmark_format("VSC", vsc_data)

# -----------------------------------------
# Summary
# -----------------------------------------
print("\n===== SUMMARY =====")
print(f"JSON Tokens: {json_total}")
print(f"TOON Tokens: {toon_total}")
print(f"VSC Tokens:  {vsc_total}")

