from openai import OpenAI
import json

client = OpenAI(api_key="YOUR_API_KEY")

# ---------- Test Data ----------
json_data = {
    "name": "Alice",
    "role": "Engineer",
    "age": 25
}

toon_data = """
name Alice
role Engineer
age 25
"""

vsc_data = "Alice,Engineer,25"

# ---------- Helper Function ----------
def benchmark_format(label, content):
    response = client.responses.create(
        model="gpt-4o-mini",   # change your model here
        input=f"Read this data and summarise it:\n{content}"
    )

    usage = response.usage
    print(f"\n--- {label} ---")
    print("Prompt tokens:", usage.prompt_tokens)
    print("Completion tokens:", usage.completion_tokens)
    print("Total tokens:", usage.total_tokens)
    return usage.total_tokens

# ---------- Run Benchmarks ----------
json_total = benchmark_format("JSON", json.dumps(json_data, indent=2))
toon_total = benchmark_format("TOON", toon_data.strip())
vsc_total = benchmark_format("VSC", vsc_data)

# ---------- Comparison ----------
print("\n===== SUMMARY =====")
print(f"JSON Tokens: {json_total}")
print(f"TOON Tokens: {toon_total}")
print(f"VSC Tokens:  {vsc_total}")

