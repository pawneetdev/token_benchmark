# Token Benchmark

A benchmarking tool to compare token usage across different data serialization formats (JSON, TOON, and VSC) when sending prompts to OpenAI's API.

## Overview

This tool measures and compares how many tokens different data formats consume when processed by OpenAI models. It's useful for optimizing API costs and understanding which format is most token-efficient for your use case.

## Formats Tested

- **JSON**: Standard JSON format with indentation
- **TOON**: Human-readable, whitespace-based format
- **VSC**: Value-Separated Compact format (CSV-like with delimiters)

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install openai
   ```

## Configuration

**Important**: Before running the script, you must set your OpenAI API key on line 7:

```python
client = OpenAI(api_key="YOUR_API_KEY")
```

Replace `"YOUR_API_KEY"` with your actual OpenAI API key.

## Usage

Run the benchmark script:

```bash
python token_benchmark.py
```

The script will:
1. Send the same data in three different formats to OpenAI's API
2. Measure token usage for each format
3. Display a summary comparison

## Benchmark Results

Based on test data (profile with skills, experience, and projects):

| Format | Input Tokens | Output Tokens | Total Tokens |
|--------|--------------|---------------|--------------|
| JSON   | 142          | 91            | **233**      |
| TOON   | 80           | 98            | **178**      |
| VSC    | 61           | 95            | **156**      |

**Winner**: VSC format uses **33% fewer tokens** than JSON.

## Customization

You can modify the test data in the script to benchmark your own use cases. The script uses `gpt-4o-mini` by default, but you can change the model on line 49.
