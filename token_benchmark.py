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
    "name": "Rover-7X",
    "age": 3,
    "role": "Mars Exploration Robot",
    "skills": ["Terrain Navigation", "Sample Collection", "Atmospheric Analysis", "Autonomous Decision Making"],
    "experience_years": 3,
    "location": "Mars, Jezero Crater",
    "projects": [
        {
            "project_name": "Ancient Water Discovery",
            "description": "Located evidence of ancient water flows in crater formations.",
            "tech": ["Spectroscopy", "Ground Penetrating Radar", "AI Vision"]
        }
    ]
}

toon_data = """
name Rover-7X
age 3
role Mars Exploration Robot
skills Terrain Navigation, Sample Collection, Atmospheric Analysis, Autonomous Decision Making
experience_years 3
location Mars, Jezero Crater

project:
  project_name Ancient Water Discovery
  description Located evidence of ancient water flows in crater formations.
  tech Spectroscopy | Ground Penetrating Radar | AI Vision
"""

vsc_data = "Rover-7X,3,Mars Exploration Robot,Terrain Navigation|Sample Collection|Atmospheric Analysis|Autonomous Decision Making,3,Mars Jezero Crater,Ancient Water Discovery,Located evidence of ancient water flows in crater formations.,Spectroscopy;Ground Penetrating Radar;AI Vision"

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

